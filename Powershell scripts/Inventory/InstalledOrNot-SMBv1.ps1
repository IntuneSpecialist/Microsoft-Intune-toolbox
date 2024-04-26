$SMB = Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol

if ($SMB.State -eq "Enabled") {
    Write-Host "SMBv1 is enabled"
    }

else{
    CreateAnErrorMessageByThisUglyMethod
    }