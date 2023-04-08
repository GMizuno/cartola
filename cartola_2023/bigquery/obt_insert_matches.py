from google.cloud import bigquery

from cartola_2023.bigquery.schema import schema_obt_matches
from cartola_2023.constant import ProjectId

client = bigquery.Client('cartola.json')

project_id = f'{ProjectId.GCP_PROD}'
dataset_id = 'cartola'
tabela = 'obt_matches'
table_id = f"{project_id}.{dataset_id}.{tabela}"

job_config = bigquery.LoadJobConfig(
    schema=schema_obt_matches,
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)
uri = f"gs://cartola_mizuno/obt/{tabela}/*.parquet"

load_job = client.load_table_from_uri(
    uri,
    table_id,
    project=project_id,
    job_config=job_config,
)

load_job.result()
