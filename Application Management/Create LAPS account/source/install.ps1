if ("$env:PROCESSOR_ARCHITEW6432" -ne "ARM64") {
    if (Test-Path "$($env:WINDIR)\SysNative\WindowsPowerShell\v1.0\powershell.exe")
    {
        & "$($env:WINDIR)\SysNative\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy bypass -NoProfile -File "$PSCommandPath"
        Exit $lastexitcode
    }
}

###Script###
function Get-RandomPassword {
    param (
        [Parameter(Mandatory)]
        [int] $length,
        [int] $amountOfNonAlphanumeric = 1
    )
    Add-Type -AssemblyName 'System.Web'
    return [System.Web.Security.Membership]::GeneratePassword($length, $amountOfNonAlphanumeric)
}
$PlainPassword = Get-RandomPassword 15
$SecurePassword = $PlainPassword | ConvertTo-SecureString -AsPlainText -Force 

New-LocalUser -Name "laps-admin" -Description "Local Administrator Password Solution (LAPS)" -AccountNeverExpires:$true -Password $SecurePassword
Add-LocalGroupMember -Group "Administrators" -Member "laps-admin"