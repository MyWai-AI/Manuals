# Reduce Algorithms container size

The default AI Algorithms container includes all built-in algorithms available on the platform. As a result, the **Docker image can be quite large** (on the order of tens of gigabytes), which may be unsuitable for some Edge devices. However, in most typical scenarios, these standard algorithms are not needed on the Edge side, since custom algorithms are often developed and deployed instead.

If you do require one or more _built-in_ algorithms on an Edge device and are experiencing issues with the resulting Docker image size, please contact us. We can provide a dedicated container image that includes only the algorithms you need, so with a lower size.
