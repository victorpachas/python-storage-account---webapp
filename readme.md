# Introduction
El repositorio tiene un ejemplo de como es posible conectarnos desde un webapp y un app hecho en python hacia un storage account utilizando key del storage, managed identity and user managed identity

# Requerimientos previos

Storage account aprovisionado con un container de nombre imagenes

# Pasos para las pruebas
## Prueba 1: Acceso del webapp al storage con keys
1. Primero desde el cloudshell hacer la descarga de los archivos de este repositorio
2. Modificar el archivo app.py, y en la variable connect_str reemplazar el valor, por el obtenido de la opción de keys del storage account.
3. Con el comando az webapp up desplegar el aplicativo en el webapp. Este comando de no existir el webapp o service plan, lo crea de forma automatica
```bash
az webapp up -n <webapp name> -g <resource-group name>
```
## Prueba 2: Acceso del webapp con system managed identity
1. Activar el managed identity en el app service creado en el paso anterior
2. Modificar el archivo app.py, y comentar toda la sección de Storage Account key access.
3. Descomentar la sección Storage account Managed identity Access
4. Con el comando az webapp up desplegar el aplicativo en el webapp
```bash
az webapp up -n <webapp name> -g <resource-group name>
```
## Prueba 3: Acceso del webapp con user managed identity
1. Eliminar el servicio creado en la prueba anterior, con ello tambien se elimina la identidad
2. Crear el webapp con el siguiente comando
```bash
az appservice plan create -g <rg-name> -n <service-plan name> --is-linux 
az webapp create -g <rg-name> -p <service-plan name> -n <web-app name> --runtime "PYTHON:3.7"
```
3. Crear el user managed identity en el portal de azure y asociarlo al webapp creado en el paso anterior
4. Modificar el archivo app.py, y comentar toda la sección de Storage account Managed identity Access.
5. Descomentar la sección Storage account User Managed identity Access. Adicional a ello reemplazar el valor <client id> por el client id del user managed identity
6. Con el comando az webapp up desplegar el aplicativo en el webapp
```bash
az webapp up -n <webapp name> -g <resource-group name>
```


