import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, header=1)

def table_parse(df: pd.DataFrame) -> pd.DataFrame:
    """Parsing for the HISPANIC OR LATINO ORIGIN BY RACE table.
    """
    df = df[["Geographic Area Name", "Estimate!!Total", "Estimate!!Total!!Not Hispanic or Latino!!White alone", "Estimate!!Total!!Not Hispanic or Latino!!Black or African American alone", "Estimate!!Total!!Not Hispanic or Latino!!American Indian and Alaska Native alone", "Estimate!!Total!!Not Hispanic or Latino!!Asian alone", "Estimate!!Total!!Hispanic or Latino", "Estimate!!Total!!Not Hispanic or Latino!!Some other race alone", "Estimate!!Total!!Not Hispanic or Latino!!Two or more races"]].copy()

    df.columns = ['zip_code', 'total', 'white', 'black', 'indigenous', 'asian', 'latino', 'other', 'multiracial']

    df['zip_code'] = df['zip_code'].str.split().str[1].astype(int)

    df['white_percent'] = df.white / df.total 

    return df

def write_csv(df: pd.DataFrame, path: str):
    df.to_csv(
        path_or_buf=path,
        sep=',',
        index=False
    )

df = read_csv('raw_data/2020.csv')
df = table_parse(df)
write_csv(df, 'parsed_data/2020.csv')