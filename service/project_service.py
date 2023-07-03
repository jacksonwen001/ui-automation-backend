from typing import List
import uuid
from fastapi import HTTPException
from models.project import Project
from sqlalchemy.orm import Session

from schemas.project import CreateProjectRequest, ProjectResponse, QueryProjectsResponse

def query(db: Session, name: str = None, current: int = 1, size: int = 10) -> QueryProjectsResponse:
    if (name):
        return db.query(Project).filter(Project.name.contains(name)).order_by(Project.created_at).limit(size).offset((current - 1) * size)
    
    projects = db.query(Project).order_by(Project.created_at).limit(size).offset((current - 1) * size)
    
    return QueryProjectsResponse(
        total = projects.count(), 
        projects = [ProjectResponse(id = p.id, name = p.name, created_at = p.created_at) for p in projects]
    )

def create(db: Session, request: CreateProjectRequest) -> ProjectResponse:
    project = Project(id=str(uuid.uuid4()), name=request.name) 
    db.add(project)
    db.commit()
    return ProjectResponse(id=project.id, name=project.name, created_at=project.created_at)

def get(db: Session, project_id: str) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project: raise HTTPException(status_code=404, detail="project not found! id={}".format(project_id))
    return project

def update(db: Session, project_id: str, name: str) -> None:
    project = get(db, project_id=project_id)
    project.name = name; 
    db.add(project)
    db.commit()
    db.refresh(project)
    return ProjectResponse(id=project.id, name=project.name, created_at=project.created_at)

def delete(db: Session, project_id: str) -> None:
    project = get(db, project_id)
    db.delete(project)
    db.commit()