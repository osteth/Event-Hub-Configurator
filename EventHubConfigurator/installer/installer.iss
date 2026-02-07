; Inno Setup Installer Script for Event Hub Configurator
; This script creates a Windows installer for the application

[Setup]
AppName=Event Hub Configurator
AppVersion=1.0
AppPublisher=Event Hub Configurator
AppPublisherURL=
DefaultDirName={pf}\EventHubConfigurator
DefaultGroupName=Event Hub Configurator
OutputDir=.
OutputBaseFilename=EventHubConfigurator_Setup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
LicenseFile=
InfoBeforeFile=
InfoAfterFile=
SetupIconFile=
WizardImageFile=
WizardSmallImageFile=

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
; Application files
Source: "..\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Exclude Python cache and build files
Source: "..\*.pyc"; DestDir: "{app}"; Flags: ignoreversion; Excludes: "*.pyc"
Source: "..\__pycache__\*"; DestDir: "{app}\__pycache__"; Flags: ignoreversion; Excludes: "*"

[Icons]
Name: "{group}\Event Hub Configurator"; Filename: "{app}\main.py"; IconFilename: "{app}\main.py"
Name: "{group}\{cm:UninstallProgram,Event Hub Configurator}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Event Hub Configurator"; Filename: "{app}\main.py"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Event Hub Configurator"; Filename: "{app}\main.py"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\main.py"; Description: "{cm:LaunchProgram,Event Hub Configurator}"; Flags: nowait postinstall skipifsilent

[Code]
function InitializeSetup(): Boolean;
begin
  Result := True;
  // Check if Python is installed
  // Note: This is a basic check - you may want to add more robust Python detection
end;
