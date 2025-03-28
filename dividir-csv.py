import pandas as pd
import math
import os

#arquivo de entrada
input_csv = "46.csv"

#quantidade de divisoes
num_files = 10

if not os.path.exists(input_csv):
    print(f"Erro: O arquivo {input_csv} não foi encontrado.")
    exit()


df = pd.read_csv(input_csv)

#pega o nome do arquivo original pra nomear as divisoes 
file_name = os.path.splitext(os.path.basename(input_csv))[0]

#definir o número de linhas por arquivo
total_rows = len(df)
rows_per_file = math.ceil(total_rows / num_files)  # Arredonda para cima

#divide o arquivo em partes iguais
for i in range(num_files):
    start_idx = i * rows_per_file
    end_idx = (i + 1) * rows_per_file

    #garante que a divisao final ta certa
    if end_idx > total_rows:
        end_idx = total_rows

    #cria um novo DataFrame com as linhas correspondentes
    df_split = df.iloc[start_idx:end_idx]

    #nome do arquivo de saída 
    output_csv = f"{file_name}-part_{i + 1}.csv"

    
    if os.path.exists(output_csv):
        print(f"Erro: O arquivo {output_csv} já existe. Por favor, mova ou exclua os arquivos de saída antes de executar o código.")
        exit()

    #salva em um novo arquivo CSV
    df_split.to_csv(output_csv, index=False)

    print(f"Arquivo {output_csv} salvo com {len(df_split)} linhas.")

