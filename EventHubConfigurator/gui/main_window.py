"""Main application window for Event Hub Configurator"""

import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import (
    QMainWindow, QMenuBar, QToolBar, QStatusBar, QDockWidget,
    QAction, QMessageBox, QFileDialog, QApplication, QDialog
)
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtGui import QIcon, QKeySequence

from gui.panels.config_editor import ConfigEditorPanel
from gui.panels.mob_browser import MobBrowserPanel
from gui.panels.generator_tool import GeneratorToolPanel
from gui.panels.sql_builder import SQLBuilderPanel
from gui.panels.bulk_upload_tool import BulkUploadToolPanel
from gui.panels.validator_panel import ValidatorPanel
from gui.panels.mob_list_manager import MobListManagerDialog


class MainWindow(QMainWindow):
    """Main application window with dockable panels"""
    
    def __init__(self):
        super().__init__()
        self.settings = QSettings('EventHubConfigurator', 'EventHubConfigurator')
        self.current_config_path = None
        self.config_modified = False
        
        self.init_ui()
        self.load_settings()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle('Event Hub Configurator')
        self.setGeometry(100, 100, 1400, 900)
        
        # Set main window dark theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
                color: #e0e0e0;
            }
            QMenuBar {
                background-color: #3c3c3c;
                color: #e0e0e0;
            }
            QMenuBar::item {
                background-color: transparent;
                color: #e0e0e0;
            }
            QMenuBar::item:selected {
                background-color: #505050;
            }
            QMenu {
                background-color: #3c3c3c;
                color: #e0e0e0;
                border: 1px solid #555555;
            }
            QMenu::item:selected {
                background-color: #505050;
            }
            QToolBar {
                background-color: #3c3c3c;
                border: none;
            }
            QStatusBar {
                background-color: #3c3c3c;
                color: #e0e0e0;
            }
        """)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create status bar
        self.create_status_bar()
        
        # Create dockable panels
        self.create_dockable_panels()
        
        # Set central widget (Config Editor)
        self.set_central_widget()
    
    def create_menu_bar(self):
        """Create the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('&File')
        
        new_action = QAction('&New Config', self)
        new_action.setShortcut(QKeySequence.New)
        new_action.setStatusTip('Create a new event configuration')
        new_action.triggered.connect(self.new_config)
        file_menu.addAction(new_action)
        
        open_action = QAction('&Open Config...', self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.setStatusTip('Open an existing event configuration')
        open_action.triggered.connect(self.open_config)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        save_action = QAction('&Save Config', self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.setStatusTip('Save the current configuration')
        save_action.triggered.connect(self.save_config)
        file_menu.addAction(save_action)
        
        save_as_action = QAction('Save Config &As...', self)
        save_as_action.setShortcut(QKeySequence.SaveAs)
        save_as_action.setStatusTip('Save the current configuration with a new name')
        save_as_action.triggered.connect(self.save_config_as)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        recent_menu = file_menu.addMenu('Recent Files')
        # TODO: Populate recent files
        
        file_menu.addSeparator()
        
        exit_action = QAction('E&xit', self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.setStatusTip('Exit the application')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu('&Edit')
        
        undo_action = QAction('&Undo', self)
        undo_action.setShortcut(QKeySequence.Undo)
        undo_action.setStatusTip('Undo last action')
        # undo_action.triggered.connect(self.undo)
        edit_menu.addAction(undo_action)
        
        redo_action = QAction('&Redo', self)
        redo_action.setShortcut(QKeySequence.Redo)
        redo_action.setStatusTip('Redo last undone action')
        # redo_action.triggered.connect(self.redo)
        edit_menu.addAction(redo_action)
        
        edit_menu.addSeparator()
        
        clear_action = QAction('&Clear All', self)
        clear_action.setStatusTip('Clear all positions in current config')
        clear_action.triggered.connect(self.clear_all)
        edit_menu.addAction(clear_action)
        
        fill_random_action = QAction('Fill &Random', self)
        fill_random_action.setStatusTip('Fill empty positions with random mobs')
        fill_random_action.triggered.connect(self.fill_random)
        edit_menu.addAction(fill_random_action)
        
        edit_menu.addSeparator()
        
        prefs_action = QAction('&Preferences...', self)
        prefs_action.setStatusTip('Open preferences dialog')
        # prefs_action.triggered.connect(self.show_preferences)
        edit_menu.addAction(prefs_action)
        
        # Generate menu
        generate_menu = menubar.addMenu('&Generate')
        
        random_event_action = QAction('&Random Event...', self)
        random_event_action.setStatusTip('Generate a random event configuration')
        random_event_action.triggered.connect(self.show_generator_tool)
        generate_menu.addAction(random_event_action)
        
        sql_files_action = QAction('&SQL Files...', self)
        sql_files_action.setStatusTip('Generate SQL files from current config')
        sql_files_action.triggered.connect(self.show_sql_builder)
        generate_menu.addAction(sql_files_action)
        
        bulk_upload_action = QAction('&Bulk Upload...', self)
        bulk_upload_action.setStatusTip('Create bulk upload SQL file')
        bulk_upload_action.triggered.connect(self.show_bulk_upload_tool)
        generate_menu.addAction(bulk_upload_action)
        
        # Tools menu
        tools_menu = menubar.addMenu('&Tools')
        
        validate_action = QAction('&Validate SQL...', self)
        validate_action.setStatusTip('Validate a SQL file')
        validate_action.triggered.connect(self.show_validator)
        tools_menu.addAction(validate_action)
        
        tools_menu.addSeparator()
        
        manage_mobs_action = QAction('&Manage Mob List...', self)
        manage_mobs_action.setStatusTip('Add, edit, or delete mobs from the spawnable mobs list')
        manage_mobs_action.triggered.connect(self.show_mob_list_manager)
        tools_menu.addAction(manage_mobs_action)
        
        # View menu
        view_menu = menubar.addMenu('&View')
        
        # Panel visibility toggles
        mob_browser_action = QAction('&Mob Browser', self, checkable=True, checked=True)
        mob_browser_action.triggered.connect(self.toggle_mob_browser)
        view_menu.addAction(mob_browser_action)
        
        generator_action = QAction('&Generator Tool', self, checkable=True, checked=False)
        generator_action.triggered.connect(self.toggle_generator_tool)
        view_menu.addAction(generator_action)
        
        sql_builder_action = QAction('&SQL Builder', self, checkable=True, checked=False)
        sql_builder_action.triggered.connect(self.toggle_sql_builder)
        view_menu.addAction(sql_builder_action)
        
        bulk_upload_action = QAction('&Bulk Upload Tool', self, checkable=True, checked=False)
        bulk_upload_action.triggered.connect(self.toggle_bulk_upload_tool)
        view_menu.addAction(bulk_upload_action)
        
        validator_action = QAction('&Validator', self, checkable=True, checked=False)
        validator_action.triggered.connect(self.toggle_validator)
        view_menu.addAction(validator_action)
        
        view_menu.addSeparator()
        
        reset_layout_action = QAction('&Reset Layout', self)
        reset_layout_action.setStatusTip('Reset window layout to default')
        reset_layout_action.triggered.connect(self.reset_layout)
        view_menu.addAction(reset_layout_action)
        
        # Help menu
        help_menu = menubar.addMenu('&Help')
        
        about_action = QAction('&About...', self)
        about_action.setStatusTip('Show application information')
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        docs_action = QAction('&Documentation...', self)
        docs_action.setStatusTip('Open documentation')
        # docs_action.triggered.connect(self.show_documentation)
        help_menu.addAction(docs_action)
    
    def create_toolbar(self):
        """Create the toolbar"""
        toolbar = QToolBar('Main Toolbar', self)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # Add common actions to toolbar
        new_action = QAction('New', self)
        new_action.triggered.connect(self.new_config)
        toolbar.addAction(new_action)
        
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_config)
        toolbar.addAction(open_action)
        
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_config)
        toolbar.addAction(save_action)
        
        toolbar.addSeparator()
        
        generate_action = QAction('Generate Random', self)
        generate_action.triggered.connect(self.show_generator_tool)
        toolbar.addAction(generate_action)
        
        validate_action = QAction('Validate', self)
        validate_action.triggered.connect(self.show_validator)
        toolbar.addAction(validate_action)
    
    def create_status_bar(self):
        """Create the status bar"""
        self.statusBar().showMessage('Ready')
    
    def create_dockable_panels(self):
        """Create dockable panels"""
        # Set style for dock widgets with dark theme
        # Make title bar lighter so buttons are visible
        dock_style = """
            QDockWidget {
                background-color: #2b2b2b;
                color: #e0e0e0;
            }
            QDockWidget::title {
                background-color: #5a5a5a;
                padding: 4px 8px;
                border: 1px solid #777777;
                color: #ffffff;
                font-weight: bold;
                text-align: left;
            }
            QDockWidget QWidget {
                background-color: #2b2b2b;
                color: #e0e0e0;
            }
        """
        
        # Mob Browser (left dock)
        self.mob_browser = MobBrowserPanel(self)
        self.mob_browser.setStyleSheet(dock_style)
        # Ensure dock features are enabled (close and float buttons)
        self.mob_browser.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.mob_browser)
        self.mob_browser.mob_selected.connect(self.on_mob_selected)
        # Set narrower default width for mob browser
        self.mob_browser.setMinimumWidth(300)
        self.mob_browser.setMaximumWidth(400)
        # Mob browser auto-loads on initialization, but ensure it's visible
        self.mob_browser.show()
        # Resize dock to narrower width (only if actually in a dock area)
        if self.dockWidgetArea(self.mob_browser) != Qt.NoDockWidgetArea:
            try:
                self.resizeDocks([self.mob_browser], [300], Qt.Horizontal)
            except:
                pass  # Ignore if not in layout
        
        # Generator Tool (can be docked or floating)
        self.generator_tool = GeneratorToolPanel(self)
        self.generator_tool.setStyleSheet(dock_style)
        self.generator_tool.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.generator_tool.setMinimumWidth(550)  # Wider minimum for tool panels
        self.generator_tool.hide()
        self.generator_tool.config_generated.connect(self.on_config_generated)
        
        # SQL Builder
        self.sql_builder = SQLBuilderPanel(self)
        self.sql_builder.setStyleSheet(dock_style)
        self.sql_builder.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.sql_builder.setMinimumWidth(550)  # Wider minimum for tool panels
        self.sql_builder.hide()
        
        # Bulk Upload Tool
        self.bulk_upload_tool = BulkUploadToolPanel(self)
        self.bulk_upload_tool.setStyleSheet(dock_style)
        self.bulk_upload_tool.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.bulk_upload_tool.setMinimumWidth(550)  # Wider minimum for tool panels
        self.bulk_upload_tool.hide()
        self.bulk_upload_tool.upload_created.connect(self.on_upload_created)
        
        # Validator
        self.validator_panel = ValidatorPanel(self)
        self.validator_panel.setStyleSheet(dock_style)
        self.validator_panel.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.validator_panel.setMinimumWidth(550)  # Wider minimum for tool panels
        self.validator_panel.hide()
    
    def set_central_widget(self):
        """Set the central widget (Config Editor)"""
        self.config_editor = ConfigEditorPanel(self)
        self.config_editor.setStyleSheet("""
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
        self.setCentralWidget(self.config_editor)
        self.config_editor.config_modified.connect(self.on_config_modified)
        self.config_editor.config_loaded.connect(self.on_config_loaded)
    
    def on_mob_selected(self, wcid, name, max_spawns):
        """Handle mob selection from browser"""
        # TODO: Add to selected position in config editor
        pass
    
    def on_config_generated(self, file_path):
        """Handle config generation"""
        self.config_editor.load_config_file(file_path)
    
    def on_config_modified(self):
        """Handle config modification"""
        self.config_modified = True
        self.update_window_title()
    
    def on_config_loaded(self, file_path):
        """Handle config loaded"""
        self.current_config_path = file_path
        self.config_modified = False
        self.update_window_title()
    
    def on_upload_created(self, file_path):
        """Handle bulk upload created"""
        # Open validator with the file
        self.validator_panel.file_path_edit.setText(file_path)
        self.validator_panel.validate_file(file_path)
        self.show_validator()
    
    def new_config(self):
        """Create a new configuration"""
        if self.check_save_changes():
            self.current_config_path = None
            self.config_modified = False
            self.update_window_title()
            # Clear config editor
            self.config_editor.populate_structure()
    
    def open_config(self):
        """Open an existing configuration"""
        if not self.check_save_changes():
            return
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Open Event Configuration',
            '',
            'CSV Files (*.csv);;All Files (*.*)'
        )
        
        if file_path:
            self.load_config_file(file_path)
    
    def save_config(self):
        """Save the current configuration"""
        if self.current_config_path:
            if self.config_editor.save_config_file(self.current_config_path):
                self.config_modified = False
                self.update_window_title()
                self.statusBar().showMessage(f'Saved: {self.current_config_path}', 3000)
        else:
            self.save_config_as()
    
    def save_config_as(self):
        """Save the current configuration with a new name"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            'Save Event Configuration',
            '',
            'CSV Files (*.csv);;All Files (*.*)'
        )
        
        if file_path:
            if self.config_editor.save_config_file(file_path):
                self.current_config_path = file_path
                self.config_modified = False
                self.update_window_title()
                self.statusBar().showMessage(f'Saved: {file_path}', 3000)
    
    def load_config_file(self, file_path: str):
        """Load a configuration file"""
        self.config_editor.load_config_file(file_path)
    
    def check_save_changes(self) -> bool:
        """Check if there are unsaved changes and prompt to save"""
        if not self.config_modified:
            return True
        
        reply = QMessageBox.question(
            self,
            'Unsaved Changes',
            'The current configuration has been modified. Save changes?',
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            QMessageBox.Save
        )
        
        if reply == QMessageBox.Save:
            self.save_config()
            return True
        elif reply == QMessageBox.Discard:
            return True
        else:
            return False
    
    def update_window_title(self):
        """Update the window title with current file and modified status"""
        title = 'Event Hub Configurator'
        if self.current_config_path:
            filename = os.path.basename(self.current_config_path)
            title = f'{filename} - {title}'
            if self.config_modified:
                title = f'*{title}'
        elif self.config_modified:
            title = f'*{title}'
        
        self.setWindowTitle(title)
    
    def show_generator_tool(self):
        """Show generator tool panel"""
        self.generator_tool.show()
        self.generator_tool.raise_()
        # Set wider default width for tool panels (600px)
        # Only resize if docked and visible and actually in a dock area
        if self.generator_tool.isVisible() and not self.generator_tool.isFloating():
            # Check if dock widget is actually in a dock area
            if self.dockWidgetArea(self.generator_tool) != Qt.NoDockWidgetArea:
                try:
                    self.resizeDocks([self.generator_tool], [600], Qt.Horizontal)
                except:
                    pass  # Ignore if not in layout
        elif self.generator_tool.isFloating():
            # If floating, resize the widget itself
            self.generator_tool.resize(600, self.generator_tool.height())
    
    def show_sql_builder(self):
        """Show SQL builder panel"""
        if self.current_config_path:
            self.sql_builder.config_path_edit.setText(self.current_config_path)
        self.sql_builder.show()
        self.sql_builder.raise_()
        # Set wider default width for tool panels (600px)
        # Only resize if docked and visible and actually in a dock area
        if self.sql_builder.isVisible() and not self.sql_builder.isFloating():
            # Check if dock widget is actually in a dock area
            if self.dockWidgetArea(self.sql_builder) != Qt.NoDockWidgetArea:
                try:
                    self.resizeDocks([self.sql_builder], [600], Qt.Horizontal)
                except:
                    pass  # Ignore if not in layout
        elif self.sql_builder.isFloating():
            # If floating, resize the widget itself
            self.sql_builder.resize(600, self.sql_builder.height())
    
    def show_bulk_upload_tool(self):
        """Show bulk upload tool panel"""
        self.bulk_upload_tool.show()
        self.bulk_upload_tool.raise_()
        # Set wider default width for tool panels (600px)
        # Only resize if docked and visible and actually in a dock area
        if self.bulk_upload_tool.isVisible() and not self.bulk_upload_tool.isFloating():
            # Check if dock widget is actually in a dock area
            if self.dockWidgetArea(self.bulk_upload_tool) != Qt.NoDockWidgetArea:
                try:
                    self.resizeDocks([self.bulk_upload_tool], [600], Qt.Horizontal)
                except:
                    pass  # Ignore if not in layout
        elif self.bulk_upload_tool.isFloating():
            # If floating, resize the widget itself
            self.bulk_upload_tool.resize(600, self.bulk_upload_tool.height())
    
    def show_validator(self):
        """Show validator panel"""
        self.validator_panel.show()
        self.validator_panel.raise_()
        # Set wider default width for tool panels (600px)
        # Only resize if docked and visible and actually in a dock area
        if self.validator_panel.isVisible() and not self.validator_panel.isFloating():
            # Check if dock widget is actually in a dock area
            if self.dockWidgetArea(self.validator_panel) != Qt.NoDockWidgetArea:
                try:
                    self.resizeDocks([self.validator_panel], [600], Qt.Horizontal)
                except:
                    pass  # Ignore if not in layout
        elif self.validator_panel.isFloating():
            # If floating, resize the widget itself
            self.validator_panel.resize(600, self.validator_panel.height())
    
    def show_mob_list_manager(self):
        """Show mob list manager dialog"""
        dialog = MobListManagerDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            # Refresh mob browser
            self.mob_browser.load_mobs()
    
    def toggle_mob_browser(self, checked):
        """Toggle mob browser visibility"""
        self.mob_browser.setVisible(checked)
    
    def toggle_generator_tool(self, checked):
        """Toggle generator tool visibility"""
        self.generator_tool.setVisible(checked)
    
    def toggle_sql_builder(self, checked):
        """Toggle SQL builder visibility"""
        self.sql_builder.setVisible(checked)
    
    def toggle_bulk_upload_tool(self, checked):
        """Toggle bulk upload tool visibility"""
        self.bulk_upload_tool.setVisible(checked)
    
    def toggle_validator(self, checked):
        """Toggle validator visibility"""
        self.validator_panel.setVisible(checked)
    
    def clear_all(self):
        """Clear all position assignments"""
        self.config_editor.clear_all()
    
    def fill_random(self):
        """Fill empty positions with random mobs"""
        self.config_editor.fill_random()
    
    def reset_layout(self):
        """Reset the window layout to default"""
        reply = QMessageBox.question(
            self,
            'Reset Layout',
            'Reset window layout to default?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Reset dock positions
            self.mob_browser.setFloating(False)
            self.addDockWidget(Qt.LeftDockWidgetArea, self.mob_browser)
            self.statusBar().showMessage('Layout reset', 2000)
    
    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self,
            'About Event Hub Configurator',
            'Event Hub Configurator\n\n'
            'A GUI application for generating and managing\n'
            'Asheron\'s Call event configurations.\n\n'
            'Version 1.0'
        )
    
    def load_settings(self):
        """Load application settings"""
        geometry = self.settings.value('geometry')
        if geometry:
            self.restoreGeometry(geometry)
        
        state = self.settings.value('windowState')
        if state:
            self.restoreState(state)
    
    def save_settings(self):
        """Save application settings"""
        self.settings.setValue('geometry', self.saveGeometry())
        self.settings.setValue('windowState', self.saveState())
    
    def closeEvent(self, event):
        """Handle window close event"""
        if self.check_save_changes():
            self.save_settings()
            event.accept()
        else:
            event.ignore()
