import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
