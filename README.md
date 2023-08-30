# USA Jobs API Search
APP designed for retrieving Daily Job Opportunity Announcements data for a given keyword.

[API Docs](https://developer.usajobs.gov/API-Reference/GET-api-Search)
## Table of content

| Content | Description |
| :------ | :---------- |
| [1. Installation](#1-installation) | Steps for dependencies installation and other configurations |
| [2. Guidelines](#2-guidelines) | Philosophy and rules for coding |
| [3. Architecture Walkthrough](#3-architecture-walkthrough) | APP design and project general layout |
| [4. APP Usage](#4-app-usage) | How to use this application |
| [5. Cloud Implementation](#5-cloud-implementation) | APP architecture implemented in GCP |
| [6. Future Improvements](#6-future-improvements) | Making a more robust and efficient application |

## 1. Installation

### 1.1 Dependencies installation

---
```
As of today: Wednesday, 30th August/2023

running the services with:

Python == 3.11.4
MacOS Ventura 13.5 | Apple M1 2020

```

---

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

<p align="center">
  <img src="https://github.com/algiraldohe/us-jobs-reporting-db/blob/development/docs/images/ProjectStructure(1).png" alt="ProjectStructure">
</p>



All code relevant to how a user access data (HTTP requests, Console) should be in the application folder, that is why all frameworks code is located in this folder.

Inside `application` folder, there is a folder called `adapters`, inside, contains functions or classes that allow us to transform the requests from the user into actions that will be carried by the `domain` or business logic. This favours the possibility of including easily new adapters for the user to interact with the app, for example in a cloud implementation the request should be translated from an HTTP request, but the logic should remain doing exactly the same.

In `domain` folder is located all the code related to the business logic, it does not care about what is the body of the request containing, or what is the database we are querying, or where are we storing the data. This code uses the adapters generated by the `infrastructure` folder to get and perform what it needs in a decoupled way.

In `infrastructure` folder we have all the code related to persistence (databases, file storage), notifications (sms, mails), local services (file navigation, local storage) and external sources (Google APIs, USA Jobs API). The idea is to have adapters (classes) that handle all these sources' logic so that `domain` code can change of adapter easily and keep working.

### 2.2 Rules
Some rules we should encourage in our development:

**Rule 1:** name of a function should clearly tell what a function is doing.

**Rule 2:** when a function starts to increase in its number of parameters it's generally because it is doing more than expected.

**Rule 3:** long functions usually reflect that maybe the function is handling things that other new functions should handle.

**Rule 4:** a function should be always testable. Testability becomes difficult when other functions or clients are used in that function, this can be solved using dependency injection, that is, sending clients and functions as parameters to the function. However, sometimes it requires creating mocks during the testing. It is acceptable. But choose well which functions should have dependencies and which not.

## 3. Architecture Walkthrough

<p align="center">
  <img src="https://github.com/algiraldohe/us-jobs-reporting-db/blob/development/docs/images/USJobs.png" alt="BaseArchitectureDiagram">
</p>

The diagram simulates a loosely decoupled architecture where each component operates independently improving flexibility and scalability.

### 3.1. Components

- **Orchestrator:** In charge of making the request to the host in order to carry out the process at the specified time (daily scheduled trigger).

- **Data Sources:** The USAJOBS REST-based API is designed to support lightweight content consumption by consumers.

- **Host:** Docker container running Python and PostgreSQL images with the following assignments:
 *(Each representing an independent container)*

		1. Parse request for the job search from the user, fetch the data and load it into a folder.
		2. Take the data, clean, transform and load it into the database with a set schema.

### 3.2 Main Tech Stack

- **Python**
- **SQLAlchemy**
- **Alembic**
- **PostgreSQL**
- **Cron**
- **Docker**

## 4. APP Usage

### 4.1 Components

`extraction`: This folder contains all the container configurations, packages and code required to carry out the search request and store the response data back in the system.

`transformation-load:` This folder contains all the container configurations, packages and code required to read the data from the file stored, format it, and store it in the Postgres database.

`file-storage:` This folder serves the purpose of a "bucket" or file storage in the local environment.

`postgres-data:` This folder serves the purpose of storing the data transformed in a resilient way independently from the container storage.

`database-network`: Virtual environment within docker, created to allow the docker containers to communicate with each other.

`orchestration.sh` : Bash file with the make commands to execute the docker actions.

### 4.2 Setting Everything Up

#### 4.2.1 Containers
The two main services of the app run independently from one another in one container each. Additionally, there are other 2 containers that compose the application `us-jobs-application`:

1. `extraction-service`
2. `transform-load-service`
3. `db`
4. `db-admin`

#### 4.2.2 Requirements:
- Docker must be installed and running already in the environment.
- Python must be installed if running locally without docker.
- `.env` and `.env.docker` should be filled in.
  ***Note: (Keep the env variable FILESTORAGE=../file-storage/)***
- Verify in the folder repository that the user has the right permissions to execute the code.

### 4.3 Commands

The following instructions illustrate how to run `us-jobs-application` using docker.

***DISCLAIMER: The following instructions only apply to users that are running MacOS. This documentation does not provide the setting up instructions to run the code in Windows although the commands might be similar to Linux environments***

#### 4.3.1 Setting Up the Repo

1. Cloning the repository
```bash
git clone git@github.com:algiraldohe/us-jobs-reporting-db.git

```

2. Fill the  `.env.docker` to run from docker.
#### 4.3.2 Extraction
[See Extraction Service](./extraction/README.md)

#### 4.3.3 Transformation Load
[See Transformation Load  Service](./transformation-load/README.md)

#### 4.3.4. Crontab
Set up the job in the local machine to run the application.

``` bash
# Open crontab
crontab -e

# Using vim: press "I" + copy paste the command below
0 3 * * * sh /Users/alejandrogiraldoh/Development/us-jobs-reporting-db/orchestration.sh >> /Users/alejandrogiraldoh/Development/us-jobs-reporting-db/orchestration-log.txt

# type esc + :wq + enter

```

The entered cron expression will run our orchestration.sh everyday at 03:00.
Reference for [Cron Expressions](https://crontab.guru)
## 5. Cloud Implementation
<p align="center">
  <img src="https://github.com/algiraldohe/us-jobs-reporting-db/blob/520eb73aaabd44c953a6f26d09fefac911058fc0/docs/images/Cloud%20GCP%20Architecture(2).png" alt="CloudArchitecture">
</p>

### 5.1 Services Breakdown

|Component|Service|Pros|Cons|
|:---:|:---:|---|---|
|Containerised App Execution|Google Kubernetes Engine (GKE)|- Managed clusters for deployment and scaling<br>- Auto-scaling for efficient resource utilisation <br>- Easy container deployment and management<br>|- Learning curve to learn how to use Kubernetes <br> - Cost is higher for simple applications in the short-term|
|Data Processing|Kubernetes Pod(s) with Python|- Customisable processing environment using Docker<br> - Flexibility in choosing Python libraries<br> - Easy scaling using Kubernetes replicas|- Learning curve to learn how to use Kubernetes|
|Data Storage|Google Cloud Storage|- Highly available and durable storage<br>- Cost-effective storage solution|- Constant data movement and retrieval does not allow for cost optimisation|
|Database|Google Cloud SQL for PostgreSQL|- Fully managed PostgreSQL service<br> - Automatic backups and high availability. <br>|- Slightly higher cost compared to self-managed solutions.|
|Scheduling|Cloud Scheduler|- Managed job scheduler for task automation. <br> - Can trigger HTTP endpoints directly.|- Slight more costly for scheduling, but low in general.|
|Logging and Monitoring|Google Cloud Logging and|- Centralised logging and monitoring for application<br> - Customisable alerts and dashboards. |- The cost might increase with extensive usage.|
|Credentials Management|Google Cloud Secret Manager|- Securely manage and rotate credentials<br>|- Slight costly, but generally low|


### 5.2. Rationale
**Component: Containerised App Execution
Alternative Service: Google Compute Engine (GCE)**

*Reasons not to use it:*
- **Resource Management:** While GCE allows you to create virtual machines for running your containers, it doesn't offer the same level of container orchestration and scaling as GKE. You would need to manually manage auto-scaling and cluster operations.
- **Complexity:** Managing individual VM instances for containers can be more complex and time-consuming compared to GKE's managed Kubernetes clusters.

**Component: Data Processing and Transformations
Alternative Service: Google Cloud Dataproc**

*Reasons not to use it:*
- **Overhead:** Google Cloud Dataproc is designed for processing big data workloads using frameworks like Hadoop and Spark. right now the application does not have extensive data needs, using Dataproc might introduce unnecessary overhead.
- **Configuration Complexity:** Setting up and configuring Dataproc clusters might be more complex than using Kubernetes Pods for smaller-scale processing tasks.
- **Redefinition Tasks:** In order to take out most of the distributed workloads, might require tweaking the code for parallel processing or switch it over completely to PySpark.

**Component: Data Storage
Alternative Service: Google Cloud Bigtable**

*Reasons not to use it:*
- **Data Format:** Google Cloud Bigtable is designed for storing and processing large-scale data using a NoSQL data model. Is designed for high-throughput, low-latency applications which is not the case. Besides the fact that Cloud Storage provides the choice to change the storage class which ultimately can reduce cost and integrates directly with BigQuery providing query capabilities.
- **Querying Flexibility:** Bigtable's query capabilities are different from Cloud Storage and relational databases. If you need complex querying and relational data modeling, Bigtable might not be the ideal choice, although this point highly depends on the downstream analytics services that are going to use the data. As the process extends, Cloud Storage is very cost-efficient and and don't require transform operations before loading the data., not even a defined schema.

**Component: Database
Alternative Service: Google Cloud Firestore**

*Reasons not to use it:*
- **Data Model:** Firestore is a NoSQL document database, and its data model might not align with the requirements of a traditional relational database like PostgreSQL. Although at this point highly depends on the downstream analytics services that are going to use the data, to establish how should be stored. If you need complex relationships and querying capabilities, BigQuery provides transformation, query and flexibility capabilities taking into account the structure of the data after the transformation process.
- **Schema Flexibility:** While NoSQL databases offer schema flexibility, they might not provide the same level of data consistency and integrity as a well-designed relational database schema, which BigQuery can infer from Json or even be defined but allowing flexibility on aggregated or nested fields while maintaining data consistency.

**Component: Scheduling
Alternative Service: Google Cloud Composer (managed Apache Airflow)**

*Reasons not to use it:*
- **Complexity:** Cloud Composer is designed for orchestrating complex workflows. If your scheduling needs are relatively simple, using Cloud Scheduler might be more straightforward.
- **Cost:** Cloud Composer involves additional costs compared to Cloud Scheduler, so if cost optimisation is a priority, Cloud Scheduler might be a more cost-effective option.

 **Component: Credentials Management
 Alternative Service: Google Cloud KMS (Key Management Service)**

*Reasons not to use it:*
- **Focus on Encryption:** Google Cloud KMS is primarily designed for managing cryptographic keys and data encryption which in this case is not a must considering the nature of the data. While it can manage credentials, its primary use case is different from Google Cloud Secret Manager's focus on managing secrets and credentials.

### 5.3. Summary

For a specific use case, many services can provide out-of-the-box functional solutions that can fulfil the intended purpose, but in the end, we need to have a very specific business requirement where you can assess the trade-offs of choosing one service or the other more accurately. At the moment with the information provided and the parameters given to solve the use case, I'm confident to say that the proposed architecture presents an optimal cutting-edge solution to support the functioning of the application developed, with good practices aiming to optimise costs, retain security and achieve operational efficiency.

## 6. Future Improvements

### 6.1. General
- Logging, messaging and notification.
- Automated unit testing.
- GitHub actions or DevOps, in general, to fast-track development to the production cycle.
- Implementation of abstract classes for code and methods re-utilisation.
- More robust error handling.
- In-depth cleansing operations, given downstream services to complement the job performed.
- Modernise the tech stack using tools like DBT for a more robust and well-managed transformation pipeline, and Terraform to take care of the management and provision of cloud services with good practices.

### 6.2. Services Specific
- [Improvements in extraction service](./extraction/README.md)
- [Improvements in transformation-load service](./transformation-load/README.md)




