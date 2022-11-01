import requests
import os
from databricks_cli.workspace.api import WorkspaceApi
from databricks_cli.sdk.api_client import ApiClient


create_folder = requests.post(
  '{}/api/2.0/workspace/mkdirs'.format('https://dbc-9d651f90-75ea.cloud.databricks.com'),
  headers={'Authorization': 'Bearer {}'.format(os.environ.get('TOKEN'))},
  json={"path": "/DevENV"}
)
 
print(create_folder.status_code) 

client = ApiClient(
    host='https://dbc-9d651f90-75ea.cloud.databricks.com',
    token=os.environ.get('TOKEN')
)

workspace_api = WorkspaceApi(client)  
workspace_api.import_workspace_dir(  
    source_path="notebooks/MyProject",
    target_path="/DevENV",
    overwrite="True",
    exclude_hidden_files="True"
)

# For Individual File API calls--Final
# workspace_api = WorkspaceApi(client)
# workspace_api.import_workspace(
#     source_path="my_file.py",
#     target_path="/Shared/Test/a.py",
#     language="PYTHON",
#     fmt='SOURCE',
#     is_overwrite='True'
# )
