"""Generator Tool Panel - Random event generation"""

from PyQt5.QtWidgets import (
    QDockWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QSpinBox, QLineEdit,
    QGroupBox, QTextEdit, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal

from core.event_generator import generate_random_event


class GeneratorToolPanel(QDockWidget):
    """Panel for generating random event configurations"""
    
    config_generated = pyqtSignal(str)  # Emits path to generated CSV
    
    def __init__(self, parent=None):
        super().__init__('Random Event Generator', parent)
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
            QPushButton:checked {
                background-color: #0066cc;
            }
            QLabel {
                background-color: transparent;
                color: #e0e0e0;
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
            QTextEdit {
                background-color: #353535;
                color: #e0e0e0;
                border: 1px solid #555555;
            }
            QGroupBox {
                background-color: #2b2b2b;
                color: #e0e0e0;
                border: 1px solid #555555;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        widget.setLayout(layout)
        self.setWidget(widget)
        
        # Options group
        options_group = QGroupBox('Generation Options')
        options_layout = QVBoxLayout()
        options_group.setLayout(options_layout)
        layout.addWidget(options_group)
        
        # Tier selection
        tier_layout = QHBoxLayout()
        tier_label = QLabel('Tiers:')
        tier_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        tier_layout.addWidget(tier_label)
        self.tier_combo = QComboBox()
        self.tier_combo.addItems(['All', 'Low', 'Mid', 'High'])
        tier_layout.addWidget(self.tier_combo)
        options_layout.addLayout(tier_layout)
        
        # Wave mode
        self.mixed_waves_check = QPushButton('Mixed Waves')
        self.mixed_waves_check.setCheckable(True)
        self.mixed_waves_check.setChecked(False)
        options_layout.addWidget(self.mixed_waves_check)
        
        # Boss count
        boss_layout = QHBoxLayout()
        boss_label = QLabel('Boss Count:')
        boss_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        boss_layout.addWidget(boss_label)
        self.boss_spin = QSpinBox()
        self.boss_spin.setMinimum(1)
        self.boss_spin.setMaximum(4)
        self.boss_spin.setValue(1)
        boss_layout.addWidget(self.boss_spin)
        options_layout.addLayout(boss_layout)
        
        # Random seed
        seed_layout = QHBoxLayout()
        seed_label = QLabel('Seed (optional):')
        seed_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        seed_layout.addWidget(seed_label)
        self.seed_input = QLineEdit()
        self.seed_input.setPlaceholderText('Leave empty for random')
        seed_layout.addWidget(self.seed_input)
        options_layout.addLayout(seed_layout)
        
        # Output filename (optional)
        filename_layout = QHBoxLayout()
        filename_label = QLabel('Filename (optional):')
        filename_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        filename_layout.addWidget(filename_label)
        self.filename_input = QLineEdit()
        self.filename_input.setPlaceholderText('Leave empty for auto-generated name')
        filename_layout.addWidget(self.filename_input)
        options_layout.addLayout(filename_layout)
        
        # Generate button
        generate_btn = QPushButton('Generate Random Event')
        generate_btn.clicked.connect(self.generate_event)
        layout.addWidget(generate_btn)
        
        # Output path
        output_layout = QHBoxLayout()
        output_label = QLabel('Output:')
        output_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        output_layout.addWidget(output_label)
        self.output_label = QLabel('(not generated yet)')
        self.output_label.setStyleSheet('color: #b0b0b0; background-color: transparent;')
        output_layout.addWidget(self.output_label)
        layout.addLayout(output_layout)
        
        # Preview (read-only text area)
        preview_label = QLabel('Preview:')
        preview_label.setStyleSheet('color: #e0e0e0; background-color: transparent; font-weight: bold;')
        layout.addWidget(preview_label)
        
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        layout.addWidget(self.preview_text)
    
    def generate_event(self):
        """Generate a random event configuration and auto-load it"""
        try:
            # Get options
            tier_text = self.tier_combo.currentText()
            tiers = ['low', 'mid', 'high'] if tier_text == 'All' else [tier_text.lower()]
            mixed_waves = self.mixed_waves_check.isChecked()
            boss_count = self.boss_spin.value()
            
            seed_text = self.seed_input.text().strip()
            seed = int(seed_text) if seed_text else None
            
            # Get filename if provided
            filename_text = self.filename_input.text().strip()
            output_file = None
            if filename_text:
                # Ensure .csv extension
                if not filename_text.endswith('.csv'):
                    filename_text += '.csv'
                # Build full path (use same directory as generate_random_event default)
                from pathlib import Path
                _script_dir = Path(__file__).parent.parent.parent.parent
                output_file = str(_script_dir / filename_text)
            
            # Generate
            output_file = generate_random_event(
                tiers=tiers,
                mixed_waves=mixed_waves,
                boss_count=boss_count,
                seed=seed,
                output_file=output_file  # None if not specified, will use default
            )
            
            self.output_label.setText(output_file)
            
            # Show preview (first 50 lines)
            with open(output_file, 'r') as f:
                lines = f.readlines()[:50]
                self.preview_text.setText(''.join(lines))
                if len(lines) == 50:
                    self.preview_text.append('\n... (truncated)')
            
            # Auto-load the generated config into the editor
            self.config_generated.emit(output_file)
            
            QMessageBox.information(self, 'Success', f'Event configuration generated and loaded:\n{output_file}')
            
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to generate event: {e}')
