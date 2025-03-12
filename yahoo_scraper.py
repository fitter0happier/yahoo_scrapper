import boto3
import yfinance as yf
import json

from datetime import datetime, timedelta
from typing import List
from queue import Queue

class YahooScraper:
    def __init__(
        self, tickers: List[str],
        start_date: datetime,
        end_date: datetime, 
        timedelta: timedelta,
        bucket_name: str = None,
        lambda_name: str = "yahoo_scraper_lambda"
    ):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.timedelta = timedelta
        self.bucket_name = bucket_name
        self.lambda_name = lambda_name
        self.bucket_tmp_dir = "yahoo_tmp"
        self.s3_client = boto3.client('s3')
        self.lambda_client = boto3.client('lambda', region_name='us-east-2')
        self.batch_size = 500
        self.files_contents_queue = Queue()

    def get_data(self):
        tickers = yf.Tickers(" ".join(self.tickers))
        print(tickers.news())
