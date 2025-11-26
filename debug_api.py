import requests

symbol = "AAPL"
api_key = "82W90FO539C5LLIV"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}"

print(f"Requesting URL: {url}")
response = requests.get(url)
data = response.json()
print(f"Response Status: {response.status_code}")
print(f"Response Data: {data}")
