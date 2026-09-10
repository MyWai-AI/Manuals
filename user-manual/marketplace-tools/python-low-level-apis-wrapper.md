# Python Low Level APIs Wrapper

In this guide, we will show how to use the Python wrapper for the MYWAI platform APIs. This wrapper allows for making API calls in a simple and intuitive way at a low level.



For this task, we used the library **pyswaggerapiwrap**, which you can find on [GitHub ](https://github.com/KlajdiBeqiraj/pyswaggerapiwrap)or [PyPI](https://pypi.org/project/pyswaggerapiwrap/).&#x20;

Python Version

The version of Python used for the package is Python 3.9.7, but there are no specific constraints on the Python version.



### Installation

You can install **PYSwaggerAPIWrap** using pip:

```bash
pip install pyswaggerapiwrap
```

### Complete Tutorial

For a complete tutorial of PySwaggerAPIWrap, please refer to the notebook available at this link: [Tutorial](https://github.com/KlajdiBeqiraj/PySwaggerAPIWrap/blob/main/notebooks/pyswaggerapi_tutorial.ipynb).&#x20;

For the complete guide on Mywai, everything can be found in the file test\_low\_level\_apis.ipynb within the Algorithms package.

### Http client

The following lines of code import the `HttpClient` class from the `PySwaggerAPIWrap.http_client` module and set up an HTTP client with a specific endpoint and authentication token.

```python
from pyswaggerapiwrap.http_client import HttpClient

ENDPOINT = "https://localhost:44330" # Route to MyWai Api's
AUTH_TOKEN = "yout Auth token"

http_client = HttpClient(base_url=ENDPOINT, auth_token=AUTH_TOKEN)

```

The http\_client module allows you to make classic HTTP **requests** using the requests library. It supports both POST and GET methods for interacting with web services.

Using this class, we can retrieve a pandas DataFrame containing all the information from the Swagger documentation with the following method:

```python
routes_dict = http_client.get_routes_df(swagger_route="swagger/v1/swagger.json")
```



<figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

Additional API's

To make life easier, the possibility to add 'additional' APIs has been added, meaning APIs available in the library but with fixed parameters. This is useful in the case of page-based APIs, meaning APIs that need to be called for a specific scenario.

For the platform, we need two specific APIs, which are:

1. Get the list of datasets
2. Get every fact associated with a certain version

Below, we will show how to create the two additional APIs and how to add them to the existing ones. First, let's create them:

```python
AdditionalAPISContainer.add_additional_api(
    new_api=AdditionalAPI(
        original_route="/Dataset/get/DatasetsPagedByProjectId/{page}/{pageSize}/{sort}/{search}/{projectId}",
        method="GET",
        fixed_route_params=dict(
            page=1,
            pageSize=-1,
            sort="empty",
            search="empty"
        )
    ), 
    name="getDatasetList"
)

AdditionalAPISContainer.add_additional_api(
    new_api=AdditionalAPI(
        original_route='/QualityControlLabelledFact/LabelledFactVersioningFilteredPagedByVersion/{page}/{pageSize}/{'
                       'sort}/{search}/{versionId}',
        method="POST",
        fixed_route_params=dict(
            page=1,
            pageSize=-1,
            sort="empty",
            search="empty"
        )
    ), 
    name="getFactsWithVersionID"
)
AdditionalAPISContainer.ADDITIONAL_APIS
```

At this point, let's add them to the existing ones:

```python
from pyswaggerapiwrap.utils import add_additional_apis_to_df

routes_dict = add_additional_apis_to_df(routes_dict)

```

### API DataFrame Filter

Through the API filter class, we can wrap this dictionary to navigate through all the APIs and find the one we are interested in.

First, we create the object by passing the DataFrame as follows:

```python
from pyswaggerapiwrap.api_filter import APIDataFrameFilter

api_filter = APIDataFrameFilter(routes_dict)
```

#### filter method

We can use the **filter method** to filter our APIs in several ways:

1. **By api\_type**: In this case, the APIs are divided based on the first key. For example, in the APIs from the notebook (“https://petstore.swagger.io/v2”), we have pet, user, and store.
2. **By route\_pattern**: This allows us to retrieve all APIs that contain the specified string within their route.
3. **By method**: We can filter by HTTP methods such as GET and POST.



```python
api_filter.filter(api_type="Dataset", route_pattern="/Dataset/get/DatasetsPagedByProjectId/")
```

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

#### Api as attributes

Additionally, the api\_filter class dynamically allows the indexing of APIs, where various APIs are assigned through a tree structure within the object. This means we can access:

```python
api_filter.Dataset
```

and we will have all the APIs with api\_type equal to Dataset. Furthermore, we can index the APIs directly as attributes. In this case, the actual API names are modified to comply with class attribute rules. To understand, let’s show an example:

The API located at the route "Dataset/get\_DatasetsPagedByProjectId" and of type GET can be accessed with the following command:

```python
api_filter.Dataset.get_DatasetsPagedByProjectId
```

The API names follow these rules:

1. They start with the method: get, post, etc.
2. Slashes / are replaced with underscores \_.
3. Attributes such as {id} are replaced with with\_\_Id.

### Run API

To call an API once we have identified the one we are interested in, we simply call the run method. This method dynamically takes both path and query parameters as inputs.

To understand, let’s show two examples:

**1. Get Projects:** method=GET, route="/Project/get/ProjectFullList"

```python
project_api = api_filter.get_api(route="/Project/get/ProjectFullList", method="GET")

result = project_api.run(http_client)
print(result)

```

```json
[{'id': 1,
  'name': 'Damiano Project',
  'description': None,
  'isDeleted': False,
  'datasets': [{'id': 1,
    'projectId': 1,
    'projectName': 'Damiano Project',
    'name': 'Damiano Dataset',
    'description': None,
    'totalFacts': 0,
    'isDeleted': False,
    'factType': 1,
    'datasetVersions': [{'id': 1,
      'versionNumber': 0,
      'datasetId': 1,
      'datasetName': 'Damiano Dataset',
      'projectName': 'Damiano Project',
      'projectId': '1',
      'numberOfFacts': 0,
      'description': 'Damiano Version',
      'parentVersionId': None,
      'hasClones': False,
      'wasTrained': False,
      'isDeleted': False}]}]},
 {'id': 2,
...
      'description': 'base',
      'parentVersionId': None,
      'hasClones': False,
      'wasTrained': False,
      'isDeleted': False}]}]}]
```

**2. Get DatasetVersion:** method=GET, route="/DatasetVersion/getDatasetVersionByDatasetId/{id}"

```python
get_dataset_version_from_dataset_id = api_filter.DatasetVersion.getDatasetVersionByDatasetId

results = get_dataset_version_from_dataset_id.run(http_client, id=dataset.id)

print(results)
```

```json
[{'id': 2,
  'versionNumber': 0,
  'datasetId': 2,
  'datasetName': 'Genaware dataset',
  'projectName': None,
  'projectId': '0',
  'numberOfFacts': 8,
  'description': 'base',
  'parentVersionId': None,
  'hasClones': False,
  'wasTrained': False,
  'isDeleted': False,
  'dataset': {'id': 2,
   'projectId': 2,
   'projectName': None,
   'name': 'Genaware dataset',
   'description': None,
   'totalFacts': 8,
   'isDeleted': False,
   'factType': 0,
   'datasetVersions': []}}]


```

## Save and reload the status

**PySwaggerAPIWrap** allows you to save the state of the package so that you don't have to wrap the documentation from the swagger each time but load it from file directly. Of course, if the API state changes, you will have to save the updated state again.

#### Example of Use

Below you will find an explanation of how to do it (find the same example in the notebook called `status_save_and_reload`).

First, let's go configure the variables as done in the previous tutorial:

```python
http_client = HttpClient(base_url=ENDPOINT, auth_token=AUTH_TOKEN)
routes_dict = http_client.get_routes_df(swagger_route="/swagger.json")

api_filter = APIDataFrameFilter(routes_dict)
```

Save the status

```python
from pyswaggerapiwrap.status import Status, save_status, load_status

file_path = os.path.join("resources", "saved_data", "status.psw")
save_status(file_path, http_client=http_client, routes_dict=routes_dict)

```

Similarly, we can reload status in this way:

```python
new_api_filter, new_http_client = load_status(file_path)
```

### Download Facts

To provide a more concrete example, let's show how to download all the facts of a DatasetVersion.



1. Get Blob storage dict from the specific API

```python
get_blobl_configuration_api = api_filter.get_api(route="/Marketplace/blobConfiguration", method="GET")

blob_storage_configuration_dict = get_blobl_configuration_api.run(http_client)

# Define python object from api result
blob_storage_configuration = BlobStorageConfiguration.from_dict(
    blob_storage_configuration_dict
)

```

2. Configuration manager

```python
from mywai_python_backend.json2data.azure.configuration_manager import (
    ConfigurationManager,
)
config_manager = ConfigurationManager(
    blob_storage_configuration=blob_storage_configuration,
    logger=None,
    timescale_connection_string=None
)
```

3. Get all facts by DatasetVersionId&#x20;

```python
get_facts_with_version_id_api = api_filter.get_additional_api(key="getFactsWithVersionID")
data = get_facts_with_version_id_api.run(http_client, versionId=2)

# parse api result to pyton object 
from mywai_python_backend.data.facts import parse_facts

facts_obj = parse_facts(data["items"])
```

4. Download all facts usign Facts class

```python
facts_obj.download(config_manager)
```

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>
