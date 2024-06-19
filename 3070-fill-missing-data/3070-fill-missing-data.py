import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    df['quantity'] = products['quantity'].fillna(0)
    return df