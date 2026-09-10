# Edge Installation on Ubuntu

1\. Create the following empty folders on the root:

* /EdgeIO
* /EdgeStorage

2\. Install **Docker Engine** following the official Docker installation guide for Ubuntu:\
https://docs.docker.com/engine/install/ubuntu/

{% hint style="info" %}
Optionally consider to apply post-install settings for your Docker: [https://docs.docker.com/engine/install/linux-postinstall](https://docs.docker.com/engine/install/linux-postinstall). If you choose to use Docker as non-root user, omit "sudo" in all the following commands of this procedure.
{% endhint %}

3\. After installation, ensure Docker is running:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

4\. Create the `mywai` Docker network (if not already created by other MYWAI containers):

```batch
sudo docker network create -d bridge --subnet=192.168.5.0/24 mywai
```

5\. Log in to the MYWAI Docker registry:

{% code overflow="wrap" %}
```batch
sudo docker login -u mywai-pull -p <token> productfeatures.azurecr.io
```
{% endcode %}

{% hint style="warning" %}
Contact MYWAI to get the access token for the proper registry.\
The registry mywaik8sfeature.azurecr.io provides a more stable version of the Edge but not the very last one available. If you need the more up-to-date version, ask MYWAI for the access to the mywaik8snextdev.azurecr.io registry.
{% endhint %}

6\. Pull the latest version of the Edge image:

```batch
sudo docker pull mywaik8sfeature.azurecr.io/edge:latest
```

7\. Create & Start the containers:

<pre class="language-batch" data-overflow="wrap"><code class="lang-batch"><strong>sudo docker run --name mywai-edge --restart always --network mywai \
</strong>--ip 192.168.5.3 \
-v /EdgeIO:/EdgeIO \
-v /EdgeStorage:/EdgeStorage \
-v /var/run/docker.sock:/var/run/docker.sock \
-e IotHub__EdgeId=Edge-&#x3C;edge-id> \
-e IotHub__TenantName=&#x3C;tenant-name> \
-e GDS__Password=&#x3C;gds-password> \
productfeatures.azurecr.io/edge:latest
</code></pre>

Where:

* `192.168.5.3`: the IP address to be assigned to the Edge container. You need to change it in case you are installing for some reasons more Edges on the same Docker.
* `IotHub__EdgeId`: an alphanumeric name you can choose for your Edge. Must start with "Edge-".
* `IotHub__TenantName`: is the tenant name of your cloud MYWAI Platform. For example, if your platform is accessible at the url **https://acme.platform.myw.ai**, your tenant name is "acme".
* `GDS__Password`: the password configured on the GDS.

