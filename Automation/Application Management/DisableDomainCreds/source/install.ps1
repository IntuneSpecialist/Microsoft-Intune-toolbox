Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name "DisableDomainCreds" -Value 1
Write-Host "HKLM:\System\CurrentControlSet\Control\Lsa\DisableDomainCreds was set to 1"