from fastapi import APIRouter
from api.v1.endpoints.monitoring import healthCheck
from api.v1.endpoints.catalog import catalog

api_router = APIRouter()

api_router.include_router(healthCheck.router, prefix="/monitoring", tags=["Monitoring"])
api_router.include_router(catalog.router, prefix="/catalog", tags=["Catalog"])