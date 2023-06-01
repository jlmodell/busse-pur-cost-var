import pandas as pd
from datetime import datetime

# GET.POD.FOR.VARS

# BUILD: pyinstaller -F -n GET.POD.FOR.VARS.exe -i "C:\Users\jmodell.BUSSEINC0\Pictures\favicon.ico" .\main.py

def main():
    file = r"C:\temp\POD_LIST.CSV"

    df = pd.read_csv(file, header=None, encoding="utf-8", dtype=str)
    df.columns = [
        "item", "purchase_price", "supplier", "received_dt", "chg_value", "status"
    ]

    df.dropna(subset=["received_dt"], inplace=True)

    df["status"] = df["status"].apply(lambda x: "Open" if x == "O" else "Closed")
    df["purchase_price"] = df["purchase_price"].astype(float)
    df["chg_value"] = df["chg_value"].astype(float)
    df["received_date"] = pd.to_datetime(df["received_dt"], format="%m-%d-%y")

    df.dropna(subset=["chg_value"], inplace=True)

    df = df[
        (df["chg_value"].notnull()) & (df["chg_value"] != 0)
    ]        
    
    df.sort_values(by=["item", "received_date"], inplace=True)    
    df.drop_duplicates(subset=["item"], keep="last", inplace=True)

    df = df[df["chg_value"] != df["purchase_price"]]

    df = df[["item","purchase_price","supplier","received_dt","chg_value","status"]]

    output = f"POD_LIST_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"            

    df.to_excel(output, index=False)

    return df


if __name__ == "__main__":
    df = main()
