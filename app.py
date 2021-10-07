from flask import Flask, request, render_template, redirect
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import os
app=Flask(__name__)

#connect_str = "DefaultEndpointsProtocol=https;AccountName=backupdiag836;AccountKey=fX2tmlyH+Web0GbBCY+Y1BrUhb8nsa6ltFelcPaYnccTzDXLYpX7PxJQUHI9+f06SQF0xZeMgKiQnAwXQCxWZA==;EndpointSuffix=core.windows.net"
connect_str = os.environ.get('connect_str','')


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/blobstorage', methods=['GET','POST'])
def blobstorage():

    # Create the BlobServiceClient object which will be used to create a container client
    if connect_str != "":
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # Create a unique name for the container
    #container_name = "demo1092933"
    # Create the container
    #container_client = blob_service_client.create_container(container_name)
    if request.method == "POST":
        if request.files:
            image = request.files['image']
            print (image.filename)
            # Create a blob client using the local file name as the name for the blob
            blob_client = blob_service_client.get_blob_client(container="demo1092933", blob=image.filename)
            # Upload the created file
            blob_client.upload_blob(image)
            
            return redirect(request.url)

    if connect_str != "":
        container_client = blob_service_client.get_container_client("demo1092933")
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
    return render_template("blob.html", files = t)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)