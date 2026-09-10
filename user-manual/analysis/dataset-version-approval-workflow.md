# Dataset version approval workflow

Each **dataset version** can undergo an **approval process**. This workflow allows one or more reviewers to validate a dataset version before it is used for model training.

You can access all datasets and their versions from the **Datasets** section in the navigation menu.\
\
![](<../.gitbook/assets/image (8).png>)

There are four distinguishable sections:

### **Datasets and versions**

This represents a collection of all the dataset. Navigating inside the Dataset you can find the different dataset versions created. On each version you can submit for for approval process by clicking on the ![](<../.gitbook/assets/image (11).png>) action button.

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

When opening the dialog, specify the "Description" field and enable users or roles responsible for reviewing. At the end of the process, a notification email will alert the specified users or members of the configured group.

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

### **Pending**

This section displays all dataset versions currently awaiting review.\
Both the requester and assigned reviewers can access the items in this list.

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

Clicking on the ![](<../.gitbook/assets/image (16).png>) action button, you can enter the approval section where you can review the dataset content and leave comment for the other reviewers.

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

### **Approved**

This section lists dataset versions whose approval workflows have been completed successfully.

Once the last reviewer completes the process and the requester finalizes it, the version appears here.\
Approved datasets are now eligible for use in training workflows.

### **Abandoned**

This list displays workflows that have not been approved by the reviewer. Abandoning a workflow does **not** remove the dataset version; it only terminates its active approval request.
