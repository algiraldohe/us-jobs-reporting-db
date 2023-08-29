# Extraction Container
App designed for retrieving Daily Job Opportunity Announcements data for a given keyword spaning a time frame.

## Table of content

| Content | Description |
| :------ | :---------- |
| [1. Installation](#1-installation) | Steps for dependencies installation |
| [2. Guidelines](#2-guidelines) | Code structure and layout |
| [3. APP Usage](#3-app-usage) | How to use the APP |

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

## 2. Guidelines

### 2.1 Files Structure

For the correct functioning of the application I have disposed the following:

`Makefile` used to build and run the docker container for the app.
`Dockerfile` with the container configuration and required images.
`.env` and `.env.docker` with environment variables used in the extraction process one for local testing one for container testing.


## 3. APP Usage

In order to run the extraction process use the following:

```
# Build the image of the container
make build

# Run the container
make run
```

**Running Locally**

`python3 main.py --console "extract_jobs" "data engineering" 2 "Chicago, Illinois"`
