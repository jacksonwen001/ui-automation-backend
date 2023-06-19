
'''
执行具体的case, 这里主要是执行步骤 
'''
from internal.tester import Tester


def execute_scenario(scenario_id: str, browser: str, browser_version: str): 
    # 获取 scenario 
    print("Get scenario_id: " + scenario_id)

    # if scenario is cancelled, just return 

    # update scenario to running
    print("update scenario to running")

    # create new tester
    tester = Tester()
    
    # start browser
    tester.start_browser(browser, browser_version)
    
    # execute step 
    for step in []:
        pass
    
    # if there are any exception, update scenario to failed else succeed
    