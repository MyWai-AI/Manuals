# Marketplace Tools

{% hint style="warning" %}
This is a preliminary documentation and it is subject to change. The Marketplace Tools functionality will be available in a future release of the Platform.
{% endhint %}

A Marketplace Tool is designed to augment the capabilities of the MYWAI Platform, offering users a powerful extension to interact with and enrich their data. This specialized tool enables the creation of custom user interfaces (UIs) tailored to perform specific tasks, significantly improving workflow efficiency and data interaction. Key functionalities provided by the Marketplace Tool include:

* **Interactive Data Enrichment**: Users can dynamically introduce new information to augment existing data sets. This feature supports a wide range of data types, including textual facts, images, and other multimedia resources, facilitating a comprehensive data enhancement process.
* **Custom Label Definition**: With the Marketplace Tool, defining labels for data categorization becomes more flexible and intuitive. Users can tailor label creation to suit their specific project needs, employing semi-automated processes to streamline the labeling workflow. This capability is particularly beneficial for machine learning and data analysis projects requiring precise and customized data categorization.
* **Data Transformation Launchpad**: The tool serves as a gateway to initiate and manage data transformation tools. Users can leverage this feature to perform complex data manipulations, conversions, and processing tasks, enhancing data quality and readiness for analysis or machine learning applications.

## Available Tools

A suite of tools is presently available, specifically crafted for particular project scenarios. These tools serve as examples of what this technology can achieve, though they may not be released for general availability.

* <mark style="background-color:yellow;">TODO: list existing tools and use cases</mark>

## Developing a Marketplace Tool

### Technology stack

A Marketplace Tool must be hosted externally to the MYW.AI Platform, akin to an independent website.

This approach ensures developers have the freedom to utilize any technology stack without limitations, facilitating the integration and reuse of existing open-source technologies.&#x20;

Optionally, packaging a tool as a Docker image will, in the future, simplify deploying the solution within the MYWAI Platform's cluster itself, eliminating the requirement for separate hosting.

### Interfacing with the Platform

The interface between MYW.AI and the Tool includes:

* **User Information Sharing**: Your tool will have access to interactive user information, enabling personalized and user-specific functionalities.
* **Data Access and Manipulation**: The tool is able to both read from and write to the MYW.AI data resources. This includes:
  * **Imports**: Accessing data that users have imported into the MYW.AI platform.
  * **DataSets**: Interacting with and manipulating DataSets within MYW.AI.
  * **Data Editing and Enrichment**: Your tool should offer functionalities to edit, transform, or enrich data, encompassing various formats such as images, videos, and textual facts.
* **Storage Access**: Developers will have access to dedicated Blob and SQL storage spaces for storing large binary objects and structured data, respectively. This feature supports the efficient handling and processing of data within your tool.
