import pandas as pd
from datetime import datetime


def main():
    file = r"C:\temp\POD_LIST.CSV"

    df = pd.read_csv(file, header=None, encoding="utf-8", dtype=str)
    df.columns = ["item", "purchase_price", "supplier", "received_dt", "chg_value"]
    # drop if received_dt is NaN
    df.dropna(subset=["received_dt"], inplace=True)

    df["purchase_price"] = df["purchase_price"].astype(float)
    df["chg_value"] = df["chg_value"].astype(float)

    df.dropna(subset=["chg_value"], inplace=True)

    df = df[
        (df["purchase_price"] != df["chg_value"])
        & df["chg_value"].notnull()
        & df["chg_value"]
        > 0
    ]

    output = f"POD_LIST_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
    
    df.drop_duplicates(subset=["item", "received_dt"], inplace=True)

    df.to_excel(output, index=False)

    return df


if __name__ == "__main__":
    df = main()
