#Christopher Ivan Malerva cruz Consulta:https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/09-functions?view=powershell-7.2 
function Show-Menu
     {
          param (
                [string]$Title = 'Escoge la funcion'
          )
          cls
          Write-Host "================ $Title ================"
            
       Write-Host "1: Presione '1' para Ver-StatusPerfil"
       Write-Host "2: Presione '2' para Ver-PerfilRedActual"
       
          
       Write-Host "Q: Presione 'Q' para salir."
     }
        
     
        
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
        
 
     
     do
     {
          Show-Menu
          $input = Read-Host "Escoge la funcion"
          switch ($input)
          {
                '1' {
                     cls
                     Ver-StatusPerfil
                } '2' {
                     cls
                     Ver-PerfilRedActual

                } 'q' {
                     return
                }
          }
          pause
     }
     until ($input -eq 'q')