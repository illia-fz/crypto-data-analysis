import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


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


def add_moving_averages(df: pd.DataFrame, windows=[20, 50]) -> pd.DataFrame:
    """
    Add moving average columns to the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with price data.
        windows (list): List of window sizes for moving averages.

    Returns:
        pd.DataFrame: DataFrame with added moving average columns.
    """
    for window in windows:
        df[f"MA_{window}"] = df['Close'].rolling(window=window).mean()
    return df


def plot_price_and_ma(df: pd.DataFrame, symbol: str, windows=[20, 50]) -> None:
    """
    Plot closing prices and moving averages.

    Args:
        df (pd.DataFrame): DataFrame containing price and moving average data.
        symbol (str): The ticker symbol for the cryptocurrency.
        windows (list): List of moving average windows plotted.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Close'], label='Close Price')
    for window in windows:
        plt.plot(df.index, df[f"MA_{window}"], label=f"MA{window}")
    plt.title(f"{symbol} Price with Moving Averages")
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.tight_layout()
    # Note: In a non-interactive environment, plt.show() may not display a window,
    # but including it for completeness.
    plt.show()


def main():
    symbol = 'BTC-USD'
    start_date = '2020-01-01'
    df = fetch_data(symbol, start=start_date)
    windows = [20, 50]
    df = add_moving_averages(df, windows)
    # Print the last few rows of the DataFrame with moving averages
    print(df[['Close'] + [f"MA_{w}" for w in windows]].tail())
    # Plot the data
    plot_price_and_ma(df, symbol, windows)


if __name__ == '__main__':
    main()
