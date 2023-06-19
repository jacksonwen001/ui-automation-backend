# 按照 poetry
```
curl -sSL https://install.python-poetry.org | python3 -
```

# 初始化项目
```
mkdir <projectName>
cd <projectName>
poetry init
poetry config virtualenvs.in-project true
poetry env use python3.11
```
# 添加依赖
```
poetry add "fastapi[all]"
```


# 启动 celery
```
# -c 100: 100 个线程池， 否则默认是系统CPU 核数。 这里不动
celery -A main.celery worker  --loglevel=info -Q universities,university
```

# 结构
```
suite
  -- before
  -- group1 ---group2 ---group3 ---group4 
  -- after 

testdata -> before(login) -> group1/2/3/4 
                          -> after(logout)

celery -> execute suite -> before -> thread1: group1
                                  -> thread2: group2
                                  -> thread3: group3
                                  join
                                  -> after

get_task_info -> check status 
```
