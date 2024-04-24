Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "RunAsPPL" -Value 0
Write-Host "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL was set to 0"