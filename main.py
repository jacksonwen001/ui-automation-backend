from fastapi import FastAPI
import uvicorn
from config.celery_utils import create_celery
from routers import page, page_element, page_operation, page_step, project, scenario, scenario_operation, scenario_page, suite, task, universities, user
from sql_app import models
from sql_app.database import engine


app = FastAPI(
    title="UI Automation Testing", 
    description="ui automation with selenium + celery + mysql",
    version="0.0.1"
)

models.Base.metadata.create_all(bind=engine)

app.celery_app = create_celery()
celery = app.celery_app

app.include_router(project.router)
app.include_router(scenario.router)
app.include_router(scenario_page.router)
app.include_router(scenario_operation.router)
app.include_router(user.router)
app.include_router(page.router)
app.include_router(page_element.router)
app.include_router(page_operation.router)
app.include_router(page_step.router)
app.include_router(suite.router)
app.include_router(task.router)
app.include_router(universities.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)


