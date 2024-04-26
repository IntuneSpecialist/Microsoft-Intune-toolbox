$ProgIDname = Get-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.pdf\UserChoice"

if ($ProgIDname.ProgID -eq "AcroExch.Document.DC") {
    Write-Host "Standaard software is Adobe Acrobat"
    }

elseif ($ProgIDname.ProgID -eq "Acrobat.Document.DC") {
    Write-Host "Standaard software is Adobe Acrobat"
    }

else {
    CreateAnErrorMessageByThisUglyMethod
    }