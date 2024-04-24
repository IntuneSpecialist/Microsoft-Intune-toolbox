Connect-AzureAD

$array = New-Object System.Collections.ArrayList
$groupmembers = Get-AzureADGroupMember -ObjectId ""

foreach ($member in $groupmembers) {
    $usersDevices = Get-AzureADUserRegisteredDevice -ObjectId $member.ObjectId | Select-Object objectid, ismanaged
    foreach ($device in $usersDevices) {
        if ($device.ismanaged) {
            $array.Add($device.ObjectId)
        }
    }
}

# $Array | set-clipboard

Disconnect-AzureAD