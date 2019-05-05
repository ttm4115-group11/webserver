# Web Server
This is a simple webserver running [Flask](http://flask.pocoo.org/) that servers both the Android app in [this repository](https://github.com/ttm4115-group11/phone-app), and the bike racks in [this repository](https://github.com/ttm4115-group11/bike-rack). 

## Run the server 
To run the server do the following. 
* We highly recommend you run this in a Python Virtual Environment
* `pip install -r requirements.txt`
* `FLASK_APP=app.py`
* `flask run`

To expose the server over the IP of your computer, which is needed to for example test the server togehter with an Android device, run the last command like this: `flask run --host=0.0.0.0` 
