import functions_framework
import pandas_gbq
import pandas as pd


def build_file_path(bucket: str, file_path: str) -> str:
    return f"gs://{bucket}/{file_path}"


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    bucket = data["bucket"]
    name = data["name"]

    path = build_file_path(bucket, name)
    print(path)
    data = pd.read_parquet(path).astype(str)
    print(data.columns)
    pandas_gbq.to_gbq(
        data,
        "cartola-360814.cartola_raw.players",
        project_id="cartola-360814",
        if_exists="append",
    )
