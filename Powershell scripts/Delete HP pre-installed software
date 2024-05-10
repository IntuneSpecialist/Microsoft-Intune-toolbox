# List of built-in apps to remove
$UninstallPackages = @(
    "AD2F1837.HPJumpStarts"
    "AD2F1837.HPPCHardwareDiagnosticsWindows"
    "AD2F1837.HPPowerManager"
    "AD2F1837.HPPrivacySettings"
    "AD2F1837.HPSupportAssistant"
    "AD2F1837.HPSureShieldAI"
    "AD2F1837.HPSystemInformation"
    "AD2F1837.HPQuickDrop"
    "AD2F1837.HPWorkWell"
    "AD2F1837.myHP"
    "AD2F1837.HPDesktopSupportUtilities"
    "AD2F1837.HPQuickTouch"
    "AD2F1837.HPEasyClean"
    "AD2F1837.HPSystemInformation"
)

# List of programs to uninstall
$UninstallPrograms = @(
    "HP Client Security Manager"
    "HP Connection Optimizer"
    "HP Documentation"
    "HP MAC Address Manager"
    "HP Notifications"
    "HP Security Update Service"
    "HP System Default Settings"
    "HP Sure Click"
    "HP Sure Click Security Browser"
    "HP Sure Run"
    "HP Sure Recover"
    "HP Sure Sense"
    "HP Sure Sense Installer"
    "HP Support Assistant"
    "HP Wolf Security"
    "HP Wolf Security Application Support for Sure Sense"
    "HP Wolf Security Application Support for Windows"
)

$optimizerUninstallAnswer = @"
[InstallShield Silent]
Version=v7.00
File=Response File
[File Transfer]
OverwrittenReadOnly=NoToAll
[{6468C4A5-E47E-405F-B675-A70A70983EA6}-DlgOrder]
Dlg0={6468C4A5-E47E-405F-B675-A70A70983EA6}-SdWelcomeMaint-0
Count=3
Dlg1={6468C4A5-E47E-405F-B675-A70A70983EA6}-MessageBox-0
Dlg2={6468C4A5-E47E-405F-B675-A70A70983EA6}-SdFinishReboot-0
[{6468C4A5-E47E-405F-B675-A70A70983EA6}-SdWelcomeMaint-0]
Result=303
[{6468C4A5-E47E-405F-B675-A70A70983EA6}-MessageBox-0]
Result=6
[Application]
Name=HP Connection Optimizer
Version=2.0.18.0
Company=HP Inc.
Lang=0409
[{6468C4A5-E47E-405F-B675-A70A70983EA6}-SdFinishReboot-0]
Result=1
BootOption=0
"@

# Run inventories
$HPidentifier = "AD2F1837"
$InstalledPackages = Get-AppxPackage -AllUsers | Where-Object {($UninstallPackages -contains $_.Name) -or ($_.Name -match "^$HPidentifier")} -Verbose
$ProvisionedPackages = Get-AppxProvisionedPackage -Online | Where-Object {($UninstallPackages -contains $_.DisplayName) -or ($_.DisplayName -match "^$HPidentifier")} -Verbose
$InstalledPrograms = Get-Package | Where-Object {$UninstallPrograms -contains $_.Name} -Verbose
$HPCommRecoveryPresent = Test-Path -Path "C:\Program Files\HPCommRecovery"
$apps = Get-WmiObject -Class Win32_Product | Where-Object {$_.Name -match "HP"}
$HPSAuninstall = "${Env:ProgramFiles(x86)}\HP\HP Support Framework\UninstallHPSA.exe"

# Remove HP APPX provisioned packages - AppxProvisionedPackage
function Step1 {
    ForEach ($ProvPackage in $ProvisionedPackages) {
        Write-Host -Object "Attempting to remove provisioned package: [$($ProvPackage.DisplayName)]..."

        Try {
            $Null = Remove-AppxProvisionedPackage -PackageName $ProvPackage.PackageName -Online -ErrorAction Stop -Verbose
            Write-Host -Object "Successfully removed provisioned package: [$($ProvPackage.DisplayName)]"
        }
        Catch {Write-Warning -Message "Failed to remove provisioned package: [$($ProvPackage.DisplayName)]"}
    }

    # Go to the next function
    Step2
}

