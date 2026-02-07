"""Main entry point for Event Hub Configurator"""

import sys
import os
from pathlib import Path

# Add parent directory to path for imports (to access original scripts)
_script_dir = Path(__file__).parent.parent
sys.path.insert(0, str(_script_dir))

# Add current directory to path for module imports
_current_dir = Path(__file__).parent
sys.path.insert(0, str(_current_dir))

from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtGui import QColor
from gui.main_window import MainWindow


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName('Event Hub Configurator')
    app.setOrganizationName('EventHubConfigurator')
    
    # Use Fusion style for better control over dock widget buttons
    app.setStyle(QStyleFactory.create('Fusion'))
    
    # Set dark theme palette for dialogs and message boxes
    palette = app.palette()
    palette.setColor(palette.Window, QColor(43, 43, 43))
    palette.setColor(palette.WindowText, QColor(224, 224, 224))
    palette.setColor(palette.Base, QColor(53, 53, 53))
    palette.setColor(palette.AlternateBase, QColor(60, 60, 60))
    palette.setColor(palette.ToolTipBase, QColor(43, 43, 43))
    palette.setColor(palette.ToolTipText, QColor(224, 224, 224))
    palette.setColor(palette.Text, QColor(224, 224, 224))
    palette.setColor(palette.Button, QColor(64, 64, 64))
    palette.setColor(palette.ButtonText, QColor(224, 224, 224))
    palette.setColor(palette.BrightText, QColor(255, 255, 255))
    palette.setColor(palette.Link, QColor(0, 102, 204))
    palette.setColor(palette.Highlight, QColor(0, 102, 204))
    palette.setColor(palette.HighlightedText, QColor(255, 255, 255))
    app.setPalette(palette)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
