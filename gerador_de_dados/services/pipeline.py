import pandas as pd
from gerador_de_dados.modules.client_gen import ClientGenerator

def run_pipeline(n_rows):
    generator = ClienteGenerator()
    data = [generator.generate_client(i) for i in range(1, n_rows + 1)]

    df = pd.DataFrame(data)

    return df.to_csv(index=False, encoding='utf-8')