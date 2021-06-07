from fastapi import APIRouter
from api.v1.endpoints.monitoring import healthCheck
from api.v1.endpoints.catalog import catalog
from api.v1.endpoints.openshift import project, user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/openshift", tags=["Openshift"])
api_router.include_router(project.router, prefix="/openshift", tags=["Openshift"])
api_router.include_router(healthCheck.router, prefix="/monitoring", tags=["Monitoring"])
api_router.include_router(catalog.router, prefix="/catalog", tags=["Catalog"])