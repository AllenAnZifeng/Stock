from Price import Price
from typing import List
from Data import Data


def parse_price_data(file_path) -> Data:
    price_data = []
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Find the start of actual data (header line "date,open,high,low,close,volume")
    for i, line in enumerate(lines):
        if line.strip().startswith("date,open,high,low,close,volume"):
            data_lines = lines[i+1:]  # Extract lines after the header
            break
    else:
        raise ValueError("No valid data header found in the file.")

    # Process the data lines
    for line in data_lines:
        parts = line.strip().split(",")
        if len(parts) == 6:  # Ensure valid row format
            date, open_price, high, low, close, volume = parts
            price_data.append(
                Price(date, open_price, high, low, close, volume))

    return Data(price_data)


if __name__ == "__main__":
    data = parse_price_data("MacroTrends_Data_Download_QQQ.csv")
    # print(data.price_data[0].date.year)
