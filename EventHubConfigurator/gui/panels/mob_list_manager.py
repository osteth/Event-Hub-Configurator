"""Mob List Manager Dialog - Add, edit, delete mobs"""

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QCheckBox,
    QMessageBox, QFileDialog, QHeaderView, QDialogButtonBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt

from core.mob_list_manager import (
    load_mob_list, save_mob_list, add_mob, update_mob, delete_mob
)
from gui.utils.file_utils import get_data_path


class AddEditMobDialog(QDialog):
    """Dialog for adding/editing a mob"""
    
    def __init__(self, parent=None, mob_data=None):
        super().__init__(parent)
        self.mob_data = mob_data
        self.init_ui()
        
        if mob_data:
            self.load_mob_data()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle('Add Mob' if not self.mob_data else 'Edit Mob')
        self.setStyleSheet("""
            QDialog {
                background-color: #2b2b2b;
                color: #e0e0e0;
            }
            QLineEdit {
                background-color: #353535;
                color: #e0e0e0;
                border: 1px solid #555555;
                padding: 3px;
            }
            QComboBox {
                background-color: #353535;
                color: #e0e0e0;
                border: 1px solid #555555;
                padding: 3px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #353535;
                color: #e0e0e0;
                selection-background-color: #505050;
            }
            QSpinBox {
                background-color: #353535;
                color: #e0e0e0;
                border: 1px solid #555555;
                padding: 3px;
            }
            QCheckBox {
                color: #e0e0e0;
            }
            QCheckBox::indicator {
                background-color: #353535;
                border: 1px solid #555555;
            }
            QCheckBox::indicator:checked {
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
            QPushButton:pressed {
                background-color: #606060;
            }
            QLabel {
                background-color: transparent;
                color: #e0e0e0;
                font-weight: bold;
            }
            QDialogButtonBox QPushButton {
                min-width: 80px;
            }
        """)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # WCID
        wcid_layout = QHBoxLayout()
        wcid_label = QLabel('WCID:')
        wcid_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        wcid_layout.addWidget(wcid_label)
        self.wcid_input = QSpinBox()
        self.wcid_input.setMinimum(1)
        self.wcid_input.setMaximum(999999999)
        self.wcid_input.setEnabled(not self.mob_data)  # Disable if editing
        wcid_layout.addWidget(self.wcid_input)
        layout.addLayout(wcid_layout)
        
        # Name
        name_layout = QHBoxLayout()
        name_label = QLabel('Name:')
        name_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        name_layout.addWidget(name_label)
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)
        
        # Difficulty
        diff_layout = QHBoxLayout()
        diff_label = QLabel('Difficulty:')
        diff_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        diff_layout.addWidget(diff_label)
        self.diff_combo = QComboBox()
        self.diff_combo.addItems(['Low', 'Mid', 'High'])
        diff_layout.addWidget(self.diff_combo)
        layout.addLayout(diff_layout)
        
        # Boss
        self.boss_check = QCheckBox('Boss')
        layout.addWidget(self.boss_check)
        
        # Spawns Per Location
        spawns_layout = QHBoxLayout()
        spawns_label = QLabel('Spawns Per Location:')
        spawns_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        spawns_layout.addWidget(spawns_label)
        self.spawns_input = QSpinBox()
        self.spawns_input.setMinimum(1)
        self.spawns_input.setMaximum(100)
        self.spawns_input.setValue(1)
        spawns_layout.addWidget(self.spawns_input)
        layout.addLayout(spawns_layout)
        
        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
    
    def load_mob_data(self):
        """Load mob data into form"""
        if self.mob_data:
            self.wcid_input.setValue(self.mob_data['ID'])
            self.name_input.setText(self.mob_data['Name'])
            self.diff_combo.setCurrentText(self.mob_data['Difficulty'])
            self.boss_check.setChecked(self.mob_data['Boss'])
            self.spawns_input.setValue(self.mob_data['Spawns Per Location'])
    
    def get_mob_data(self):
        """Get mob data from form"""
        return {
            'ID': self.wcid_input.value(),
            'Name': self.name_input.text().strip(),
            'Difficulty': self.diff_combo.currentText(),
            'Boss': self.boss_check.isChecked(),
            'Spawns Per Location': self.spawns_input.value()
        }
    
    def accept(self):
        """Validate and accept"""
        if not self.name_input.text().strip():
            QMessageBox.warning(self, 'Validation', 'Name is required.')
            return
        
        super().accept()


