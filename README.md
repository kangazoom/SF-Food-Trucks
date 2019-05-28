
## San Francisco Food Truck Finder
This CLI program uses data from [The City of San Francisco's Food Truck API](https://dev.socrata.com/foundry/data.sfgov.org/jjew-r69b) to tell users which San Francisco-area food trucks are currently open. Mobile Food Schedule

## Installation
- Clone this repo
- Navigate into the project directory
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
- Optional: Register and obtain an 'App Token' from the SF Data website (the app will still work without on, but you may run into throttling issues) [here](https://dev.socrata.com/docs/app-tokens.html)
- Add the following text to a .env file but replace the `{YOUR_APP_TOKEN}` value with your own:
```
APP_TOKEN="{YOUR_APP_TOKEN}"
```

## Usage
Execute the app from the command line via one of the following options:
```
# Homebrew-installed Python 3.x on Mac OS, not using Pipenv:
python3 show_open_food_trucks.py

# All others, including Pipenv on Mac or Windows:
python show_open_food_trucks.py
```




3. A one- or two-paragraph write-up that is no more than 250 words describing, at a high level, what you would do differently if you were asked to build this as a full-scale web application. In your write-up, please focus on the technical differences between the command-line program and the web application, rather than on the product differences. 


If I built this as a full-scale web application, I would do a few things differently. 

In its current form, the app makes a GET request each time the user indicates they would like to view more trucks. As a web app, I would cache or store all of or most of the results (in back or front end?) and serve the ten-truck list to the user from that location instead. 

Instead of relying on the client-side to determine an accurate timestamp, I would rely on the server side.