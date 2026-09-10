# DataSets

DataSets provide a way to group collections of events or discrete assets (such as images, audio recordings, videos, or time series) for the purpose of training supervised or unsupervised AI algorithms.

To create a DataSet, you must first set up a dedicated Project. A single Project can contain multiple DataSets, each of which is versioned to track changes over time.&#x20;

A DataSet is defined by its **Name**, **Description**, the **Fact Type** of the items it contains (Event, Image, Audio, Video, or Time Series), and whether it is **Supervised** (requiring each item to have a label) or not.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

When a DataSet is initially created, a default version (version 0) is automatically generated. You can then populate this version through the **Data Repository** by selecting items and clicking **Assign to DataSet**.&#x20;

Once the DataSet version is ready, it can be used to run **training experiments** with a **compatible** algorithm. For Events—whose formats can vary significantly—a custom algorithm is often required.

As soon as you use a specific version of a DataSet for training, and as long as the resulting model remains on the platform (i.e., is not deleted), that version becomes **read-only**. To continue updating the DataSet, you must create a new version.

You can review and manage DataSets using a workflow similar to the one used for Labels.
