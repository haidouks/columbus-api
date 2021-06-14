from pydantic import BaseModel
from typing import List, Optional

class Openshift_Metadata_Info(BaseModel):
    name: str
    uid: str

class Openshift_Metadata(BaseModel):
    metadata: Openshift_Metadata_Info
    status: dict

class Openshift_Project_List(BaseModel):
    items: List[Openshift_Metadata]