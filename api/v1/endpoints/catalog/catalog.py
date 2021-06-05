from typing import Any, List, Optional
from fastapi import APIRouter, HTTPException, Path, Query, Body, Request
from fastapi.openapi.utils import get_openapi
from ...schemas.router import catalog as routerSchemas
from pprint import pprint
router = APIRouter()


@router.get('/', response_model=routerSchemas.Catalog_Items_Response)
def list_catalog_items(request: Request) -> Any:
    """
    Returns the names of all available catalog items
    """
    result = []
    for route in request.app.routes:
        if hasattr(route, "tags"):
            firstTag = route.tags[0]
            if firstTag not in result and firstTag != "Catalog":
                result.append(firstTag)
    return {'catalogs': result}


@router.get('/{catalogName}/automations', response_model=routerSchemas.Automation_Items_Response)
def list_automations_for_specified_catalog(
    request: Request,
    catalogName: str = Path(..., description="Catalog Name")
) -> Any:
    """
    Returns the list of all available automations for the specified catalog name
    """
    result = []
    for route in request.app.routes:
        if hasattr(route, "tags"):
            if route.tags[0] == catalogName:
                result.append(route.name)
    return {'catalog': catalogName,
            'automations': result
            }


@router.get('/{catalogName}/automations/{automationName}', response_model=routerSchemas.Automation_Detail_Response)
def get_automation_request_detail(
    request: Request,
    catalogName: str = Path(..., description="Catalog Name"),
    automationName: str = Path(..., description="Automation Name")
) -> Any:
    """
    Returns required information to invoke the specified automation
    """
    result = {}
    for route in request.app.routes:
        if hasattr(route, "tags"):
            if route.tags[0] == catalogName and route.name == automationName:
                request_body = {}
                result["catalog"] = catalogName
                result["automation"] = automationName
                result["body_required"] = False
                if(hasattr(route.body_field, "type_")):
                    result["body_required"] = True
                    for body_param in route.body_field.type_.__fields__.keys():
                        request_body[body_param] = ""
                result["url"] = route.path
                result["method"] = next(iter(route.methods))
                result["description"] = route.description
                result["request_body"] = request_body
                result["documentation"] = f"/redoc#operation/{automationName}{result['url'].replace('/','_').replace('{','_').replace('}','_')}_{result['method'].lower()}"
    pprint(result)
    return result
