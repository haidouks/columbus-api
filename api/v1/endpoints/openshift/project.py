from typing import Any, List, Optional
from fastapi import APIRouter, HTTPException, Body, Request
from ...schemas.router import openshift as routerSchemas
from lib.k8s.k8s import kubernetes

router = APIRouter()
k8s = kubernetes()


@router.get("/projects")
def get_openshift_projects():
  return k8s.getNamespaces()


@router.put("/projects")
def create_new_openshift_project(
    projectName: str = Body(..., description="Name of project")):
  return k8s.newNamespace(namespace=projectName)
