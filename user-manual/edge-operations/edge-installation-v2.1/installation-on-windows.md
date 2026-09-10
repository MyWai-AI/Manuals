# Installation on Windows

1\. Create the following empty folders on the C: drive:

1. C:\EdgeIO
2. C:\EdgeStorage

2\. (Only for installations without GDS) Login in the MYWAI platform, go to the Edges pages and find the Edge you want to install. If you have no Edges listed in the page, create a new Edge and give it a proper name.\
On the Edge line, click on the "Edge Device Details" button (![](/broken/files/IdllMtyRqMU8PRPKWepZ)) on the right, then click on **Download Edge.env** and **Download Algo.env** buttons.\
Save the two downloaded files in the C:\EdgeStorage folder.

3\. Download and install **Docker Desktop** ([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/))

4\. Open a command prompt in the C:\EdgeStorage folder.

5\. Create the _mywai_ network:

```bash
docker network create -d bridge --subnet=192.168.5.0/24 mywai
```

6\. Login into _mywai_ docker registry:

{% code overflow="wrap" %}
```bash
docker login -u mywai-pull -p <token> mywai.azurecr.io
```
{% endcode %}

{% hint style="warning" %}
Contact MYWAI to get the access token for the proper registry.
{% endhint %}

7\. Download the latest version of the docker images:

```bash
docker pull mywai.azurecr.io/edge:latest
docker pull mywai.azurecr.io/algo:latest
```

8\. Create & Start the containers:

{% code overflow="wrap" %}
```bash
docker run --name mywai-edge --restart always --network mywai --ip 192.168.5.3 --env-file .\Edge.env -p 1883:1883 -p 8023:8023 -v C:\EdgeIO:/EdgeIO -v C:\EdgeStorage:/EdgeStorage -v /var/run/docker.sock:/var/run/docker.sock mywai.azurecr.io/edge:latest 

docker run --name mywai-algo --restart always --network mywai --ip 192.168.5.2 --env-file .\Algo.env -p 5005:5005 -p 8022:8022 -v C:\EdgeIO:/EdgeIO -v C:\EdgeStorage:/EdgeStorage mywai.azurecr.io/algo:latest
```
{% endcode %}



