# databricks-notebook-cicd-ado

This is a sample project for Databricks showcasing how to leverage DBX with Azure DevOps Pipelines.


## CICD pipeline settings

#### Azure DevOps Pipelines
This pipeline uses `Variable Groups` to hold the credentials required to establish connectivity to the Databricks Workspace.

Each `Variable Group` needs to have the follow variables/secrets defined:
- `DATABRICKS_HOST`
- `DATABRICKS_TOKEN`


The pipeline in this repo is set to use `dev-databricks-workspace-environment` and `prod-databricks-workspace-environment` as the variable group names for the Dev and Prod deployments. This can be changed in the `azure-pipelines.yml` file.


## Deploying from IDE (Local Machine)
The workflow can also be deployed and restarted locally using the following commands in the terminal:

1. Deploy updated job configuration
`dbx deploy --deployment-file=conf/dev-deployment.yml --no-rebuild`

<br>

2. Start job, and restart and current executions
`dbx launch --job=databricks-notebook-cicd-ado-dev --existing-runs=cancel `