class MobListManagerDialog(QDialog):
    """Dialog for managing the mob list"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mob_list_path = get_data_path('Spawnable Mobs List.csv')
        self.mobs = []
        
        self.init_ui()
        self.load_mobs()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle('Manage Mob List')
        self.setMinimumSize(800, 600)
        self.setStyleSheet("""
            QDialog {
                background-color: #2b2b2b;
                color: #e0e0e0;
            }
            QTableWidget {
                background-color: #353535;
                color: #e0e0e0;
                border: 1px solid #555555;
                alternate-background-color: #3c3c3c;
                gridline-color: #555555;
            }
            QTableWidget::item:selected {
                background-color: #505050;
                color: #ffffff;
            }
            QHeaderView::section {
                background-color: #404040;
                color: #e0e0e0;
                padding: 4px;
                border: 1px solid #555555;
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
        """)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['WCID', 'Name', 'Difficulty', 'Boss', 'Spawns Per Location'])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.doubleClicked.connect(self.edit_mob)
        # Make all columns resizable
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # Set initial column widths to ensure all data is visible
        self.table.setColumnWidth(0, 120)  # WCID
        self.table.setColumnWidth(1, 300)  # Name (wider for long names)
        self.table.setColumnWidth(2, 120)  # Difficulty
        self.table.setColumnWidth(3, 100)  # Boss
        self.table.setColumnWidth(4, 150)  # Spawns Per Location
        layout.addWidget(self.table)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        add_btn = QPushButton('Add Mob...')
        add_btn.clicked.connect(self.add_mob)
        button_layout.addWidget(add_btn)
        
        edit_btn = QPushButton('Edit Mob...')
        edit_btn.clicked.connect(self.edit_mob)
        button_layout.addWidget(edit_btn)
        
        delete_btn = QPushButton('Delete Mob')
        delete_btn.clicked.connect(self.delete_mob)
        button_layout.addWidget(delete_btn)
        
        button_layout.addStretch()
        
        import_btn = QPushButton('Import CSV...')
        import_btn.clicked.connect(self.import_csv)
        button_layout.addWidget(import_btn)
        
        export_btn = QPushButton('Export CSV...')
        export_btn.clicked.connect(self.export_csv)
        button_layout.addWidget(export_btn)
        
        layout.addLayout(button_layout)
        
        # Dialog buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.button(QDialogButtonBox.Save).clicked.connect(self.save_mobs)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
    
    def load_mobs(self):
        """Load mobs from CSV"""
        try:
            self.mobs = load_mob_list(self.mob_list_path)
            if not self.mobs:
                QMessageBox.warning(self, 'Warning', 'No valid mobs found in the CSV file. Check that IDs are valid numbers.')
            self.populate_table()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load mob list: {e}')
    
    def populate_table(self):
        """Populate table with mobs"""
        self.table.setRowCount(len(self.mobs))
        
        for i, mob in enumerate(self.mobs):
            self.table.setItem(i, 0, QTableWidgetItem(str(mob['ID'])))
            self.table.setItem(i, 1, QTableWidgetItem(mob['Name']))
            self.table.setItem(i, 2, QTableWidgetItem(mob['Difficulty']))
            self.table.setItem(i, 3, QTableWidgetItem('Yes' if mob['Boss'] else 'No'))
            self.table.setItem(i, 4, QTableWidgetItem(str(mob['Spawns Per Location'])))
        
        # Resize columns to fit content, ensuring minimum widths
        for col in range(5):
            self.table.resizeColumnToContents(col)
        # Ensure minimum widths
        if self.table.columnWidth(0) < 120:
            self.table.setColumnWidth(0, 120)
        if self.table.columnWidth(1) < 250:
            self.table.setColumnWidth(1, 250)
        if self.table.columnWidth(2) < 120:
            self.table.setColumnWidth(2, 120)
        if self.table.columnWidth(3) < 100:
            self.table.setColumnWidth(3, 100)
        if self.table.columnWidth(4) < 150:
            self.table.setColumnWidth(4, 150)
    
    def add_mob(self):
        """Add a new mob"""
        dialog = AddEditMobDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            mob_data = dialog.get_mob_data()
            
            # Check for duplicate WCID
            if any(m['ID'] == mob_data['ID'] for m in self.mobs):
                QMessageBox.warning(self, 'Error', f'Mob with WCID {mob_data["ID"]} already exists.')
                return
            
            self.mobs.append(mob_data)
            self.populate_table()
    
    def edit_mob(self):
        """Edit selected mob"""
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, 'Warning', 'Please select a mob to edit.')
            return
        
        mob_data = self.mobs[row].copy()
        dialog = AddEditMobDialog(self, mob_data)
        if dialog.exec_() == QDialog.Accepted:
            new_data = dialog.get_mob_data()
            
            # Check for duplicate WCID (if changed)
            if new_data['ID'] != mob_data['ID']:
                if any(m['ID'] == new_data['ID'] for m in self.mobs):
                    QMessageBox.warning(self, 'Error', f'Mob with WCID {new_data["ID"]} already exists.')
                    return
            
            self.mobs[row] = new_data
            self.populate_table()
    
    def delete_mob(self):
        """Delete selected mob"""
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, 'Warning', 'Please select a mob to delete.')
            return
        
        mob = self.mobs[row]
        reply = QMessageBox.question(
            self,
            'Confirm Delete',
            f'Delete mob "{mob["Name"]}" (WCID {mob["ID"]})?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.mobs.pop(row)
            self.populate_table()
    
    def import_csv(self):
        """Import mobs from CSV file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Import Mob List',
            '',
            'CSV Files (*.csv);;All Files (*.*)'
        )
        
        if file_path:
            try:
                imported_mobs = load_mob_list(file_path)
                reply = QMessageBox.question(
                    self,
                    'Import Options',
                    f'Found {len(imported_mobs)} mobs. Merge with existing or replace?',
                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                    QMessageBox.Yes
                )
                
                if reply == QMessageBox.Yes:  # Merge
                    # Add new mobs, update existing
                    for imported in imported_mobs:
                        existing = next((m for m in self.mobs if m['ID'] == imported['ID']), None)
                        if existing:
                            existing.update(imported)
                        else:
                            self.mobs.append(imported)
                elif reply == QMessageBox.No:  # Replace
                    self.mobs = imported_mobs
                
                self.populate_table()
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to import CSV: {e}')
    
    def export_csv(self):
        """Export mobs to CSV file"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            'Export Mob List',
            '',
            'CSV Files (*.csv);;All Files (*.*)'
        )
        
        if file_path:
            try:
                save_mob_list(self.mobs, file_path)
                QMessageBox.information(self, 'Success', f'Mob list exported to:\n{file_path}')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to export CSV: {e}')
    
    def save_mobs(self):
        """Save mobs to CSV file"""
        try:
            save_mob_list(self.mobs, self.mob_list_path)
            QMessageBox.information(self, 'Success', 'Mob list saved successfully.')
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save mob list: {e}')
