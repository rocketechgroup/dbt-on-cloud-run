import asyncio

from google.cloud import run_v2


def run_job_sync(project_id, location, job_id, override_args):
    """
    Runs a job. Sync, waits for the whole cloud run job execution to complete
    """
    # Create a client
    client = run_v2.JobsClient()

    # Initialize request argument(s)
    request = run_v2.RunJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}",
        overrides=run_v2.types.RunJobRequest.Overrides(
            container_overrides=[
                run_v2.types.RunJobRequest.Overrides.ContainerOverride(
                    args=override_args
                )
            ]
        )
    )

    # Make the request
    operation = client.run_job(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


async def run_job_async(project_id, location, job_id, override_args):
    """
    Run a job asynchronously.
    """
    # Create a client
    client = run_v2.JobsAsyncClient()

    # Initialize request argument(s)
    request = run_v2.RunJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}",
        overrides=run_v2.types.RunJobRequest.Overrides(
            container_overrides=[
                run_v2.types.RunJobRequest.Overrides.ContainerOverride(
                    args=override_args
                )
            ]
        )
    )

    # Make the request
    operation = client.run_job(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)


# Example usage
project_id = "rocketech-de-pgcp-sandbox"
location = "europe-west2"
job_id = "dbt-cloud-run-job-demo"

# override to do dbt debug
override_args = ["poetry", "run", "dbt", "debug", "--target", "dev"]

# Sync submission
run_job_sync(project_id, location, job_id, override_args=override_args)

# Async submission
override_args = ["poetry", "run", "dbt", "run", "--full-refresh", "--target", "dev"]
asyncio.run(run_job_async(project_id, location, job_id, override_args))
