# USA Jobs API Search
Flask app designed for retrieving Daily Job Opportunity Announcements data for a given keyword.

[API Docs](https://developer.usajobs.gov/API-Reference/GET-api-Search)

## Table of content


| Content | Description |
| :------ | :---------- |
| [1. Installation](#1-installation) | Steps for dependencies installation and other configurations |
| [2. Guidelines](#2-guidelines) | Philosophy and rules for coding |
| [3. Architecture Walkthrough](#3-architecture-walkthrough) | APP design and project general layout |
| [4. APP Usage](#4-app-usage) | How to use this application |
| [5. Cloud Implementation](#5-cloud-implementation) | APP architecture implemented in gcp |
| [6. Future Improvements](#6-future-improvements) | Making a more robust and efficient application |

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

Check commits:

```

pre-commit install --hook-type commit-msg --hook-type pre-push

```
## 2. Guidelines

### 2.1 Folder structure


The main idea is to split the code into three cores: application, domain and infrastructure (see diagram).

![ProjectStructure](https://github.com/algiraldohe/us-jobs-reporting-db/blob/development/docs/images/ProjectStructure.png)


All code relevant to how a user access data (HTTP requests, Console, WebSockets, GraphQL, etc) should be in the application folder, that is why all frameworks code is located in this folder. There is a main.py that is outside and it uses Flask, but it was left there for simplicity.

Inside `application` folder there are two folders, one for `blueprints` a.k.a. flask apps. Here for each specific set of tasks, we could define an app and its routes. The second folder `adapters` are functions or classes that allow us to transform data retrieved for `domain` code into data that the user is requesting or expecting to see.

In `domain` folder is located all the code related to the business logic, it does not care about what is the body of the request containing or what is the database we are querying. This code uses the adapters generated by the `infrastructure` folder to get what it needs.

In `infrastructure` folder we have all the code related to persistence (databases, file storage), notifications (sms, mails), and external sources (Google Trends API, Twitter API). The idea is to have adapters (classes) that handles all these sources logic, so that `domain` code can change of adapter easily and keep working.

### 2.2 Rules
Some rules we should encourage in our development:

**Rule 1:** name of a function should clearly tell what a function is doing.

**Rule 2:** when a function starts to increase in its number of parameters it's generally because it is doing more than expected.

**Rule 3:** long functions usually reflect that maybe the function is handling things that other new functions should handle.

**Rule 4:** a function should be always testable. Testability becomes difficult when other functions or clients are used in that function, this can be solved using dependency injection, that is, sending clients and functions as parameters to the function. However, sometimes it requires creating mocks during the testing. It is acceptable. But choose well which functions should have dependencies and which not.

## 3. Architecture Walkthrough

![BaseDiagram](https://github.com/algiraldohe/us-jobs-reporting-db/blob/development/docs/images/USJobs.png)

The diagram simulates a loosely decoupled architecture where each component operates independently improving flexibility and scalability.

**Tech Stack:**
Cron: Time-based job scheduler
Python
Docker
PostgreSQL

### 3.1. Components

- **Orchestrator:** In charge of making the request to the host in order to carry out the process at the specified time (daily scheduled trigger).

- **Data Sources:** The USAJOBS REST-based API is designed to support lightweight content consumption by consumers.

- **Host:** Docker container running Python and PostgreSQL images with the following assignments:
 *(Each representing an independent container)*

1. Parse request for the job search from the user, fetch the data and load it into a folder.
2. Take the data, clean, transform and load it into the database with a set schema.

### 3.2 Main Tech Stack


## 4. APP Usage

### 4.1 Components

`extraction`: This folder contains all the container configurations, packages and code required to carry out the search request and store the response data back in the system.

`transformation-load:` This folder contains all the container configurations, packages and code required to read the data from the file stored, format it, and store it in the Postgres database.

`file-storage:` This folder serves the purpose of a "bucket" or file storage in the local environment.

`postgres-data:` This folder serves the purpose of storing the data transformed in a resilient way independently from the container storage.

`database-network`: Virtual environment created to allow the docker containers to communicate with each other.
### 4.2 Setting Everything Up

#### 4.2.1 Containers
The two main services of the app run independently from one another. There are four containers that compose the application `us-jobs-application`:

1. `extraction-service` 
2. `transform-load-service`
3. `db`
4. `admin`

#### 4.2.2 Requirements:
- Docker must be installed and running already in the environment.
- Python must be installed if running locally without docker.
- `.env` and `.env.docker` should be filled in. 
  ***Note: (Keep the env variable FILESTORAGE=../file-storage/)***
- Verify in the folder repository that the user has the right permissions to execute the code.

### 4.3 Commands

The following instructions illustrate how to run `us-jobs-application` using docker.

***DISCLAIMER: The following instructions only apply to users that are running MacOS. This documentation does not provide the setting up instructions to run the code in Windows although the commands might be similar to Linux environments***

#### 4.3.1 Setting the Repo

1. Cloning the repository 
```bash
git clone git@github.com:algiraldohe/us-jobs-reporting-db.git

```

2. Fill the  `.env.docker` to run from docker.
#### 4.3.2 Extraction
[See Extraction Service](./extraction/README.md)

## 5. Cloud Implementation

![CloudArchitecture](https://github.com/algiraldohe/us-jobs-reporting-db/blob/development/docs/images/Cloud%20GCP%20Architecture.png)

### 5.1 Services Breakdown


## 6. Future Improvements




