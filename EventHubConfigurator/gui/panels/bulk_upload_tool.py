"""Bulk Upload Tool Panel - Create bulk upload SQL file"""

from PyQt5.QtWidgets import (
    QDockWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog,
    QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal

from core.bulk_upload import create_bulk_upload_file
from gui.utils.file_utils import open_file_location, open_file_in_editor


class BulkUploadToolPanel(QDockWidget):
    """Panel for creating bulk upload SQL files"""
    
    upload_created = pyqtSignal(str)  # Emits path to created file
    
    def __init__(self, parent=None):
        super().__init__('Bulk Upload Tool', parent)
        self.setAllowedAreas(Qt.AllDockWidgetAreas)
        
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
            QTreeWidget {
                background-color: #353535;
                color: #e0e0e0;
                border: 1px solid #555555;
                alternate-background-color: #3c3c3c;
            }
            QTreeWidget::item:selected {
                background-color: #505050;
                color: #ffffff;
            }
            QHeaderView::section {
                background-color: #404040;
                color: #e0e0e0;
                padding: 4px;
                border: 1px solid #555555;
                font-weight: bold;
            }
        """)
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        widget.setLayout(layout)
        self.setWidget(widget)
        
        # SQL directory input
        sql_dir_layout = QHBoxLayout()
        sql_dir_label = QLabel('SQL Files Directory:')
        sql_dir_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        sql_dir_layout.addWidget(sql_dir_label)
        self.sql_dir_edit = QLineEdit()
        self.sql_dir_edit.setPlaceholderText('Directory containing SQL files...')
        sql_dir_layout.addWidget(self.sql_dir_edit)
        
        sql_dir_browse_btn = QPushButton('Browse...')
        sql_dir_browse_btn.clicked.connect(self.browse_sql_dir)
        sql_dir_layout.addWidget(sql_dir_browse_btn)
        
        auto_detect_btn = QPushButton('Auto-detect')
        auto_detect_btn.clicked.connect(self.auto_detect_sql_dir)
        sql_dir_layout.addWidget(auto_detect_btn)
        layout.addLayout(sql_dir_layout)
        
        # Output file
        output_layout = QHBoxLayout()
        output_label = QLabel('Output File:')
        output_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        output_layout.addWidget(output_label)
        self.output_file_edit = QLineEdit()
        self.output_file_edit.setPlaceholderText('(default: timestamped name)')
        output_layout.addWidget(self.output_file_edit)
        
        output_browse_btn = QPushButton('Browse...')
        output_browse_btn.clicked.connect(self.browse_output_file)
        output_layout.addWidget(output_browse_btn)
        layout.addLayout(output_layout)
        
        # Create button
        create_btn = QPushButton('Create Bulk Upload')
        create_btn.clicked.connect(self.create_bulk_upload)
        layout.addWidget(create_btn)
        
        # Results
        results_label = QLabel('Results:')
        results_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        layout.addWidget(results_label)
        
        self.file_path_label = QLabel('(not created yet)')
        self.file_path_label.setStyleSheet('color: #b0b0b0; background-color: transparent;')
        layout.addWidget(self.file_path_label)
        
        self.file_size_label = QLabel('')
        self.file_size_label.setStyleSheet('color: #b0b0b0; background-color: transparent;')
        layout.addWidget(self.file_size_label)
        
        self.file_count_label = QLabel('')
        self.file_count_label.setStyleSheet('color: #b0b0b0; background-color: transparent;')
        layout.addWidget(self.file_count_label)
        
        # Action buttons
        action_layout = QHBoxLayout()
        
        preview_btn = QPushButton('Preview')
        preview_btn.clicked.connect(self.preview_file)
        action_layout.addWidget(preview_btn)
        
        open_location_btn = QPushButton('Open File Location')
        open_location_btn.clicked.connect(self.open_file_location)
        action_layout.addWidget(open_location_btn)
        
        validate_btn = QPushButton('Validate Now')
        validate_btn.clicked.connect(self.validate_file)
        action_layout.addWidget(validate_btn)
        
        layout.addLayout(action_layout)
    
    def browse_sql_dir(self):
        """Browse for SQL files directory"""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            'Select SQL Files Directory'
        )
        
        if dir_path:
            self.sql_dir_edit.setText(dir_path)
    
    def auto_detect_sql_dir(self):
        """Auto-detect SQL directory from common locations"""
        import os
        from pathlib import Path
        
        # Try to find Low/Mid/High Event Sequence directories
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        
        for check_dir in [current_dir, parent_dir]:
            for tier in ['Low', 'Mid', 'High']:
                tier_dir = os.path.join(check_dir, f'{tier} Event Sequence')
                if os.path.exists(tier_dir):
                    self.sql_dir_edit.setText(check_dir)
                    QMessageBox.information(self, 'Auto-detected', f'Found SQL files in:\n{check_dir}')
                    return
        
        QMessageBox.warning(self, 'Not Found', 'Could not auto-detect SQL files directory.')
    
    def browse_output_file(self):
        """Browse for output file"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            'Save Bulk Upload File',
            '',
            'SQL Files (*.sql);;All Files (*.*)'
        )
        
        if file_path:
            self.output_file_edit.setText(file_path)
    
    def create_bulk_upload(self):
        """Create bulk upload file"""
        sql_dir = self.sql_dir_edit.text().strip()
        if not sql_dir:
            QMessageBox.warning(self, 'Warning', 'Please select SQL files directory.')
            return
        
        # Validate directory exists
        import os
        if not os.path.exists(sql_dir):
            QMessageBox.critical(self, 'Error', f'SQL directory does not exist:\n{sql_dir}')
            return
        
        output_file = self.output_file_edit.text().strip() or None
        
        try:
            result_file = create_bulk_upload_file(sql_dir, output_file)
            
            if not result_file or not os.path.exists(result_file):
                raise Exception("Bulk upload file was not created successfully")
            
            self.file_path_label.setText(f'File: {result_file}')
            
            # Get file size
            file_size = os.path.getsize(result_file)
            size_mb = file_size / (1024 * 1024)
            self.file_size_label.setText(f'Size: {size_mb:.2f} MB ({file_size:,} bytes)')
            
            # Count files (approximate from directory)
            file_count = 0
            for tier in ['Low', 'Mid', 'High']:
                tier_dir = os.path.join(sql_dir, f'{tier} Event Sequence')
                if os.path.exists(tier_dir):
                    for root, dirs, files in os.walk(tier_dir):
                        file_count += len([f for f in files if f.endswith('.sql')])
            
            # Add root files
            if os.path.exists(sql_dir):
                for f in os.listdir(sql_dir):
                    if f.endswith('.sql') and ('Event' in f or 'Bell' in f):
                        file_count += 1
            
            self.file_count_label.setText(f'Files included: {file_count}')
            
            self.upload_created.emit(result_file)
            
            QMessageBox.information(self, 'Success', f'Bulk upload file created:\n{result_file}')
            
        except Exception as e:
            import traceback
            error_msg = f"{str(e)}"
            if hasattr(e, '__traceback__'):
                error_msg += f"\n\n{traceback.format_exc()}"
            QMessageBox.critical(self, 'Error', f'Failed to create bulk upload:\n{error_msg}')
    
    def preview_file(self):
        """Preview the created file"""
        file_path = self.file_path_label.text().replace('File: ', '')
        if file_path and file_path != '(not created yet)':
            open_file_in_editor(file_path)
        else:
            QMessageBox.warning(self, 'Warning', 'No file to preview.')
    
    def open_file_location(self):
        """Open file location in Windows Explorer"""
        file_path = self.file_path_label.text().replace('File: ', '')
        if file_path and file_path != '(not created yet)':
            open_file_location(file_path)
        else:
            QMessageBox.warning(self, 'Warning', 'No file location to open.')
    
    def validate_file(self):
        """Open validator with this file"""
        file_path = self.file_path_label.text().replace('File: ', '')
        if file_path and file_path != '(not created yet)':
            self.upload_created.emit(file_path)
            # TODO: Show validator panel
        else:
            QMessageBox.warning(self, 'Warning', 'No file to validate.')
