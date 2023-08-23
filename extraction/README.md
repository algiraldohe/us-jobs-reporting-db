# Extraction Container
App designed for retrieving Daily Job Opportunity Announcements data for a given keyword.

## Table of content

| Content | Description |
| :------ | :---------- |
| [1. Installation](#1_installation) | Steps for dependencies installation |

## 1. Installation

### 1.1 Dependencies installation

To install this project, it is recommended to use `virtualenv` python package. By default, macOS has installed the `python3` binary. So the following commands should work:


Install virtualenv to create an environment for your python packages:
```
python3 -m pip install virtualenv
```

If pip is not installed follow the guide at https://pip.pypa.io/en/stable/installation/. Use get-pip.py code.

Create an environment:
```
python3 -m virtualenv -p python3 venv
```

Activate the environment:
```
source venv/bin/activate
```

Install python dependencies:

```
pip install -r dev-requirements.txt -r requirements.txt
```

Run tests (tests configuration is set in pytest.ini):

```
python -m pytest tests/
```

Run tests and get coverage:

```
coverage run -m pytest tests/ && coverage report -m
```

Check linting (linting configuration is set in .flake8):

```
flake8
```

Check more linting:

```
black -l 88 --preview .
```


```
isort --profile=black .
```

Check docstyle in the code (docstyle configuration is set in .pydocstyle):

```
pydocstyle
```
