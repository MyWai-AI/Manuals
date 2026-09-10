# Edge Installation on Windows with Docker Compose

1\. Create the following empty folders on the C: drive:

* C:\EdgeIO
* C:\EdgeStorage

2\. Download, install and run **Docker Desktop** ([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/))

3\. Open a **command prompt**.

4\. If not already created installing a GDS, create the _mywai_ network:

```shellscript
docker network create -d bridge --subnet=192.168.5.0/24 mywai
```

5\. Login into _mywaik8sfeature_ docker registry:

{% code overflow="wrap" %}
```shellscript
docker login -u mywai-pull -p <token> productfeatures.azurecr.io
```
{% endcode %}

{% hint style="warning" %}
Contact MYWAI to get the access token for the proper registry.\
The registry mywaik8sfeature.azurecr.io provides a more stable version of the Edge but not the very last one available. If you need the more up-to-date version, ask MYWAI for the access to the mywaik8snextdev.azurecr.io registry.
{% endhint %}

6\. Create a file `.env` in the folder `C:\EdgeStorage` where you will define the following environment variables as described below:

```
MYWAI_EDGE_ID=<value>
MYWAI_TENANT_NAME=<value>
MYWAI_GDS_PASSWORD=<value>
```

* `MYWAI_EDGE_ID`: an alphanumeric name you can choose for your Edge.
* `MYWAI_TENANT_NAME`: is the tenant name of your cloud MYWAI Platform. For example, if your platform is accessible at the url **https://acme.platform.myw.ai**, your tenant name is "acme".
* `MYWAI_GDS_PASSWORD`: the password configured on the GDS.

7. Create a file `docker-compose.yml` in the folder `C:\EdgeStorage` with the following content:

{% code overflow="wrap" %}
```yml
name: mywai

services:
  mywai-edge:
    image: productfeatures.azurecr.io/edge:latest
    container_name: mywai-edge
    restart: always
    networks:
      mywai:
        ipv4_address: 192.168.5.3
    volumes:
      - C:\EdgeIO:/EdgeIO
      - C:\EdgeStorage:/EdgeStorage
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      IotHub__EdgeId: Edge-${MYWAI_EDGE_ID}
      IotHub__TenantName: ${MYWAI_TENANT_NAME}
      GDS__Password: ${MYWAI_GDS_PASSWORD}

networks:
  mywai:
    external: true
```
{% endcode %}

{% hint style="info" %}
192.168.5.3 is the predefined internal IP address for the Edge. You need to change it in case you are installing for some reasons more Edges on the same Docker.
{% endhint %}

8. Run the following command from the folder `C:\EdgeStorage`:

```shellscript
docker compose up -d
```
