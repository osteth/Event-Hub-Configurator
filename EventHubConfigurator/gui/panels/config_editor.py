"""Config Editor Panel - Main editing area for event configuration"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem,
    QPushButton, QLabel, QHeaderView, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QDropEvent, QDragEnterEvent, QDragMoveEvent

from gui.utils.config_manager import load_config, save_config
from core.mob_list_manager import load_mob_list
from gui.utils.file_utils import get_data_path


class ConfigTreeWidget(QTreeWidget):
    """Custom tree widget with drop support for mobs"""
    
    mob_dropped = pyqtSignal(object, int, str, int)  # item, wcid, name, max_spawns
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter event"""
        if event.mimeData().hasText():
            event.acceptProposedAction()
    
    def dragMoveEvent(self, event: QDragMoveEvent):
        """Handle drag move event"""
        if event.mimeData().hasText():
            event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        """Handle drop event"""
        item = self.itemAt(event.pos())
        if not item:
            return
        
        # Check if dropped on a position item (has UserRole data with 3 elements)
        mob_data = item.data(0, Qt.UserRole)
        if not mob_data or not isinstance(mob_data, tuple) or len(mob_data) != 3:
            return
        
        # Parse dropped data
        mime_data = event.mimeData().text()
        parts = mime_data.split('|')
        if len(parts) != 3:
            return
        
        try:
            wcid = int(parts[0])
            name = parts[1]
            max_spawns = int(parts[2])
            
            # Emit signal to parent to handle the update
            self.mob_dropped.emit(item, wcid, name, max_spawns)
            event.acceptProposedAction()
        except (ValueError, IndexError):
            pass


