from google.cloud import bigquery

from cartola_2023.bigquery.schema import schema_obt_matches
from cartola_2023.constant import ProjectId

client = bigquery.Client('cartola.json')

project_id = f'{ProjectId.GCP_PROD}'
dataset_id = 'cartola'
tabela = 'obt_matches'
table_id = f"{project_id}.{dataset_id}.{tabela}"

dataset_ref = client.dataset(dataset_id, project=project_id)

table_ref = dataset_ref.table(tabela)

table = bigquery.Table(table_ref, schema=schema_obt_matches)

table = client.create_table(table)
