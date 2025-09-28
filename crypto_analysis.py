"""
A simple script to download and analyze historical cryptocurrency price data.

This script uses the yfinance library to download price data for a given symbol
(e.g., BTC-USD) and calculates moving averages. It then outputs a summary of the
closing prices and moving averages.
"""

import pandas as pd
import yfinance as yf


def fetch_data(symbol: str, start: str = "2020-01-01", end: str = None) -> pd.DataFrame:
    """
    Fetch historical price data for a cryptocurrency symbol using yfinance.

    Args:
        symbol (str): The ticker symbol, e.g., 'BTC-USD' or 'ETH-USD'.
        start (str): Start date in YYYY-MM-DD format.
        end (str): End date in YYYY-MM-DD format (defaults to today if None).
    Returns:
        pd.DataFrame: Historical price data with datetime index.
    """
    data = yf.download(symbol, start=start, end=end)
    return data


def add_moving_averages(df: pd.DataFrame, windows=[20, 50]):
    """
    Add moving average columns to the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with price data.
        windows (list): List of window sizes for moving averages.
    """
    for window in windows:
        df[f"MA{window}"] = df["Close"].rolling(window=window).mean()


def main():
    symbol = "BTC-USD"
    df = fetch_data(symbol)
    add_moving_averages(df, windows=[20, 50, 100])
    print(df.tail())


if __name__ == "__main__":
    main()
