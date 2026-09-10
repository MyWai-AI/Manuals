# Edge Installation on Ubuntu with Docker Compose

1\. Create the following empty folders on the root:

* /EdgeIO
* /EdgeStorage

2\. Install **Docker Engine** following the official Docker installation guide for Ubuntu:\
https://docs.docker.com/engine/install/ubuntu/

{% hint style="info" %}
Optionally consider to apply post-install settings for your Docker: [https://docs.docker.com/engine/install/linux-postinstall](https://docs.docker.com/engine/install/linux-postinstall). If you choose to use Docker as non-root user, omit "sudo" in all the following commands of this procedure.
{% endhint %}

3\. After installation, ensure Docker is running:

```shellscript
sudo systemctl start docker
sudo systemctl enable docker
```

4\. Create the `mywai` Docker network (if not already created by other MYWAI containers):

```shellscript
sudo docker network create -d bridge --subnet=192.168.5.0/24 mywai
```

5\. Log in to the MYWAI Docker registry:

{% code overflow="wrap" %}
```shellscript
sudo docker login -u mywai-pull -p <token> productfeatures.azurecr.io
```
{% endcode %}

{% hint style="warning" %}
Contact MYWAI to get the access token for the proper registry.\
The registry mywaik8sfeature.azurecr.io provides a more stable version of the Edge but not the very last one available. If you need the more up-to-date version, ask MYWAI for the access to the mywaik8snextdev.azurecr.io registry.
{% endhint %}

6\. Create a file `.env` in the folder `/EdgeStorage` where you will define the following environment variables as described below:

```
MYWAI_EDGE_ID=<value>
MYWAI_TENANT_NAME=<value>
MYWAI_GDS_PASSWORD=<value>
```

* `MYWAI_EDGE_ID`: an alphanumeric name you can choose for your Edge.
* `MYWAI_TENANT_NAME`: is the tenant name of your cloud MYWAI Platform. For example, if your platform is accessible at the url **https://acme.platform.myw.ai**, your tenant name is "acme".
* `MYWAI_GDS_PASSWORD`: the password configured on the GDS.

7. Create a file `docker-compose.yml` in the folder `/EdgeStorage` with the following content:

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
      - /EdgeIO:/EdgeIO
      - /EdgeStorage:/EdgeStorage
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

8. Run the following command from the folder `/EdgeStorage`:

```shellscript
docker compose up -d
```

