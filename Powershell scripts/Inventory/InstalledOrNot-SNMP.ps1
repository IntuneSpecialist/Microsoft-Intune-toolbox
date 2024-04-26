$SNMPInstalled = Get-WindowsCapability -Online -Name "SNMP*"
    
if ($SNMPInstalled.State -eq "Installed"){
        Write-Host "Installed"
    }

else {
    CreateAnErrorMessageByThisUglyMethod
    }