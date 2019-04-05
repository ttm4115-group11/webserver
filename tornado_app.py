import tornado.ioloop
import tornado.web
import json
import tornado.websocket
import tornado.httpserver
import socket

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
        "location": "Torget",
        "leatitude": u"63.43012",
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


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(racks))


class ReserveHandler(tornado.web.RequestHandler):
    def put(self):
        body = json.loads(self.request.body)
        reservations.append(body)
        print(body)
        self.write("All good")


# The pies will poll this for new reservations
class RackHandler(tornado.websocket.RequestHandler):
    def get(self):
        self.write(json.dumps(reservations))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/reserve", ReserveHandler),
        (r"/reservations", RackHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
