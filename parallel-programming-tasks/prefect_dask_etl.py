from prefect import flow, task
import dask.dataframe as dd
from dask.distributed import Client

@task
def load_data(path):
    df = dd.read_csv(path)
    return df

@task
def transform_data(df):
    result = df.groupby("name").amount.mean().compute()
    return result

@task
def save_result(result, output_path):
    with open(output_path, "w") as f:
        f.write(result.to_string())
    return output_path

@flow
def prefect_dask_etl_flow(
    input_path="data/people.csv",
    output_path="result.txt"
):
    client = Client()  # buka Dask client
    df = load_data(input_path)
    result = transform_data(df)
    saved_path = save_result(result, output_path)
    client.close()
    return saved_path

if __name__ == "__main__":
    prefect_dask_etl_flow()
