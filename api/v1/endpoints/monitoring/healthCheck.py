from typing import Any, List, Optional
from fastapi import APIRouter, HTTPException, Path, Query, Body, Request
from ...schemas.router import schemas as routerSchemas

router = APIRouter()


@router.get("/status", response_model=routerSchemas.Monitoring_HealthCheck)
def get_prometheus_metrics() -> Any:
    """
    this operation returns dummy response
    """
    status = {
        "db": "healthy",
        "ceph": "healthy"
    }
    return status


@router.post("/message/{message}", response_model=routerSchemas.Monitoring_Message_Response)
def post_hello_message(
    reqBody: routerSchemas.Monitoring_Message_Request,
    message: str = Path(default=..., title="Message for your friend",
                        description="Your message description is here")):
    """
    Write your favorite message here
    * Think it
        * write it
        * like it
    """
    return {
        "message": message
    }
