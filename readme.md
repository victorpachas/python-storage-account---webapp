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
2. Asignar el permiso de Storage Blob Data Contributor a la identidad generada por el webapp sobre el storage account.
3. Modificar el archivo app.py, y comentar toda la sección de Storage Account key access.
4. Descomentar la sección Storage account Managed identity Access
5. Cambiar el valor <storageaccountname> por el nombre del storage account
6. Con el comando az webapp up desplegar el aplicativo en el webapp
```bash
az webapp up -n <webapp name> -g <resource-group name>
```

## Prueba 3: Acceso del webapp con user managed identity
1. Eliminar el servicio creado en la prueba anterior, con ello tambien se elimina la identidad
2. Crear el user managed identity en el portal de azure
3. Modificar el archivo app.py, y comentar toda la sección de Storage account Managed identity Access.
4. Descomentar la sección Storage account User Managed identity Access. Reemplazar el valor <client id> por el client id del user managed identity. Cambiar el valor <storageaccountname> por el nombre del storage account
5. Con el comando az webapp up desplegar el aplicativo en el webapp
```bash
az webapp up -n <webapp name> -g <resource-group name>
```
6. Asociar el user managed identity creado en el paso anterior y asociarlo al webapp

