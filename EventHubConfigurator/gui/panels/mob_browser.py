"""Mob Browser Panel - Displays spawnable mobs with drag-and-drop support"""

import os
from PyQt5.QtWidgets import (
    QDockWidget, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem,
    QLineEdit, QPushButton, QLabel, QHeaderView, QDialog, QMessageBox,
    QApplication
)
from PyQt5.QtCore import Qt, pyqtSignal, QMimeData
from PyQt5.QtGui import QDrag, QClipboard

from core.mob_list_manager import load_mob_list, add_mob
from gui.utils.file_utils import get_data_path


class MobBrowserPanel(QDockWidget):
    """Dockable panel showing spawnable mobs"""
    
    mob_selected = pyqtSignal(int, str, int)  # wcid, name, max_spawns
    
    def __init__(self, parent=None):
        super().__init__('Mob Browser', parent)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        
        self.mobs = []
        # Get mob list path (uses bundled data file from app directory)
        self.mob_list_path = get_data_path('Spawnable Mobs List.csv')
        
        self.init_ui()
        # Auto-load mobs on initialization
        self.load_mobs()
    
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
            QPushButton:checked {
                background-color: #0066cc;
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
            QTreeWidget::item:hover {
                background-color: #404040;
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
        
        # Search box
        search_label = QLabel('Search:')
        search_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        layout.addWidget(search_label)
        
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText('Filter mobs by name or WCID...')
        self.search_box.textChanged.connect(self.filter_mobs)
        layout.addWidget(self.search_box)
        
        # Filter buttons
        filter_layout = QVBoxLayout()
        filter_label = QLabel('Difficulty:')
        filter_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        filter_layout.addWidget(filter_label)
        
        self.filter_low = QPushButton('Low')
        self.filter_low.setCheckable(True)
        self.filter_low.setChecked(True)
        self.filter_low.clicked.connect(self.filter_mobs)
        filter_layout.addWidget(self.filter_low)
        
        self.filter_mid = QPushButton('Mid')
        self.filter_mid.setCheckable(True)
        self.filter_mid.setChecked(True)
        self.filter_mid.clicked.connect(self.filter_mobs)
        filter_layout.addWidget(self.filter_mid)
        
        self.filter_high = QPushButton('High')
        self.filter_high.setCheckable(True)
        self.filter_high.setChecked(True)
        self.filter_high.clicked.connect(self.filter_mobs)
        filter_layout.addWidget(self.filter_high)
        
        self.filter_boss = QPushButton('Boss')
        self.filter_boss.setCheckable(True)
        self.filter_boss.setChecked(True)
        self.filter_boss.clicked.connect(self.filter_mobs)
        filter_layout.addWidget(self.filter_boss)
        
        layout.addLayout(filter_layout)
        
        # Mob tree
        self.mob_tree = MobTreeWidget()
        self.mob_tree.setHeaderLabels(['WCID', 'Name', 'Max Spawns'])
        self.mob_tree.setDragEnabled(True)
        self.mob_tree.setDragDropMode(QTreeWidget.DragOnly)
        self.mob_tree.itemDoubleClicked.connect(self.on_mob_double_clicked)
        self.mob_tree.setRootIsDecorated(True)
        layout.addWidget(self.mob_tree)
        
        # Toolbar buttons
        button_layout = QVBoxLayout()
        
        refresh_btn = QPushButton('Refresh')
        refresh_btn.clicked.connect(self.load_mobs)
        button_layout.addWidget(refresh_btn)
        
        edit_mobs_btn = QPushButton('Edit Mob List...')
        edit_mobs_btn.clicked.connect(self.edit_mob_list)
        button_layout.addWidget(edit_mobs_btn)
        
        add_mob_btn = QPushButton('Add New Mob...')
        add_mob_btn.clicked.connect(self.add_new_mob)
        button_layout.addWidget(add_mob_btn)
        
        layout.addLayout(button_layout)
    
    def load_mobs(self):
        """Load mobs from CSV file"""
        try:
            if not os.path.exists(self.mob_list_path):
                print(f"Warning: Mob list file not found at {self.mob_list_path}")
                print("  The file should be in EventHubConfigurator/data/Spawnable Mobs List.csv")
                return
            
            self.mobs = load_mob_list(self.mob_list_path)
            if self.mobs:
                self.populate_tree()
                print(f"Loaded {len(self.mobs)} mobs from {self.mob_list_path}")
            else:
                print(f"Warning: No mobs loaded from {self.mob_list_path}")
        except Exception as e:
            print(f"Error loading mobs: {e}")
            import traceback
            traceback.print_exc()
    
    def populate_tree(self):
        """Populate the tree widget with mobs"""
        self.mob_tree.clear()
        
        # Group by difficulty
        difficulty_groups = {
            'Low': {'regular': [], 'boss': []},
            'Mid': {'regular': [], 'boss': []},
            'High': {'regular': [], 'boss': []}
        }
        
        for mob in self.mobs:
            difficulty = mob.get('Difficulty', '')
            is_boss = mob.get('Boss', False)
            
            if difficulty in difficulty_groups:
                if is_boss:
                    difficulty_groups[difficulty]['boss'].append(mob)
                else:
                    difficulty_groups[difficulty]['regular'].append(mob)
        
        # Create tree structure
        for difficulty in ['Low', 'Mid', 'High']:
            diff_item = QTreeWidgetItem(self.mob_tree, [difficulty])
            diff_item.setExpanded(True)
            
            # Regular mobs
            regular_item = QTreeWidgetItem(diff_item, ['Regular Mobs'])
            regular_item.setExpanded(True)
            for mob in sorted(difficulty_groups[difficulty]['regular'], key=lambda x: x['Name']):
                mob_item = QTreeWidgetItem(regular_item, [
                    str(mob['ID']),
                    mob['Name'],
                    str(mob['Spawns Per Location'])
                ])
                mob_item.setData(0, Qt.UserRole, mob)
            
            # Boss mobs
            if difficulty_groups[difficulty]['boss']:
                boss_item = QTreeWidgetItem(diff_item, ['Boss Mobs'])
                boss_item.setExpanded(True)
                for mob in sorted(difficulty_groups[difficulty]['boss'], key=lambda x: x['Name']):
                    mob_item = QTreeWidgetItem(boss_item, [
                        str(mob['ID']),
                        mob['Name'],
                        str(mob['Spawns Per Location'])
                    ])
                    mob_item.setData(0, Qt.UserRole, mob)
        
        self.mob_tree.header().setSectionResizeMode(0, QHeaderView.Interactive)
        self.mob_tree.header().setSectionResizeMode(1, QHeaderView.Interactive)
        self.mob_tree.header().setSectionResizeMode(2, QHeaderView.Interactive)
        # Resize columns to fit content, then ensure minimum widths
        self.mob_tree.header().setStretchLastSection(False)
        for col in range(3):
            self.mob_tree.resizeColumnToContents(col)
        # Set minimum column widths to ensure all data is visible
        if self.mob_tree.columnWidth(0) < 120:
            self.mob_tree.setColumnWidth(0, 120)  # WCID
        if self.mob_tree.columnWidth(1) < 250:
            self.mob_tree.setColumnWidth(1, 250)  # Name (wider for long names)
        if self.mob_tree.columnWidth(2) < 150:
            self.mob_tree.setColumnWidth(2, 150)  # Spawns Per Location
    
    def filter_mobs(self):
        """Filter mobs based on search text and difficulty filters"""
        search_text = self.search_box.text().lower()
        show_low = self.filter_low.isChecked()
        show_mid = self.filter_mid.isChecked()
        show_high = self.filter_high.isChecked()
        show_boss = self.filter_boss.isChecked()
        
        for i in range(self.mob_tree.topLevelItemCount()):
            diff_item = self.mob_tree.topLevelItem(i)
            difficulty = diff_item.text(0)
            
            # Check if difficulty is filtered
            if difficulty == 'Low' and not show_low:
                diff_item.setHidden(True)
                continue
            elif difficulty == 'Mid' and not show_mid:
                diff_item.setHidden(True)
                continue
            elif difficulty == 'High' and not show_high:
                diff_item.setHidden(True)
                continue
            
            diff_item.setHidden(False)
            
            # Filter children
            for j in range(diff_item.childCount()):
                category_item = diff_item.child(j)
                is_boss_category = 'Boss' in category_item.text(0)
                
                if is_boss_category and not show_boss:
                    category_item.setHidden(True)
                    continue
                
                category_item.setHidden(False)
                
                # Filter mobs by search text
                for k in range(category_item.childCount()):
                    mob_item = category_item.child(k)
                    mob = mob_item.data(0, Qt.UserRole)
                    
                    if mob:
                        name = mob.get('Name', '').lower()
                        wcid = str(mob.get('ID', ''))
                        
                        matches_search = (not search_text or 
                                        search_text in name or 
                                        search_text in wcid)
                        
                        mob_item.setHidden(not matches_search)
    
    def on_mob_double_clicked(self, item, column):
        """Handle double-click on mob item"""
        mob = item.data(0, Qt.UserRole)
        if not mob:
            return
        
        # If double-clicked on WCID column (column 0), copy to clipboard
        if column == 0:
            wcid = str(mob['ID'])
            clipboard = QApplication.clipboard()
            clipboard.setText(wcid)
            # Show feedback in status bar if parent window has one
            parent = self.parent()
            while parent and not hasattr(parent, 'statusBar'):
                parent = parent.parent()
            if parent and hasattr(parent, 'statusBar'):
                parent.statusBar().showMessage(f'WCID {wcid} copied to clipboard', 2000)
            return
        
        # Otherwise, emit mob_selected signal (for other uses)
        self.mob_selected.emit(
            mob['ID'],
            mob['Name'],
            mob['Spawns Per Location']
        )
    
    def edit_mob_list(self):
        """Open mob list manager dialog"""
        from gui.panels.mob_list_manager import MobListManagerDialog
        dialog = MobListManagerDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.load_mobs()
    
    def add_new_mob(self):
        """Open add new mob dialog"""
        from gui.panels.mob_list_manager import AddEditMobDialog
        
        dialog = AddEditMobDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            mob_data = dialog.get_mob_data()
            try:
                add_mob(mob_data, self.mob_list_path)
                self.load_mobs()
                QMessageBox.information(self, 'Success', 'Mob added successfully.')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to add mob: {e}')


class MobTreeWidget(QTreeWidget):
    """Custom tree widget with drag support"""
    
    def startDrag(self, supportedActions):
        """Start drag operation"""
        item = self.currentItem()
        if not item:
            return
        
        mob = item.data(0, Qt.UserRole)
        if not mob:
            return
        
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(f"{mob['ID']}|{mob['Name']}|{mob['Spawns Per Location']}")
        drag.setMimeData(mime_data)
        drag.exec_(Qt.CopyAction)
