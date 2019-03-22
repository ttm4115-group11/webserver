from flask import Flask 
from flask import jsonify

app = Flask(__name__)

racks = [
    {
        "id": 1,
        "location": u"Hovedbygget, Gløshuagen",
        "latitude": u"64.41947",
        "longditude": u"10.40093", 
        "parkingspots": 20,
        "available_spots": 15
    }
]

@app.route('/')
def index():
    return jsonify({'racks': racks})

if __name__ == "__main__":
    app.run(debug=True)