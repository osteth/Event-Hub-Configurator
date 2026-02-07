"""Validator Panel - Validate SQL files"""

import os
from pathlib import Path

from PyQt5.QtWidgets import (
    QDockWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog,
    QTextEdit, QMessageBox, QProgressDialog
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from core.validator import validate_bulk_upload
from gui.utils.file_utils import open_file_in_editor, open_file_location


class ValidatorWorker(QThread):
    """Worker thread for validation"""
    
    finished = pyqtSignal(dict)
    
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
    
    def run(self):
        """Run validation"""
        import os
        
        # Verify file path was passed correctly
        if not self.file_path:
            self.finished.emit({
                'success': False,
                'errors': ['No file path provided to validator worker thread'],
                'warnings': [],
                'file_count': 0,
                'error_count': 1,
                'warning_count': 0
            })
            return
        
        # Verify file exists
        if not os.path.exists(self.file_path):
            self.finished.emit({
                'success': False,
                'errors': [f'File not found: {self.file_path}\n\nPlease check that the file exists and the path is correct.'],
                'warnings': [],
                'file_count': 0,
                'error_count': 1,
                'warning_count': 0
            })
            return
        
        # Ensure we have an absolute path
        if not os.path.isabs(self.file_path):
            self.file_path = os.path.abspath(self.file_path)
        
        # Force reload of validator module to ensure we're using the latest version
        # This is important because Python caches imported modules and .pyc files
        import importlib
        import sys
        from pathlib import Path
        
        # Remove cached modules from sys.modules to force fresh import
        modules_to_remove = [key for key in sys.modules.keys() if 'validate_sql' in key or key == 'core.validator']
        for module_name in modules_to_remove:
            del sys.modules[module_name]
        
        # Also clear the core.validator module
        if 'core.validator' in sys.modules:
            del sys.modules['core.validator']
        
        # Now import fresh
        from core.validator import validate_bulk_upload
        
        # Call validator with the file path
        result = validate_bulk_upload(self.file_path)
        self.finished.emit(result)


class ValidatorPanel(QDockWidget):
    """Panel for validating SQL files"""
    
    def __init__(self, parent=None):
        super().__init__('SQL Validator', parent)
        self.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.worker = None  # Keep reference to worker thread
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface"""
        widget = QWidget()
        widget.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #e0e0e0;
            }
            QLineEdit {
                background-color: #353535;
                color: #e0e0e0;
                border: 1px solid #555555;
                padding: 3px;
            }
            QPushButton {
                background-color: #404040;
                color: #e0e0e0;
                border: 1px solid #555555;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QPushButton:pressed {
                background-color: #606060;
            }
            QLabel {
                background-color: transparent;
                color: #e0e0e0;
            }
            QTextEdit {
                background-color: #353535;
                color: #e0e0e0;
                border: 1px solid #555555;
            }
        """)
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        widget.setLayout(layout)
        self.setWidget(widget)
        
        # File input
        file_layout = QHBoxLayout()
        file_label = QLabel('SQL File:')
        file_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        file_layout.addWidget(file_label)
        self.file_path_edit = QLineEdit()
        self.file_path_edit.setPlaceholderText('Select SQL file to validate...')
        file_layout.addWidget(self.file_path_edit)
        
        browse_btn = QPushButton('Browse...')
        browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(browse_btn)
        layout.addLayout(file_layout)
        
        # Validate button
        validate_btn = QPushButton('Validate')
        # Connect without passing the clicked signal's boolean argument
        validate_btn.clicked.connect(lambda: self.validate_file())
        layout.addWidget(validate_btn)
        
        # Results
        results_label = QLabel('Results:')
        results_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        layout.addWidget(results_label)
        
        # Status
        self.status_label = QLabel('(not validated yet)')
        self.status_label.setStyleSheet('font-weight: bold; color: #e0e0e0; background-color: transparent;')
        layout.addWidget(self.status_label)
        
        # Statistics
        self.stats_label = QLabel('')
        self.stats_label.setStyleSheet('color: #e0e0e0; background-color: transparent;')
        layout.addWidget(self.stats_label)
        
        # Errors
        errors_label = QLabel('Errors:')
        errors_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        layout.addWidget(errors_label)
        
        self.errors_text = QTextEdit()
        self.errors_text.setReadOnly(True)
        layout.addWidget(self.errors_text)
        
        # Warnings
        warnings_label = QLabel('Warnings:')
        warnings_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        layout.addWidget(warnings_label)
        
        self.warnings_text = QTextEdit()
        self.warnings_text.setReadOnly(True)
        layout.addWidget(self.warnings_text)
        
        # Action buttons
        action_layout = QHBoxLayout()
        
        export_btn = QPushButton('Export Report')
        export_btn.clicked.connect(self.export_report)
        action_layout.addWidget(export_btn)
        
        open_file_btn = QPushButton('Open File')
        open_file_btn.clicked.connect(self.open_file)
        action_layout.addWidget(open_file_btn)
        
        layout.addLayout(action_layout)
    
    def browse_file(self):
        """Browse for SQL file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Select SQL File',
            '',
            'SQL Files (*.sql);;All Files (*.*)'
        )
        
        if file_path:
            self.file_path_edit.setText(file_path)
    
    def validate_file(self, file_path=None):
        """Validate SQL file"""
        # Get file path from parameter or text field
        # Handle case where file_path might be passed as boolean or other type
        if file_path is None or not isinstance(file_path, str):
            # Read from text field
            file_path = self.file_path_edit.text().strip()
        else:
            # If path was provided as parameter, ensure it's a string and update the text field
            file_path = str(file_path).strip()
            self.file_path_edit.setText(file_path)
        
        # Check if we have a file path
        if not file_path or file_path == '' or file_path == 'Select SQL file to validate...':
            QMessageBox.warning(
                self, 
                'No File Selected', 
                'Please select a SQL file to validate.\n\nUse the "Browse..." button to select a file, or enter the file path in the text field.'
            )
            return
        
        # Resolve relative paths to absolute
        original_path = file_path
        
        # First, try to resolve as absolute path
        if not os.path.isabs(file_path):
            # Try to resolve relative to current working directory first
            abs_path = os.path.abspath(file_path)
            if os.path.exists(abs_path):
                file_path = abs_path
            else:
                # Try relative to the Event-Hub-Configurator directory
                script_dir = Path(__file__).parent.parent.parent.parent
                test_path = script_dir / file_path
                if test_path.exists():
                    file_path = str(test_path.resolve())
                else:
                    # Try relative to parent of script dir (where bulk uploads are created)
                    parent_dir = script_dir.parent
                    test_path = parent_dir / file_path
                    if test_path.exists():
                        file_path = str(test_path.resolve())
                    else:
                        # Last resort: use abspath even if it doesn't exist (will error below)
                        file_path = abs_path
        else:
            # Already absolute, but resolve any relative components
            file_path = str(Path(file_path).resolve())
        
        # Verify file exists with the resolved path
        if not os.path.exists(file_path):
            QMessageBox.warning(
                self, 
                'File Not Found', 
                f'SQL file not found:\n\nOriginal: {original_path}\nResolved: {file_path}\n\nPlease check the file path and try again.'
            )
            return
        
        # Show progress
        progress = QProgressDialog('Validating SQL file...', 'Cancel', 0, 0, self)
        progress.setWindowModality(Qt.WindowModal)
        progress.setStyleSheet("""
            QProgressDialog {
                background-color: #2b2b2b;
                color: #e0e0e0;
            }
            QProgressBar {
                background-color: #353535;
                border: 1px solid #555555;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #0066cc;
            }
            QPushButton {
                background-color: #404040;
                color: #e0e0e0;
                border: 1px solid #555555;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QLabel {
                color: #e0e0e0;
            }
        """)
        progress.show()
        
        # Clean up any existing worker thread
        if self.worker and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait(1000)  # Wait up to 1 second
        
        # Verify file path is valid before starting worker
        if not file_path:
            progress.close()
            QMessageBox.warning(
                self,
                'Error',
                'No file path provided to validator. Please select a SQL file.'
            )
            return
        
        if not os.path.exists(file_path):
            progress.close()
            QMessageBox.warning(
                self,
                'File Not Found',
                f'File does not exist:\n\n{file_path}\n\nPlease check the file path and try again.'
            )
            return
        
        # Create worker thread (keep reference to prevent garbage collection)
        # Pass the absolute, verified file path
        self.worker = ValidatorWorker(file_path)
        self.worker.finished.connect(lambda result: self.on_validation_finished(result, progress))
        self.worker.finished.connect(self.cleanup_worker)  # Clean up when done
        self.worker.start()
    
    def cleanup_worker(self):
        """Clean up worker thread"""
        if self.worker:
            if self.worker.isRunning():
                self.worker.wait()  # Wait for thread to finish
            self.worker.deleteLater()  # Schedule for deletion
            self.worker = None
    
    def on_validation_finished(self, result, progress):
        """Handle validation completion"""
        progress.close()
        
        # Update status
        if result['success']:
            self.status_label.setText('✓ Validation PASSED')
            self.status_label.setStyleSheet('font-weight: bold; color: #4caf50; background-color: transparent;')
        else:
            self.status_label.setText('✗ Validation FAILED')
            self.status_label.setStyleSheet('font-weight: bold; color: #f44336; background-color: transparent;')
        
        # Update statistics
        stats_text = (
            f"Files checked: {result['file_count']}\n"
            f"Errors: {result['error_count']}\n"
            f"Warnings: {result['warning_count']}"
        )
        self.stats_label.setText(stats_text)
        
        # Update errors
        if result['errors']:
            self.errors_text.setText('\n'.join(result['errors']))
        else:
            self.errors_text.setText('No errors found.')
        
        # Update warnings
        if result['warnings']:
            self.warnings_text.setText('\n'.join(result['warnings']))
        else:
            self.warnings_text.setText('No warnings found.')
    
    def export_report(self):
        """Export validation report to file"""
        sql_file_path = self.file_path_edit.text().strip()
        if not sql_file_path:
            QMessageBox.warning(self, 'Warning', 'Please select a SQL file to export a report for.')
            return
        
        # Resolve relative paths to absolute for display
        if not os.path.isabs(sql_file_path):
            script_dir = Path(__file__).parent.parent.parent.parent
            parent_dir = script_dir.parent
            resolved_path = parent_dir / sql_file_path
            if resolved_path.exists():
                sql_file_path = str(resolved_path)
            else:
                sql_file_path = os.path.abspath(sql_file_path)
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            'Save Validation Report',
            '',
            'Text Files (*.txt);;All Files (*.*)'
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('SQL Validation Report\n')
                    f.write('=' * 80 + '\n\n')
                    f.write(f"File: {sql_file_path}\n")
                    f.write(f"Status: {self.status_label.text()}\n")
                    f.write(f"{self.stats_label.text()}\n\n")
                    f.write('Errors:\n')
                    f.write('-' * 80 + '\n')
                    f.write(self.errors_text.toPlainText())
                    f.write('\n\nWarnings:\n')
                    f.write('-' * 80 + '\n')
                    f.write(self.warnings_text.toPlainText())
                
                QMessageBox.information(self, 'Success', f'Report saved to:\n{file_path}')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to save report: {e}')
    
    def open_file(self):
        """Open the SQL file in editor"""
        file_path = self.file_path_edit.text().strip()
        if not file_path:
            QMessageBox.warning(self, 'Warning', 'Please select a SQL file.')
            return
        
        # Resolve relative paths to absolute
        if not os.path.isabs(file_path):
            script_dir = Path(__file__).parent.parent.parent.parent
            parent_dir = script_dir.parent
            resolved_path = parent_dir / file_path
            if resolved_path.exists():
                file_path = str(resolved_path)
            else:
                file_path = os.path.abspath(file_path)
        
        # Check if file exists
        if not os.path.exists(file_path):
            QMessageBox.warning(self, 'Warning', f'File not found:\n{file_path}')
            return
        
        try:
            open_file_in_editor(file_path)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to open file: {e}')
