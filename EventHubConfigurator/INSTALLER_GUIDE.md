# Event Hub Configurator - Installer Guide

## Building the Windows Installer

This guide explains how to create a Windows installer for Event Hub Configurator using Inno Setup.

## Prerequisites

1. **Inno Setup** (free, available at https://jrsoftware.org/isdl.php)
   - Download and install Inno Setup 6 or later
   - The installer script is located at `installer/installer.iss`

2. **Python Runtime** (for bundling)
   - Option 1: Use PyInstaller to create a standalone executable
   - Option 2: Bundle Python with the application
   - Option 3: Require users to have Python installed

## Building with PyInstaller (Recommended)

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Create Executable

```bash
cd EventHubConfigurator
pyinstaller --onefile --windowed --name "EventHubConfigurator" main.py
```

This creates a single executable file in the `dist/` directory.

### Step 3: Update Installer Script

Modify `installer.iss` to include the PyInstaller executable:

```ini
[Files]
Source: "dist\EventHubConfigurator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs
```

### Step 4: Build Installer

1. Open `installer/installer.iss` in Inno Setup Compiler
2. Click "Build > Compile" (or press F9)
3. The installer will be created in the `installer/` directory

## Building with Embedded Python

### Step 1: Download Embedded Python

Download Python 3.11+ embedded distribution from python.org

### Step 2: Update Installer Script

Modify `installer.iss` to include Python:

```ini
[Files]
Source: "python\*"; DestDir: "{app}\python"; Flags: ignoreversion recursesubdirs
Source: "..\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
```

### Step 3: Create Launcher Script

Create a batch file launcher:

```batch
@echo off
cd /d "%~dp0"
python\python.exe main.py
```

Include this in the installer and set it as the main executable.

## Installer Customization

### Adding Icons

1. Create or obtain an icon file (`.ico`)
2. Update `SetupIconFile` in `installer.iss`:
   ```ini
   SetupIconFile=icon.ico
   ```

### Adding License File

1. Create a license text file
2. Update `LicenseFile` in `installer.iss`:
   ```ini
   LicenseFile=LICENSE.txt
   ```

### Customizing Installation Path

Modify `DefaultDirName` in `installer.iss`:
```ini
DefaultDirName={pf}\EventHubConfigurator
```

Options:
- `{pf}` = Program Files
- `{localappdata}` = User's Local AppData
- `{userdocs}` = User's Documents

## Testing the Installer

1. Run the installer on a clean Windows system (or VM)
2. Verify all files are installed correctly
3. Test launching the application
4. Verify all features work correctly
5. Test uninstallation

## Distribution

The installer file (`EventHubConfigurator_Setup.exe`) can be distributed to users. They simply need to:

1. Download the installer
2. Run it
3. Follow the installation wizard
4. Launch the application from Start Menu or desktop shortcut

## Notes

- The installer requires administrator privileges for installation to Program Files
- Users can choose a different installation directory during setup
- The uninstaller is automatically created and can be accessed from Control Panel