# Remove HP APPX packages - AppxPackage
function Step2 {
    ForEach ($AppxPackage in $InstalledPackages) {                                 
        Write-Host -Object "Attempting to remove Appx package: [$($AppxPackage.Name)]..."

        Try {
            $Null = Remove-AppxPackage -Package $AppxPackage.PackageFullName -AllUsers -ErrorAction Stop -Verbose
            Write-Host -Object "Successfully removed Appx package: [$($AppxPackage.Name)]"
        }
        Catch {Write-Warning -Message "Failed to remove Appx package: [$($AppxPackage.Name)]"}
    }

    # Go to the next function
    Step3
}

# Remove HP installed programs
function Step3 {
    $InstalledPrograms | ForEach-Object {
        Try {
            $Null = $_ | Uninstall-Package -AllVersions -Force -ErrorAction Stop -Verbose
            Write-Host -Object "Successfully uninstalled: [$($_.Name)]"
        }
        Catch {Write-Warning -Message "Failed to uninstall: [$($_.Name)]"}
    }
    
    # Go to the next function
    Step4
}

# Remove HP Win32 Apps
function Step4 {
    foreach ($app in $apps) {
        $id = $app.IdentifyingNumber
        msiexec /uninstall "$id" /quiet /log $msilog /norestart
    }

    # Go to next function
    Step5
}

# Remove HP Connection Optimizer
function Step5 {
    if ($HPCommRecoveryPresent) {
    $optimizerUninstallAnswer | Out-File $env:TEMP\optimizer.iss
    $arguments = "/s /f1`"$env:Temp\optimizer.iss`" /f2`"C:\Temp\Uninstall.log`""
    Start-Process "C:\Program Files (x86)\InstallShield Installation Information\{6468C4A5-E47E-405F-B675-A70A70983EA6}\Setup.exe" -ArgumentList $arguments -PassThru -Wait
    }

    #Go to next function
    Step6
}

# Remove HP Documentation
function Step6 {
#Remove HP Documentation
    if (Test-Path "${Env:ProgramFiles}\HP\Documentation\Doc_uninstall.cmd" -PathType Leaf) {
        try {
            Invoke-Item "${Env:ProgramFiles}\HP\Documentation\Doc_uninstall.cmd"
            Write-Host "Successfully removed provisioned package: HP Documentation"
        }
        catch {
            Write-Host "Error Remvoving HP Documentation $($_.Exception.Message)"
        }
    }
    else {
        Write-Host "HP Documentation is not installed"
    }

        # Go to next function
        Step7
}

# Remove HP Active Support
function Step7 {
    if (Test-Path -Path "HKLM:\Software\WOW6432Node\Hewlett-Packard\HPActiveSupport") {
        try {
            Remove-Item -Path "HKLM:\Software\WOW6432Node\Hewlett-Packard\HPActiveSupport"
            Write-Host "HP Support Assistant regkey deleted $($_.Exception.Message)"
        }
        catch {
            Write-Host "Error retreiving registry key for HP Support Assistant: $($_.Exception.Message)"
        }
    }
    else {
        Write-Host "HP Support Assistant regkey not found"
    }

    if (Test-Path $HPSAuninstall -PathType Leaf) {
        try {
            & $HPSAuninstall /s /v/qn UninstallKeepPreferences=FALSE
            Write-Host "Successfully removed provisioned package: HP Support Assistant silently"
        }
        catch {
            Write-Host "Error uninstalling HP Support Assistant: $($_.Exception.Message)"
        }
    }
    else {
        Write-Host "HP Support Assistant Uninstaller not found"
    }
    # Go to next function
    Step8
}

# Check is apps are still present
function Step8 {
    $apps = Get-WmiObject -Class Win32_Product | Where-Object {$_.Name -match "HP"}
    if ($apps) {
        #Try to remove apps that are still present
        foreach ($app in $apps) {
            $id = $app.IdentifyingNumber
            msiexec /uninstall "$id" /quiet /log $msilog /norestart
        }
    } 
}

# Start with the first function
Step1
