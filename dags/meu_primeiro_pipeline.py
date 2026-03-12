from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from pendulum import datetime
import pandas as pd

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
)
def pipeline_atividade_pratica():

    @task
    def extrair_dados():
        hook = PostgresHook(postgres_conn_id='postgres_source')
        df = hook.get_pandas_df(sql="SELECT * FROM customers;")
        return df

    @task
    def salvar_arquivo_csv(df: pd.DataFrame):
        caminho = "/usr/local/airflow/include/clientes_extraidos.csv"
        df.to_csv(caminho, index=False)
        return caminho

    @task
    def carregar_no_destino(caminho_arquivo: str):
        df_lido = pd.read_csv(caminho_arquivo)
        hook = PostgresHook(postgres_conn_id='postgres_target')
        hook.insert_rows(
            table='customers', 
            rows=df_lido.values.tolist(), 
            target_fields=df_lido.columns.tolist()
        )

    tabela_bruta = extrair_dados()
    caminho_final = salvar_arquivo_csv(tabela_bruta)
    carregar_no_destino(caminho_final)

pipeline_atividade_pratica()