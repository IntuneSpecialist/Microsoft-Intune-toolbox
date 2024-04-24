$value = Get-ItemPropertyValue -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "DisableDomainCreds"

if ($value -eq [int]1) {
    Write-Host "DisableDomainCreds has been detected"
    Exit 0
}

else {
    Write-Host "DisableDomainCreds has not been detected"
    Exit 1
}