# Event Hub Configurator

A PyQt5-based GUI application for generating and managing Asheron's Call event configurations.

## Features

- **Random Event Generation**: Generate randomized event configurations with customizable options
- **Visual Config Editor**: Drag-and-drop interface for editing event configurations
- **Mob Management**: Add, edit, and delete mobs from the spawnable mobs list
- **SQL Generation**: Generate SQL files for Position Generators, Wave Controllers, and Event Controllers
- **Bulk Upload Creation**: Combine all SQL files into a single bulk upload file
- **SQL Validation**: Validate generated SQL files before deployment

## Requirements

- Python 3.7 or higher
- PyQt5 5.15.0 or higher

## Installation

### From Source

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

### Windows Installer

1. Download `EventHubConfigurator_Setup.exe` from the releases
2. Run the installer and follow the prompts
3. Launch "Event Hub Configurator" from the Start Menu or desktop shortcut

## Usage

### Basic Workflow

1. **Generate or Load Configuration**
   - Use "Generate > Random Event" to create a new random configuration
   - Or use "File > Open Config" to load an existing CSV file

2. **Edit Configuration**
   - Drag mobs from the Mob Browser panel to position slots in the Config Editor
   - Adjust spawn counts by editing the values in the tree
   - Save your changes with "File > Save Config"

3. **Generate SQL Files**
   - Use "Generate > SQL Files" to create SQL files from your configuration
   - Files will be created in `Low Event Sequence/`, `Mid Event Sequence/`, and `High Event Sequence/` directories

4. **Create Bulk Upload**
   - Use "Generate > Bulk Upload" to combine all SQL files into a single file
   - The bulk upload file can be executed directly on your ACE server database

5. **Validate SQL**
   - Use "Tools > Validate SQL" to check your bulk upload file for errors
   - Export validation reports for documentation

### Managing Mobs

- **Add New Mobs**: Use "Tools > Manage Mob List" to add, edit, or delete mobs
- **Import/Export**: Import mob lists from CSV or export for backup

## File Formats

### Configuration CSV Format

The application uses CSV files with the following format:
```csv
tier,wave_number,position_index,wcid,spawn_count
low,1,0,290500204,4
low,1,1,290500204,4
...
```

### Spawnable Mobs List Format

```csv
ID,Name,Difficulty,Difficulty (eg: boss),Spawns Per Location
290444489,Charred Benedino,High,TRUE,7
290500550,Molten Menace,High,FALSE,1
...
```

## Architecture

The application follows a modular architecture:

- **Core Modules**: Wrappers around existing Python scripts (`core/`)
- **GUI Panels**: Dockable panels for different features (`gui/panels/`)
- **Widgets**: Reusable UI components (`gui/widgets/`)
- **Utils**: Helper functions (`gui/utils/`)

## Compatibility

All generated files are compatible with the original command-line scripts:
- CSV configuration files work with `generate_random_event.py`
- SQL files work with `generate_event_files.py`
- Bulk upload files work with `create_bulk_upload.py`
- Files can be validated with `validate_sql.py`

## Troubleshooting

### Application Won't Start

- Ensure Python 3.7+ is installed
- Verify PyQt5 is installed: `pip install PyQt5`
- Check that all files are in the correct directory structure

### SQL Generation Fails

- Verify the configuration CSV file is valid
- Check that all required mobs exist in `Spawnable Mobs List.csv`
- Ensure output directory is writable

### Drag-and-Drop Not Working

- Make sure you're dragging from the Mob Browser panel
- Drop on position items (not tier or wave items)
- Check that the mob has valid data (WCID, Name, Max Spawns)

## License

This is an open-source project. See LICENSE file for details.

## Support

For issues or questions, please open an issue on the project repository.
