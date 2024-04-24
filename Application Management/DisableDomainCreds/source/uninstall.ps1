Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name "DisableDomainCreds" -Value 0
Write-Host "HKLM:\System\CurrentControlSet\Control\Lsa\DisableDomainCreds was set to 0"