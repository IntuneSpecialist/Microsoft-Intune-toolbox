###Parameters###
$logginglocation = "C:\ProgramData\Intune\IntuneDeploymentLogging"
$NameIntuneApp = "WLAN Driver Update"
$versionnumber = "V1"
$installoruninstall = "install "
$loggingpath = "$logginglocation\$NameIntuneApp\$versionnumber\$installoruninstall-transcript.txt"
# $msilog = "$logginglocation\$NameIntuneApp\$versionnumber\$installoruninstall-msi.txt"

###Notes###
### For MSI installations you can use: msiexec /i ".\MSIPACKAGE" /qn /log $msilog ###
### For MSI deletions you can use: msiexec /x ".\MSIPACKAGE" /qn /log $msilog ###
### Location of logging will be C:\ProgramData\Intune\IntuneDeploymentLogging ###
 
###Switch on logging###
Start-Transcript -Append "$loggingpath"
###Create logging location###
if (-not(Test-Path -Path $logginglocation -PathType Leaf)) {
New-Item -ItemType Directory -Path $logginglocation -Force -ErrorAction Stop}

### YOUR SCRIPT HERE ###
# Get network adapter information
$networkAdapters = Get-NetAdapter -Physical -InterfaceDescription "*8822*" | Select-Object Name, InterfaceDescription, DriverVersion, DriverDate, DriverProvider, MacAddress

# Check if any matching network adapters were found
if ($networkAdapters) {
    $neededversion = "2024.10.228.9"
    $neededversion = $neededversion -replace '\.', ''
    $neededversion = [long]$neededversion

    $actualdriver = $networkAdapters.DriverVersion
    $actualdriver = $actualdriver -replace '\.', ''
    $actualdriver = [long]$actualdriver 

    if ($actualdriver -lt $neededversion) {
        Disable-NetAdapterPowerManagement -InterfaceDescription “*8822*”
        # install HP drivers silently
        $installerPath = ".\sp150721.exe"
        & $installerPath /S
        Write-Host "Driver update initiated"
        exit 0  
        }

    else {
        Write-Host "Driver already has been updated"
        exit 1
        }
} 

else {
    Write-Host "No network adapters matching the criteria were found."
    exit 0
}

###End of script###
Stop-Transcript