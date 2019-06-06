# pytest with tox demo

## how to running

* exec command

```code
tox
```

* some result

```code
GLOB sdist-make: /Users/dalong/mylearning/pytest-projects/setup.py
py27 inst-nodeps: /Users/dalong/mylearning/pytest-projects/.tox/.tmp/package/1/firsttest-0.0.3.zip
py27 installed: atomicwrites==1.3.0,attrs==19.1.0,configparser==3.7.4,contextlib2==0.5.5,firsttest==0.0.3,funcsigs==1.0.2,hashids==1.2.0,importlib-metadata==0.17,more-itertools==5.0.0,packaging==19.0,pathlib2==2.3.3,pluggy==0.12.0,py==1.8.0,pyparsing==2.4.0,pytest==4.6.2,scandir==1.10.0,six==1.12.0,wcwidth==0.1.7,zipp==0.5.1
py27 run-test-pre: PYTHONHASHSEED='2484884844'
py27 run-test: commands[0] | pytest
=========================================================== test session starts ============================================================
platform darwin -- Python 2.7.15, pytest-4.6.2, py-1.8.0, pluggy-0.12.0
cachedir: .tox/py27/.pytest_cache
rootdir: /Users/dalong/mylearning/pytest-projects
collected 1 item                                                                                                                           

firsttest/test_userid.py .                                                                                                           [100%]

========================================================= 1 passed in 0.02 seconds =========================================================
py37 inst-nodeps: /Users/dalong/mylearning/pytest-projects/.tox/.tmp/package/1/firsttest-0.0.3.zip
py37 installed: atomicwrites==1.3.0,attrs==19.1.0,firsttest==0.0.3,hashids==1.2.0,importlib-metadata==0.17,more-itertools==7.0.0,packaging==19.0,pluggy==0.12.0,py==1.8.0,pyparsing==2.4.0,pytest==4.6.2,six==1.12.0,wcwidth==0.1.7,zipp==0.5.1
py37 run-test-pre: PYTHONHASHSEED='2484884844'
py37 run-test: commands[0] | pytest
=========================================================== test session starts ============================================================
platform darwin -- Python 3.7.3, pytest-4.6.2, py-1.8.0, pluggy-0.12.0
cachedir: .tox/py37/.pytest_cache
rootdir: /Users/dalong/mylearning/pytest-projects
collected 1 item                                                                                                                           

firsttest/test_userid.py .                                                                                                           [100%]

========================================================= 1 passed in 0.02 seconds =========================================================
_________________________________________________________________ summary __________________________________________________________________
  py27: commands succeeded
  py37: commands succeeded
  congratulations :)
```