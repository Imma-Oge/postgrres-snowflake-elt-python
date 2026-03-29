# ETL Project: PostgreSQL to Snowflake with Python

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the repository](#-1-clone-the-repository)
  - [2. Create a Python virtual environment (optional but recommended)](#-2-create-a-python-virtual-environment-optional-but-recommended)
  - [3. Install dependencies](#-3-install-dependencies)
  - [4. Set up .env file](#-4-set-up-env-file)
  - [5. Connect to databases](#-5-connect-to-databases)
  - [6. Run ETL scripts](#-6-run-etl-scripts)
- [Dependencies](#7-dependencies)
- [Next Steps](#next-steps)
  - [Advanced Transformations](#advanced-transformations)
  - [Gold Layer Preparation](#gold-layer-preparation)
  - [Automation / Scheduling](#automation--scheduling)
  - [Testing & Monitoring](#testing--monitoring)
  - [Documentation & Visualization](#documentation--visualization)
  - [Portfolio & Presentation](#portfolio--presentation)

## Overview
This repository contains a Python-based ETL (Extract, Transform, Load) project designed to connect to a PostgreSQL database, perform data transformations, and load data into a Snowflake data warehouse. The project leverages environment variables for secure credential management and modular Python functions for reusable database connections.

The workflow is suitable for learning analytics, reporting, and data engineering.

## Features
* PostgreSQL connection using SQLAlchemy and psycopg2.
* Snowflake connection using SQLAlchemy for Python.
* Environment variable management using .env files for secure storage of credentials.
* Modular functions for reusable database connections.
* ETL pipeline capable of reading from Postgres and writing to Snowflake using pandas.
* Follows standard Python best practices for readability and maintainability.

## Folder Structure
```
project-root/
│
├── ETL_Notebooks/             # Jupyter notebooks containing ETL scripts
│   └── ETL.ipynb
│
├── src/
│   └── db_connections.py      # Functions to connect to Postgres and Snowflake
│
├── .gitignore                 # To ignore files like .env
├── .env                       # Environment variables (never push credentials!)
├── 
└── README.md                  # Project documentation

```

## Setup Instructions

##  1. Clone the repository
git clone <your-repo-url>
cd <your-project-folder>

##  2. Create a Python virtual environment (optional but recommended)
conda create -n etl_env python=3.11
conda activate etl_env

##  3. Install dependencies

##  4. Set up .env file
Create a .env file in the project root:
```
db_user=your_postgres_user
db_password=your_postgres_password
db_host=your_postgres_host
db_port=5432
db_database=your_postgres_db

sf_user=your_snowflake_user
sf_password=your_snowflake_password
sf_account=your_snowflake_account
sf_warehouse=your_snowflake_warehouse
sf_database=your_snowflake_database
sf_schema=your_snowflake_schema
```

##  5. Connect to databases
Use the functions defined in ```src/db_connections.py ```

```
from src.db_connections import get_postgres_engine, get_snowflake_connection
# Connect to Postgres
pg_engine = get_postgres_engine()

# Connect to Snowflake
sf_conn = get_snowflake_connection()
```

##  6. Run ETL scripts

## 7. Dependencies
* Python 3.11+
* pandas
* SQLAlchemy
* psycopg2
* snowflake-connector-python
* python-dotenv

#Next Steps:
After the initial ETL setup and loading data into Snowflake, the project will evolve with the following:

## Advanced Transformations
* Clean, standardize, and enrich data in the Silver layer.
* Apply business rules, calculations, and joins across tables.
## Gold Layer Preparation
* Aggregate data for analytics-ready tables.
* Prepare KPI tables, summaries, and dashboards-ready datasets.
## Automation / Scheduling
* Schedule ETL notebooks using Airflow, Prefect, or cron jobs.
* Automate incremental updates from Postgres to Snowflake.
## Testing & Monitoring
* Implement unit tests for transformation logic.
* Monitor Snowflake loads and data quality for consistency.
## Documentation & Visualization
* Maintain data dictionaries for all tables.
* Add visual dashboards or reports on top of the Gold layer.
## Portfolio & Presentation
* Add visual summaries of the ETL workflow.
* Include example analytics queries to showcase the Gold layer’s value.
