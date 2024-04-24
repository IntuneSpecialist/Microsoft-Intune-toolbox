# Get network adapter information
$networkAdapters = Get-NetAdapter -Physical -InterfaceDescription "*8822*" | Select-Object Name, InterfaceDescription, DriverVersion, DriverDate, DriverProvider, MacAddress

# Check if any matching network adapters were found
if ($networkAdapters) {
    $neededversion = "2024.10.228.9"
    $neededversion = $neededversion -replace '\.', ''
    $neededversion = [long]$neededversion

    $actualdriver = $networkAdapters.DriverVersion
    $actualdriver = $actualdriver -replace '\.', ''
    $actualdriver = [long]$actualdriver

    if ($actualdriver -lt $neededversion) {
        Write-Host "Driver can be updated"
        exit 1
        }

    else {
        Write-Host "Driver already has been updated"
        exit 0
        }
} 

else {
    Write-Host "No network adapters matching the criteria were found."
    exit 0
}