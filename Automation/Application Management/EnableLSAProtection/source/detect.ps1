$value = Get-ItemPropertyValue -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "RunAsPPL"

if ($value) {
    Write-Host "LSA Protection has been detected"
    Exit 0
}

else {
    Write-Host "LSA Protection has not been detected"
    Exit 1
}