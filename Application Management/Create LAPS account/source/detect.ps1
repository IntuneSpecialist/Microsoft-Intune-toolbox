###Parameters###
$logginglocation = "C:\ProgramData\Intune\IntuneDeploymentLogging"
$NameIntuneApp = "Local Admin account"
$versionnumber = "V1"
$installoruninstall = "detect"
$loggingpath = "$logginglocation\$NameIntuneApp\$versionnumber\$installoruninstall-transcript.txt"
 
###Switch on logging###
Start-Transcript -Append "$loggingpath"
###Create logging location###
if (-not(Test-Path -Path $logginglocation -PathType Leaf)) {
New-Item -ItemType Directory -Path $logginglocation -Force -ErrorAction Stop}

###Script###
$localuser = Get-LocalUser -Name "laps-admin"
if ($localuser) {
    continue
}

else {
    exit 1
}

try {Add-LocalGroupMember -Group "Administrators" -Member "laps-admin" -ErrorAction Stop -Verbose}
catch [Microsoft.PowerShell.Commands.MemberExistsException] {
    Write-Warning -Message "Member of group already exists."
    Exit 0
}

catch {
    Write-Warning -Message "Another error"
    Exit 1
}

###End of script###
Stop-Transcript