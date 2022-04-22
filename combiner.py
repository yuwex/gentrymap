import pandas as pd

def load_df_with_year(path: str, year: int):
    df = pd.read_csv(path)
    df['year'] = year
    return df

def merge_csvs(start=2010, end=2020) -> pd.DataFrame:
    dfs = []
    for year in range(start, end+1):
        dfs.append(load_df_with_year(f'parsed_data/{year}.csv', year))
    
    return pd.concat(dfs)

merge_csvs().to_csv(
    path_or_buf='combined_data/all.csv',
    sep=',',
    index=False
)