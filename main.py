from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from starlette_prometheus import metrics, PrometheusMiddleware

from api.v1.api import api_router


tags_metadata = [
  {
      "name": "Virtualization",
      "description": "Operations related to Virtualization Category",
  },
  {
      "name": "Openshift",
      "description": "Operations related to Openshift",
  },
  {
      "name": "Storage",
      "description": "Operations related to Storage",
  },
  {
      "name": "Monitoring",
      "description": "Operations related to Storage",
  },
  {
      "name": "Catalog",
      "description": "Discover Turkcell's Automation Operations Catalog",
  },
]

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="IaC-API", 
        version="1.0.0",
        description="Turkcell Infrastructure as Code API",  
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://s.turkcell.com.tr/SiteAssets/Hakkimizda/genel-bakis/logolarimiz/TURKCELL_DIKEY_ERKEK_LOGO.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI(
    openapi_url=f"/api/v1/openapi.json",
    openapi_tags=tags_metadata,
)
app.openapi = custom_openapi

app.add_middleware(PrometheusMiddleware)
app.add_route("/api/v1/monitoring/metrics", metrics)
app.include_router(api_router, prefix="/api/v1")
