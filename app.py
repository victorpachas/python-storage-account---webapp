from flask import Flask, request, render_template, redirect
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
#from azure.identity import DefaultAzureCredential
import os
app=Flask(__name__)


##Storage Account key access
connect_str = "DefaultEndpointsProtocol=https;AccountName=storageweb123;AccountKey=86Y975cXnwojUoxe6T/jdBQhthxbpU3IBerUw0doKGHGLoOGqiHtJbyazPdqIbsVxY+EjRKyfQXQ+AStCbng8g==;EndpointSuffix=core.windows.net"
#connect_str = os.environ.get('connect_str','')
# Create the BlobServiceClient object which will be used to create a container client
if connect_str != "":
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)


##Storage account Managed identity Access
#account_url = "https://<storageaccountname>.blob.core.windows.net"
#connect_str = DefaultAzureCredential()
#if connect_str != "":
#    blob_service_client = BlobServiceClient(account_url, credential=connect_str)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/blobstorage', methods=['GET','POST'])
def blobstorage():
    if request.method == "POST":
        if request.files:
            image = request.files['image']
            print (image.filename)
            # Create a blob client using the local file name as the name for the blob
            blob_client = blob_service_client.get_blob_client(container="imagenes", blob=image.filename)
            # Upload the created file
            blob_client.upload_blob(image)
            
            return redirect(request.url)

    if connect_str != "":
        container_client = blob_service_client.get_container_client("imagenes")
        list_blob=[]
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            #print("\t" + blob.name)
            list_blob.append((blob.name, blob.size))
        t=tuple(list_blob)
    else :
        list_blob=[]
        list_blob.append(('No se ha creado la variable de entorno connect_str',''))
        t=tuple(list_blob)
    print (t)
    return render_template("blob.html", files = t, connect_str = connect_str)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)