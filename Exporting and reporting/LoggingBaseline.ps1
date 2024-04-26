### Parameters ###
$logginglocation = "C:\ProgramData\Intune\IntuneDeploymentLogging"
$NameIntuneApp = "USE THE SAME NAME AS YOU USE IN INTUNE TO NAME THE APP."
$versionnumber = "For example V1"
$installoruninstall = "For example install OR uninstall"
$loggingpath = "$logginglocation\$NameIntuneApp\$versionnumber\$installoruninstall-transcript.txt"
$msilog = "$logginglocation\$NameIntuneApp\$versionnumber\$installoruninstall-msi.txt"

### Notes ###
### For MSI installations you can use: msiexec /i ".\MSIPACKAGE" /qn /log $msilog ###
### For MSI deletions you can use: msiexec /x ".\MSIPACKAGE" /qn /log $msilog ###
### Location of logging will be C:\ProgramData\Intune\IntuneDeploymentLogging ###
 
### Switch on logging ###
Start-Transcript -Append "$loggingpath"

### Create logging location if not present ###
if (-not(Test-Path -Path $logginglocation -PathType Leaf)) {
New-Item -ItemType Directory -Path $logginglocation -Force -ErrorAction Stop}

### YOUR SCRIPT HERE ###

### End of script ###
Stop-Transcript
