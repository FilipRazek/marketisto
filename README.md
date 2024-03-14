# Marketisto
Use this command-line app to easily fetch data about historical stock market data!



https://github.com/FilipRazek/marketisto/assets/65445960/6c43b8d4-94b6-41c0-99af-0ec37d94ecc5

## Features

- Get up-to-date valuations for stocks since their appearance on the stock market 💸
- Small requests are cached with Redis to avoid straining your API key 🔑
- Quickly compare multiple stocks, their historical valuations and their yearly returns 📈

## Usage

- Clone this repository
- Get a [twelvedata API key](https://twelvedata.com/pricing) (the free tier is sufficient)
- Run `python marketisto.py $API_KEY [stocks-to-compare]` (for example `python marketisto.py demo AAPL`)
