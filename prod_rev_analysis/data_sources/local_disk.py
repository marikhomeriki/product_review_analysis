import pandas as pd
import os
from colorama import Fore, Style
from product_review_analysis.ml_logic.params import LOCAL_DATA_PATH

def get_pandas_chunk(path: str,
                     index: int,
                     chunk_size: int,
                     dtypes,
                     columns: list = None,
                     verbose=True) -> pd.DataFrame:
    """
    return a chunk of the raw dataset from local disk or cloud storage
    """
    path = os.path.join(
        os.path.expanduser(LOCAL_DATA_PATH),
        "processed" if "processed" in path else "raw",
        f"{path}.csv")

    if verbose:
        print(Fore.MAGENTA + f"Source data from {path}: {chunk_size if chunk_size is not None else 'all'} rows (from row {index})" + Style.RESET_ALL)

    try:

        df = pd.read_csv(
                path,
                skiprows=index + 1,  # skip header
                nrows=chunk_size,
                dtype=dtypes,
                header=None)  # read all rows

        # read_csv(dtypes=...) will silently fail to convert data types, if column names do no match dictionnary key provided.
        if isinstance(dtypes, dict):
            assert dict(df.dtypes) == dtypes

        if columns is not None:
            df.columns = columns

    except pd.errors.EmptyDataError:

        return None  # end of data

    return df

def save_local_chunk(path: str,
                     data: pd.DataFrame,
                     is_first: bool):
    """
    save a chunk of the dataset to local disk
    """

    path = os.path.join(
        os.path.expanduser(LOCAL_DATA_PATH),
        "raw" if "raw" in path else "processed",
        f"{path}.csv")

    print(Fore.BLUE + f"\nSave data to {path}:" + Style.RESET_ALL)

    data.to_csv(path,
                mode="w" if is_first else "a",
                header=is_first,
                index=False)
