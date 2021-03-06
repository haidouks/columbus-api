from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from starlette_prometheus import metrics, PrometheusMiddleware

from api.v1.api import api_router


tags_metadata = [
  {
      "name": "Virtualization",
      "description": "Automations related to Virtualization",
  },
  {
      "name": "Openshift",
      "description": "Automations related to Openshift",
  },
  {
      "name": "Storage",
      "description": "Automations related to Storage",
  },
  {
      "name": "Monitoring",
      "description": "Automations related to Storage",
  },
  {
      "name": "Catalog",
      "description": "Discover Turkcell's Automation Catalog",
  },
]

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Turkcell Columbus-API", 
        version="1.0.0",
        description="Columbus-API aims to connect any infrastructure automation to consumer in a standardized declarative way.",  
        routes=app.routes,
        tags=tags_metadata
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://s.turkcell.com.tr/SiteAssets/Hakkimizda/genel-bakis/logolarimiz/TURKCELL_DIKEY_ERKEK_LOGO.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI(
    openapi_url=f"/api/v1/openapi.json",
)
app.openapi = custom_openapi

app.add_middleware(PrometheusMiddleware)
app.add_route("/api/v1/monitoring/metrics", metrics)
app.include_router(api_router, prefix="/api/v1")
