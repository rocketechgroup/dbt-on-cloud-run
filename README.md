# dbt-on-cloud-run

Execute DBT core on Cloud Run Job

## Prerequisites

- Python 3.11+
- Poetry
- Docker
- Load the seed data under `dbt/seeds`
- Update the following in `dbt/profiles.yml` to match to your environment:
    - project: <change to yours>
    - dataset: <change to yours>

## How to run locally

```
poetry update
poetry shell
cd dbt
dbt run
```

## Build

```
gcloud builds submit --config cloudbuild_build.yaml . --substitutions _REPO_NAME=demo
```

## Create the Cloud Run Job

> this uses the `deploy` command which manages both create and update

```
gcloud builds submit --config cloudbuild_create.yaml . --substitutions _REPO_NAME=demo
```

## Trigger execution, including overriding
See [cloudrun/execute_cloud_run_job.py](cloudrun/execute_cloud_run_job.py)