function Ver-StatusPerfil{  

param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil)  

$status = Get-NetFirewallProfile -Name $perfil  

Write-Host "Perfil:" $perfil  

if($status.enabled){  

Write-Host "Status: Activado"  

} else{  

Write-Host "Status: Desactivado"  

}  

}  




function Ver-PerfilRedActual{  

$perfilRed = Get-NetConnectionProfile  

Write-Host "Nombre de red:" $perfilRed.Name  

Write-Host "Perfil de red:" $perfilRed.NetworkCategory  

}  