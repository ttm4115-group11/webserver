from flask import Flask 
from flask import jsonify
from flask import request
import socket
import json
from werkzeug.datastructures import ImmutableMultiDict


#!/usr/bin/env python
# -*- coding: utf-8 -*-

app = Flask(__name__)


racks = [
    {
        "id": 1,
        "location": u"Hovedbygget, Glshuagen",
        "latitude": u"63.41947",
        "longitude": u"10.40093", 
        "parkingspots": 20,
        "available_spots": 15
    },
    {
        "id": 2,
        "location": u"Torget",
        "latitude": u"63.43012",
        "longitude": u"10.39508", 
        "parkingspots": 30,
        "available_spots": 29
    },
    {
        "id": 3,
        "location": u"Solsiden",
        "latitude": u"63.43427",
        "longitude": u"10.41275", 
        "parkingspots": 10,
        "available_spots": 0
    }

]

reservations = [

]

@app.route('/update/<int:rack_id>', methods=['PUT'])
def addRack(rack_id):
    content = request.json
    
    racks.append({
        "id": rack_id,
        "location": request.json.get('location'),
        "latitude": request.json.get('latitude'),
        "longitude": request.json.get('longitude'),
        "parkingspots": 10,
        "available_spots": 0
    })
    print(racks)
    return 'all good'


@app.route('/reserve/<int:id>', methods=['PUT'])
def reserve(id):
    body = request.form.to_dict()
    print(body)
    reservations.append(body)
    return 'Reservation added'


@app.route('/reservations', methods=["GET"])
def reservation():
    return jsonify(reservations)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'racks': racks})



if __name__ == "__main__":
    app.run(debug=True)

