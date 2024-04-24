Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "RunAsPPL" -Value 1
Write-Host "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL was set to 1"