class ConfigEditorPanel(QWidget):
    """Main configuration editor panel"""
    
    config_modified = pyqtSignal()
    config_loaded = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config_path = None
        self.config_data = {}  # {tier: {wave_num: {position: (wcid, spawn_count)}}}
        self.modified = False
        self.mob_name_lookup = {}  # {wcid: name} for quick name lookup
        
        self.init_ui()
        self.load_mob_names()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
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
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)
        
        # Title
        title = QLabel('Event Configuration Editor')
        title.setStyleSheet('font-size: 14pt; font-weight: bold; color: #e0e0e0; background-color: transparent;')
        layout.addWidget(title)
        
        # Tree widget for tier/wave/position hierarchy
        self.tree = ConfigTreeWidget()
        self.tree.setHeaderLabels(['Tier', 'WCID', 'Mob Name', 'Spawn Count'])
        self.tree.setDragDropMode(QTreeWidget.DropOnly)
        self.tree.setAcceptDrops(True)
        self.tree.setDropIndicatorShown(True)
        self.tree.setDefaultDropAction(Qt.CopyAction)
        # Make spawn count column editable (column 3)
        self.tree.setColumnCount(4)
        self.tree.itemChanged.connect(self.on_item_changed)
        self.tree.mob_dropped.connect(self.on_mob_dropped)
        layout.addWidget(self.tree)
        
        # Toolbar
        toolbar_layout = QVBoxLayout()
        
        clear_btn = QPushButton('Clear All')
        clear_btn.clicked.connect(self.clear_all)
        toolbar_layout.addWidget(clear_btn)
        
        layout.addLayout(toolbar_layout)
        
        # Populate initial structure
        self.populate_structure()
    
    def populate_structure(self):
        """Populate the tree with tier/wave/position structure"""
        self.tree.clear()
        
        for tier in ['low', 'mid', 'high']:
            tier_item = QTreeWidgetItem(self.tree, [tier.capitalize()])
            tier_item.setExpanded(True)
            
            # Regular waves 1-10
            for wave_num in range(1, 11):
                wave_item = QTreeWidgetItem(tier_item, [f'Wave {wave_num}'])
                wave_item.setExpanded(True)
                
                for pos in range(4):
                    pos_item = QTreeWidgetItem(wave_item, [f'Position {pos}'])
                    pos_item.setData(0, Qt.UserRole, (tier, str(wave_num), pos))
                    self.set_position_empty(pos_item)
            
            # Boss wave
            boss_item = QTreeWidgetItem(tier_item, ['Boss Wave'])
            boss_item.setExpanded(True)
            
            for pos in range(4):
                pos_item = QTreeWidgetItem(boss_item, [f'Position {pos}'])
                pos_item.setData(0, Qt.UserRole, (tier, 'boss', pos))
                self.set_position_empty(pos_item)
        
        # Set column resize modes
        self.tree.header().setSectionResizeMode(0, QHeaderView.Interactive)  # Tier
        self.tree.header().setSectionResizeMode(1, QHeaderView.Interactive)  # WCID
        self.tree.header().setSectionResizeMode(2, QHeaderView.Interactive)  # Mob Name
        self.tree.header().setSectionResizeMode(3, QHeaderView.Interactive)  # Spawn Count
        # Set initial column widths to ensure all data is visible
        self.tree.setColumnWidth(0, 100)   # Tier
        self.tree.setColumnWidth(1, 120)   # WCID
        self.tree.setColumnWidth(2, 300)   # Mob Name (wider for long names)
        self.tree.setColumnWidth(3, 120)   # Spawn Count
        # Resize columns to fit content after initial setup
        self.tree.header().setStretchLastSection(False)
        # Resize columns to ensure all data is visible
        self.resize_columns_to_content()
    
    def load_mob_names(self):
        """Load mob names from CSV for lookup"""
        try:
            mob_list_path = get_data_path('Spawnable Mobs List.csv')
            mobs = load_mob_list(mob_list_path)
            self.mob_name_lookup = {mob['ID']: mob['Name'] for mob in mobs}
        except Exception as e:
            print(f"Warning: Could not load mob names: {e}")
            self.mob_name_lookup = {}
    
    def get_mob_name(self, wcid: int) -> str:
        """Get mob name by WCID"""
        return self.mob_name_lookup.get(wcid, f'WCID {wcid}')
    
    def set_position_empty(self, pos_item):
        """Set a position item to empty state"""
        pos_item.setText(1, '')
        pos_item.setText(2, 'Empty')
        pos_item.setText(3, '0')
        pos_item.setFlags(pos_item.flags() & ~Qt.ItemIsEditable)  # Not editable when empty
        pos_item.setData(1, Qt.UserRole, None)
    
    def load_config_file(self, file_path: str):
        """Load configuration from CSV file"""
        try:
            config = load_config(file_path)
            self.config_data = config
            self.config_path = file_path
            self.modified = False
            
            # Update tree with loaded data
            self.update_tree_from_config()
            
            self.config_loaded.emit(file_path)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load config: {e}')
    
    def update_tree_from_config(self):
        """Update tree widget from config data"""
        for i in range(self.tree.topLevelItemCount()):
            tier_item = self.tree.topLevelItem(i)
            tier = tier_item.text(0).lower()
            
            if tier not in self.config_data:
                continue
            
            for j in range(tier_item.childCount()):
                wave_item = tier_item.child(j)
                wave_text = wave_item.text(0)
                
                if wave_text == 'Boss Wave':
                    wave_num = 'boss'
                else:
                    wave_num = wave_text.split()[1]
                
                if wave_num not in self.config_data[tier]:
                    continue
                
                # Update positions
                for k in range(wave_item.childCount()):
                    pos_item = wave_item.child(k)
                    tier_key, wave_key, pos_idx = pos_item.data(0, Qt.UserRole)
                    
                    # Find matching assignment
                    assignment = None
                    for pos_idx_config, wcid, spawn_count in self.config_data[tier][wave_num]:
                        if pos_idx_config == pos_idx:
                            assignment = (wcid, spawn_count)
                            break
                    
                    if assignment:
                        wcid, spawn_count = assignment
                        mob_name = self.get_mob_name(wcid)
                        # Get max spawns from mob list
                        max_spawns = 1  # Default
                        from core.mob_list_manager import load_mob_list
                        mobs = load_mob_list(get_data_path('Spawnable Mobs List.csv'))
                        for mob in mobs:
                            if mob['ID'] == wcid:
                                max_spawns = mob.get('Spawns Per Location', 1)
                                break
                        
                        pos_item.setText(1, str(wcid))
                        pos_item.setText(2, mob_name)
                        pos_item.setText(3, str(spawn_count))
                        pos_item.setFlags(pos_item.flags() | Qt.ItemIsEditable)  # Make editable
                        pos_item.setData(1, Qt.UserRole, (wcid, spawn_count, max_spawns))
                    else:
                        self.set_position_empty(pos_item)
        
        # Resize columns after loading data
        self.resize_columns_to_content()
    
    def resize_columns_to_content(self):
        """Resize columns to fit their content"""
        # Resize all columns to content, but ensure minimum widths
        for col in range(4):
            self.tree.resizeColumnToContents(col)
            # Ensure minimum widths
            current_width = self.tree.columnWidth(col)
            min_widths = [100, 120, 250, 100]  # Min widths for each column: Tier, WCID, Mob Name, Spawn Count
            if current_width < min_widths[col]:
                self.tree.setColumnWidth(col, min_widths[col])
    
    def save_config_file(self, file_path: str = None):
        """Save configuration to CSV file"""
        if file_path is None:
            file_path = self.config_path
        
        if not file_path:
            return False
        
        try:
            # Build config dict from tree
            config = {}
            
            for i in range(self.tree.topLevelItemCount()):
                tier_item = self.tree.topLevelItem(i)
                tier = tier_item.text(0).lower()
                config[tier] = {}
                
                for j in range(tier_item.childCount()):
                    wave_item = tier_item.child(j)
                    wave_text = wave_item.text(0)
                    
                    if wave_text == 'Boss Wave':
                        wave_num = 'boss'
                    else:
                        wave_num = wave_text.split()[1]
                    
                    config[tier][wave_num] = []
                    
                    for k in range(wave_item.childCount()):
                        pos_item = wave_item.child(k)
                        tier_key, wave_key, pos_idx = pos_item.data(0, Qt.UserRole)
                        
                        mob_data = pos_item.data(1, Qt.UserRole)
                        if mob_data:
                            # Handle both old format (wcid, spawn_count) and new format (wcid, spawn_count, max_spawns)
                            if len(mob_data) == 2:
                                wcid, spawn_count = mob_data
                            else:
                                wcid, spawn_count, _ = mob_data
                            config[tier][wave_num].append((pos_idx, wcid, spawn_count))
            
            save_config(config, file_path)
            self.config_path = file_path
            self.modified = False
            return True
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save config: {e}')
            return False
    
    def on_mob_dropped(self, item, wcid, name, max_spawns):
        """Handle mob dropped on position item"""
        # Update position item with max spawns as default
        mob_name = self.get_mob_name(wcid)  # Get actual mob name
        item.setText(1, str(wcid))
        item.setText(2, mob_name)
        item.setText(3, str(max_spawns))  # Default to max spawns
        item.setFlags(item.flags() | Qt.ItemIsEditable)  # Make spawn count editable
        item.setData(1, Qt.UserRole, (wcid, max_spawns, max_spawns))  # Store (wcid, spawn_count, max_spawns)
        
        self.modified = True
        self.config_modified.emit()
    
    def on_item_changed(self, item, column):
        """Handle item change (e.g., spawn count edit)"""
        if column == 3:  # Spawn count column
            try:
                spawn_count = int(item.text(3))
                mob_data = item.data(1, Qt.UserRole)
                if mob_data:
                    # Handle both old format (wcid, spawn_count) and new format (wcid, spawn_count, max_spawns)
                    if len(mob_data) == 2:
                        wcid, _ = mob_data
                        max_spawns = 1  # Default if not stored
                    else:
                        wcid, _, max_spawns = mob_data
                    
                    # Validate spawn count doesn't exceed max
                    if spawn_count < 1:
                        spawn_count = 1
                        item.setText(3, '1')
                        QMessageBox.warning(self, 'Invalid Value', 'Spawn count must be at least 1.')
                    elif spawn_count > max_spawns:
                        spawn_count = max_spawns
                        item.setText(3, str(max_spawns))
                        QMessageBox.warning(self, 'Invalid Value', f'Spawn count cannot exceed maximum spawns ({max_spawns}) for this mob.')
                    
                    # Update with validated value
                    item.setData(1, Qt.UserRole, (wcid, spawn_count, max_spawns))
                    self.modified = True
                    self.config_modified.emit()
            except ValueError:
                # Invalid input, revert to previous value
                mob_data = item.data(1, Qt.UserRole)
                if mob_data:
                    if len(mob_data) == 2:
                        _, spawn_count = mob_data
                    else:
                        _, spawn_count, _ = mob_data
                    item.setText(3, str(spawn_count))
                    QMessageBox.warning(self, 'Invalid Input', 'Spawn count must be a number.')
    
    def clear_all(self):
        """Clear all position assignments"""
        reply = QMessageBox.question(
            self,
            'Clear All',
            'Clear all position assignments?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            for i in range(self.tree.topLevelItemCount()):
                tier_item = self.tree.topLevelItem(i)
                for j in range(tier_item.childCount()):
                    wave_item = tier_item.child(j)
                    for k in range(wave_item.childCount()):
                        pos_item = wave_item.child(k)
                        self.set_position_empty(pos_item)
            
            self.modified = True
            self.config_modified.emit()
    
    def fill_random(self):
        """Fill empty positions with random mobs"""
        import random
        from core.mob_list_manager import load_mob_list
        
        # Load mob list
        mob_list_path = get_data_path('Spawnable Mobs List.csv')
        mobs = load_mob_list(mob_list_path)
        
        if not mobs:
            QMessageBox.warning(self, 'Warning', 'No mobs available in the mob list.')
            return
        
        # Group mobs by difficulty
        mobs_by_tier = {
            'low': [],
            'mid': [],
            'high': []
        }
        
        for mob in mobs:
            difficulty = mob.get('Difficulty', '').lower()
            if difficulty in mobs_by_tier:
                mobs_by_tier[difficulty].append(mob)
        
        # Fill empty positions
        filled_count = 0
        for i in range(self.tree.topLevelItemCount()):
            tier_item = self.tree.topLevelItem(i)
            tier = tier_item.text(0).lower()
            
            if tier not in mobs_by_tier or not mobs_by_tier[tier]:
                continue
            
            for j in range(tier_item.childCount()):
                wave_item = tier_item.child(j)
                for k in range(wave_item.childCount()):
                    pos_item = wave_item.child(k)
                    
                    # Check if position is empty
                    mob_data = pos_item.data(1, Qt.UserRole)
                    if mob_data is None:
                        # Position is empty, fill with random mob
                        random_mob = random.choice(mobs_by_tier[tier])
                        wcid = random_mob['ID']
                        max_spawns = random_mob.get('Spawns Per Location', 1)
                        mob_name = self.get_mob_name(wcid)
                        
                        pos_item.setText(1, str(wcid))
                        pos_item.setText(2, mob_name)
                        pos_item.setText(3, str(max_spawns))
                        pos_item.setFlags(pos_item.flags() | Qt.ItemIsEditable)
                        pos_item.setData(1, Qt.UserRole, (wcid, max_spawns, max_spawns))
                        filled_count += 1
        
        if filled_count > 0:
            self.modified = True
            self.config_modified.emit()
            QMessageBox.information(self, 'Success', f'Filled {filled_count} empty positions with random mobs.')
        else:
            QMessageBox.information(self, 'Info', 'No empty positions to fill.')
