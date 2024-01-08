import pandas as pd

def split_csv(file_path, chunk_size, output_name):
    chunk_container = pd.read_csv(file_path, chunksize=chunk_size)
    
    for i, chunk in enumerate(chunk_container):
        chunk.to_csv(f'{output_name}_{i}.csv', index=False)

file_path = 'data_modified.csv'

chunk_size = 50000

output_name = 'data_modified_chunk.csv'

split_csv(file_path, chunk_size, output_name)

