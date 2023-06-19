from fastapi import APIRouter
from internal.tester import Tester
from schemas import task

router = APIRouter(tags=['tasks'], prefix='/tasks')

@router.get('')
async def query(): pass

@router.post('')
async def execute(request: task.ExecuteRequest): 
    tester = Tester()
    tester.start_browser(request.browser, request.browser_version)
    tester.execute('open', None, None, 'http://www.baidu.com', {})
    tester.execute('type', 'id', 'kw', 'selenium', {})
  
