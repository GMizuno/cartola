from google.cloud import bigquery

from cartola_2023.bigquery import client
from cartola_2023.bigquery.schema import schema_obt_players
from cartola_2023.constant import ProjectId, DATASET_ID

project_id = f"{ProjectId.GCP_PROD}"
tabela = "obt_players"
table_id = f"{project_id}.{DATASET_ID}.{tabela}"

dataset_ref = bigquery.dataset.DatasetReference(
    project=project_id, dataset_id=DATASET_ID
)

table_ref = dataset_ref.table(tabela)

table = bigquery.Table(table_ref, schema=schema_obt_players)

table = client.create_table(table)
