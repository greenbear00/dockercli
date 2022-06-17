# DockerCLI

다중 docker container에 동시 명령어를 수행할 수 있는 cli command

## 설치방법

사용 가능한 명령어
- ls : 현재 docker container를 보여줌
- exec : 지정한 cname(docker container name과 일치한 container)에 cmd(명령어) 를 수행함

설치
```
# 먼저 pip update
python3 -m pip install --upgrade pip

python3 setup.py bdist_wheel
pip install dist/dockercli-1.0-py3-none-any.whl

# 만약 오류가 생긴다면.
pip install --force-reinstall dist/dockercli-1.0-py3-none-any.whl

dockercli -v
Version 1.0
```

## 사용법
```
$ dockercli --help

$ dockercli ls --help

$ dockercli exec --help

$ dockercli ls                                              
List of current docker containers.
        [airflow-cluster_airflow-worker_2] running
        [airflow-cluster_airflow-worker_3] running
        [airflow-jupyter] running
        [flower] running
        [airflow-cluster_airflow-worker_1] running
        [airflow-webserver] running
        [airflow-triggerer] running
        [airflow-scheduler] running
        [mysql] running
        [redis] running

$ dockercli exec -cname worker -cmd pwd -u root
[airflow-cluster_airflow-worker_2] running
/opt/airflow

====================================================================================================
[airflow-cluster_airflow-worker_3] running
/opt/airflow

====================================================================================================
[airflow-cluster_airflow-worker_1] running
/opt/airflow

====================================================================================================
DONE!

```

