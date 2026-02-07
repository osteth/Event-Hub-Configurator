"""SQL Builder Panel - Generate SQL files from configuration"""

from PyQt5.QtWidgets import (
    QDockWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog,
    QTreeWidget, QTreeWidgetItem, QProgressDialog,
    QMessageBox, QHeaderView
)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from core.sql_generator import generate_sql_files


class SQLBuilderWorker(QThread):
    """Worker thread for SQL generation"""
    
    finished = pyqtSignal(dict)
    
    def __init__(self, config_path, output_dir):
        super().__init__()
        self.config_path = config_path
        self.output_dir = output_dir
    
    def run(self):
        """Run SQL generation"""
        try:
            result = generate_sql_files(self.config_path, self.output_dir)
            self.finished.emit(result)
        except Exception as e:
            import traceback
            error_msg = f"{str(e)}\n{traceback.format_exc()}"
            self.finished.emit({
                'success': False,
                'files': [],
                'output_dir': self.output_dir or '',
                'error': error_msg
            })


class SQLBuilderPanel(QDockWidget):
    """Panel for generating SQL files"""
    
    def __init__(self, parent=None):
        super().__init__('SQL Builder', parent)
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
        
        # Config file input
        config_layout = QHBoxLayout()
        config_label = QLabel('Config File:')
        config_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        config_layout.addWidget(config_label)
        self.config_path_edit = QLineEdit()
        self.config_path_edit.setPlaceholderText('Select configuration CSV file...')
        config_layout.addWidget(self.config_path_edit)
        
        config_browse_btn = QPushButton('Browse...')
        config_browse_btn.clicked.connect(self.browse_config)
        config_layout.addWidget(config_browse_btn)
        layout.addLayout(config_layout)
        
        # Output directory
        output_layout = QHBoxLayout()
        output_label = QLabel('Output Directory:')
        output_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        output_layout.addWidget(output_label)
        self.output_dir_edit = QLineEdit()
        self.output_dir_edit.setPlaceholderText('(default: same as config file)')
        output_layout.addWidget(self.output_dir_edit)
        
        output_browse_btn = QPushButton('Browse...')
        output_browse_btn.clicked.connect(self.browse_output_dir)
        output_layout.addWidget(output_browse_btn)
        layout.addLayout(output_layout)
        
        # Generate button
        generate_btn = QPushButton('Generate SQL Files')
        generate_btn.clicked.connect(self.generate_sql)
        layout.addWidget(generate_btn)
        
        # Results
        results_label = QLabel('Results:')
        results_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        layout.addWidget(results_label)
        
        self.results_tree = QTreeWidget()
        self.results_tree.setHeaderLabels(['File'])
        self.results_tree.header().setSectionResizeMode(0, QHeaderView.Interactive)
        self.results_tree.setColumnWidth(0, 600)
        # Resize to fit content when populated
        self.results_tree.header().setStretchLastSection(True)
        layout.addWidget(self.results_tree)
        
        # Open folder button
        open_folder_btn = QPushButton('Open Output Folder')
        open_folder_btn.clicked.connect(self.open_output_folder)
        layout.addWidget(open_folder_btn)
    
    def browse_config(self):
        """Browse for config file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Select Configuration File',
            '',
            'CSV Files (*.csv);;All Files (*.*)'
        )
        
        if file_path:
            self.config_path_edit.setText(file_path)
    
    def browse_output_dir(self):
        """Browse for output directory"""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            'Select Output Directory'
        )
        
        if dir_path:
            self.output_dir_edit.setText(dir_path)
    
    def generate_sql(self):
        """Generate SQL files"""
        config_path = self.config_path_edit.text()
        if not config_path:
            QMessageBox.warning(self, 'Warning', 'Please select a configuration file.')
            return
        
        output_dir = self.output_dir_edit.text() or None
        
        # Show progress dialog
        progress = QProgressDialog('Generating SQL files...', 'Cancel', 0, 0, self)
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
        
        # Create worker thread (keep reference to prevent garbage collection)
        self.worker = SQLBuilderWorker(config_path, output_dir)
        self.worker.finished.connect(lambda result: self.on_generation_finished(result, progress))
        self.worker.finished.connect(self.cleanup_worker)  # Clean up when done
        self.worker.start()
    
    def cleanup_worker(self):
        """Clean up worker thread"""
        if self.worker:
            if self.worker.isRunning():
                self.worker.wait()  # Wait for thread to finish
            self.worker.deleteLater()  # Schedule for deletion
            self.worker = None
    
    def on_generation_finished(self, result, progress):
        """Handle generation completion"""
        progress.close()
        
        if result['success']:
            # Populate results tree
            self.results_tree.clear()
            
            for file_path in result['files']:
                item = QTreeWidgetItem(self.results_tree, [file_path])
            
            # Resize column to fit content
            self.results_tree.resizeColumnToContents(0)
            
            QMessageBox.information(
                self,
                'Success',
                f'Generated {len(result["files"])} SQL files in:\n{result["output_dir"]}'
            )
        else:
            QMessageBox.critical(self, 'Error', f'Failed to generate SQL files:\n{result.get("error", "Unknown error")}')
    
    def open_output_folder(self):
        """Open output folder in Windows Explorer"""
        from gui.utils.file_utils import open_file_location
        
        output_dir = self.output_dir_edit.text()
        if output_dir:
            open_file_location(output_dir)
        else:
            config_path = self.config_path_edit.text()
            if config_path:
                import os
                open_file_location(os.path.dirname(config_path))
