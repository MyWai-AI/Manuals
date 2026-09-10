# HTTP API polling Adapter

The HTTP API polling Adapter can be used to periodically perform an HTTP(S) call to an external service to gather the data, and it also supports the RTSP video stream protocol.

The adapter must be configured with the following information:

* **URL**: the URL to be called.
* **Request type**: GET or POST.
* **Polling interval**: milliseconds between each request.
* **Optional authentication**: only the BASIC authentication method is supported, by entering username and password.

The following mime-types are expected for the different measure types:

| Measure field type | Mime-type                              |
| ------------------ | -------------------------------------- |
| Image              | image/\*                               |
| Video              | video/\*                               |
| Audio              | audio/\*                               |
| Numeric values     | text/plain, application/json, text/csv |

In case of text data for numeric values, the payload of the response is processed with the following regular expression:

`-?\d+(.\d+)?`

and each matching value is assigned, in order, to the measure field(s).

{% hint style="warning" %}
The adapter can read multiple numeric field with the same request (for example, x-y-z acceleration triplets of floating point values) but cannot process multiple multimedia files. In the case the sensor is associated to multiple measures, the system maps the response payload data to the first compatibile field.
{% endhint %}
