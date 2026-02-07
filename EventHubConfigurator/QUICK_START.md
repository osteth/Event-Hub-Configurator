# Quick Start Guide

## Running the Application

### Prerequisites

1. Python 3.7 or higher installed
2. PyQt5 installed: `pip install PyQt5`

### Launch

From the `EventHubConfigurator` directory:

```bash
python main.py
```

## Basic Workflow

### 1. Generate a Random Event

1. Click **Generate > Random Event** (or use the toolbar button)
2. Select tier(s), wave mode, boss count
3. Click **Generate Random Event**
4. Click **Generate and Load** to load into the editor

### 2. Edit Configuration

1. **Drag mobs** from the Mob Browser (left panel) to position slots in the Config Editor (center)
2. **Edit spawn counts** by clicking on the spawn count value in the tree
3. **Clear positions** by right-clicking and selecting "Clear"

### 3. Save Configuration

1. Click **File > Save Config** (or Ctrl+S)
2. Choose a location and filename
3. The CSV file will be saved in the same format as the command-line scripts

### 4. Generate SQL Files

1. Click **Generate > SQL Files**
2. Select your configuration CSV file (or use current open config)
3. Choose output directory (default: same as config file)
4. Click **Generate SQL Files**
5. Files will be created in `Low Event Sequence/`, `Mid Event Sequence/`, `High Event Sequence/` directories

### 5. Create Bulk Upload

1. Click **Generate > Bulk Upload**
2. Select SQL files directory (or use Auto-detect)
3. Choose output file (or use default timestamped name)
4. Click **Create Bulk Upload**
5. The bulk SQL file is ready for deployment

### 6. Validate SQL

1. Click **Tools > Validate SQL**
2. Select your bulk upload SQL file
3. Click **Validate**
4. Review errors and warnings
5. Export report if needed

## Managing Mobs

### Add/Edit/Delete Mobs

1. Click **Tools > Manage Mob List**
2. Use **Add Mob** to create new entries
3. **Double-click** or use **Edit Mob** to modify existing entries
4. Select a mob and click **Delete Mob** to remove
5. Click **Save** to apply changes

### Import/Export

- **Import CSV**: Merge or replace mob list from another CSV file
- **Export CSV**: Backup your mob list to a CSV file

## Tips

- **Panel Layout**: Drag panels to rearrange them. Use **View** menu to show/hide panels
- **Keyboard Shortcuts**: Standard shortcuts work (Ctrl+S to save, Ctrl+O to open, etc.)
- **Recent Files**: Access recently opened configs from **File > Recent Files**
- **Auto-save**: The application will prompt to save unsaved changes before closing

## Troubleshooting

### Application won't start
- Check Python version: `python --version` (should be 3.7+)
- Verify PyQt5: `pip list | findstr PyQt5`
- Check console for error messages

### Drag-and-drop not working
- Ensure you're dragging from Mob Browser (left panel)
- Drop on position items (not tier or wave parent items)
- Check that mob data is valid

### SQL generation fails
- Verify config CSV is valid
- Check that all mobs in config exist in Spawnable Mobs List
- Ensure output directory is writable
