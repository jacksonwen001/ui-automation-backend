import datetime
from typing import Annotated
from fastapi import APIRouter, Depends
from models.project import Project
from routers import get_db

from schemas.project import CreateProjectRequest, QueryProjectRequest, ProjectResponse, QueryProjectsResponse, UpdateProjectrequest
from service import project_service
from sqlalchemy.orm import Session

router = APIRouter(tags=['projects'], prefix='/projects')

@router.post('')
async def create(*, request: CreateProjectRequest, db: Session = Depends(get_db)) -> ProjectResponse:
    return project_service.create(db, request) 

@router.get('')
async def query(*, request: Annotated[QueryProjectRequest, Depends()], db: Session = Depends(get_db)) -> QueryProjectsResponse: 
    response = project_service.query(db, request.name, request.current, request.size)
    return response; 

@router.get('/{project_id}')
async def get(*, project_id: str, db: Session = Depends(get_db)) -> ProjectResponse: 
    project: Project = project_service.get(db, project_id=project_id)
    return ProjectResponse(id=project.id, name=project.name, created_at=project.created_at)

@router.put('/{project_id}')
async def get(*, project_id: str, request: UpdateProjectrequest, db: Session = Depends(get_db)) -> ProjectResponse: 
    return project_service.update(db, project_id=project_id,  name=request.name)

@router.delete('/{project_id}')
async def delete(*, project_id: str, db: Session = Depends(get_db)): 
    project_service.delete(db, project_id=project_id)