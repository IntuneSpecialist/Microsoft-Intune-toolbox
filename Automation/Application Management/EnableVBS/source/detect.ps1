$value = Get-ItemPropertyValue -Path "HKLM:\System\CurrentControlSet\Control\DeviceGuard" -Name "EnableVirtualizationBasedSecurity"

if ($value) {
    Write-Host "Virtualization-Based Security has been detected"
    Exit 0
}

else {
    Write-Host "Virtualization-Based Security has not been detected"
    Exit 1
}