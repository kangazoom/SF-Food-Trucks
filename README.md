
## San Francisco Food Truck Finder
This CLI application uses data from [Data SF's Mobile Food Schedule API](https://dev.socrata.com/foundry/data.sfgov.org/jjew-r69b) to tell users which San Francisco-area food trucks are currently open.

## Installation
- Run this app in Python 3.6 (or get it [here](https://realpython.com/installing-python/))
- Clone this repo
- From the command line, navigate into the project directory
- Install package dependencies via one of the following options:
```
# Pipenv on Mac or Windows:
pipenv install -r requirements.txt

# Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

## Setup
- Optional: Register and obtain an app token from the Socrata Open Data API (the app will still work without one, but you may run into throttling issues) [here](https://dev.socrata.com/docs/app-tokens.html)
- If you obtained an app token, add the following text to a `.env` file but replace the `YOUR_APP_TOKEN` value with your own:
```
APP_TOKEN="YOUR_APP_TOKEN"
```

## Usage
Execute the app from the command line via one of the following options:
```
# Homebrew-installed Python 3.x on Mac OS, not using Pipenv:
python3 show_open_food_trucks.py

# All others, including Pipenv on Mac or Windows:
python show_open_food_trucks.py
```