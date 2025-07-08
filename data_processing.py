import pandas as pd

def load_transactions(file):
    df = pd.read_csv(file)
    df.columns = [col.strip() for col in df.columns]
    df["Amount"] = df["Amount"].astype(str).str.replace(",", "").astype(float)
    df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")
    return df

def categorize_transactions(df, categories):
    df["Category"] = "Uncategorized"
    for cat, keywords in categories.items():
        if cat == "Uncategorized":
            continue
        for idx, row in df.iterrows():
            details = row["Details"].lower().strip()
            for keyword in keywords:
                if keyword.lower().strip() in details:
                    df.at[idx, "Category"] = cat
                    break
    return df