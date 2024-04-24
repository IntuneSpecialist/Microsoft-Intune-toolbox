$Array = New-Object System.Collections.ArrayList
$path = "C:\temp\devices.csv"
$content = Import-Csv -Path $path -Delimiter ";"

Connect-AzureAD
$getDevice = Get-AzureADDevice -All $true | Select-Object ApproximateLastLogonTimeStamp, objectid, deviceid

foreach ($device in $content) {
$item = $getDevice | Where-Object { $_.DisplayName -eq $device.name }
$Array.Add($item.ObjectId)
}

# $Array | set-clipboard

Disconnect-AzureAD