from typing import Any, List, Optional
from fastapi import APIRouter, HTTPException, Path, Query, Body, Request
from ...schemas.router import schemas as routerSchemas

router = APIRouter()


@router.get("/projects", response_model=routerSchemas.Monitoring_HealthCheck)
def get_openshift_projects() -> Any:
    """
    this operation returns dummy response
    """
    status = {
        "db": "healthy",
        "ceph": "healthy"
    }
    return status