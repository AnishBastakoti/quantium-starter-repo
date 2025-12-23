import pandas as pd
from pathlib import Path

def process_pink_morsels_data():
    # Define data directory
    data_dir = Path("data")

    # List of input CSV files
    input_files = [
        data_dir / "daily_sales_data_0.csv",
        data_dir / "daily_sales_data_1.csv",
        data_dir / "daily_sales_data_2.csv",
    ]

    # Read and combine all CSV files
    dataframes = [pd.read_csv(file) for file in input_files]
    df = pd.concat([pd.read_csv(file) for file in input_files], ignore_index=True)

    # Filter for Pink Morsels only
    df["product"] = df["product"].str.strip().str.lower()
    df = df[df["product"] == "pink morsel"]

    # Clean price column: remove '$' and convert to float
    df["price"] = (
        df["price"]
        .str.replace("$", "", regex=False)
        .astype(float)
    )

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Select and rename required columns
    final_df = df[["Sales", "date", "region"]].rename(
        columns={
            "date": "Date",
            "region": "Region"
        }
    )

    # Write output CSV
    output_file = data_dir / "pink_morsels_sales.csv"
    final_df.to_csv(output_file, index=False)

    print(f"Processed data saved to: {output_file}")
    print(f"Total records: {len(final_df)}")


if __name__ == "__main__":
    process_pink_morsels_data()
