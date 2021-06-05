from pydantic import BaseModel, Field
from typing import List, Optional, Any

class Catalog_Items_Response(BaseModel):
    catalogs: List[str] = Field(..., description="List of catalog items", example=["openshift", "virtualization", "storage", "..."])

class Automation_Items_Response(BaseModel):
    catalog: str = Field(..., description="Catalog item", example="openshift")
    automations: List[str] = Field(..., description="Automation list for specified catalog", example=['new_project', 'new_user', 'set_quota', '...'])

class Automation_Detail_Response(BaseModel):
    catalog: str = Field(..., description="Catalog item", example="openshift")
    automation: str = Field(..., description="Automation name", example="new_project")
    body_required: str = Field(..., description="Requirment flag for body. If false, no need to send body with request", example="True")
    url: str = Field(..., description="Url for invoking automation", example="http://../api/v1/openshift/new_project")
    method: str = Field(..., description="Http method for invoking automation", example="POST")
    description: str = Field(..., description="Description about automation", example="This automation aims to ...")
    request_body: Any = Field(..., description="Request body for invoking automation", example={'param1':'value1', 'param2':'value2'})
    documentation: str = Field(..., description="Documentation URL for specified automation", example="http://../documentation/openshift/new_project")

