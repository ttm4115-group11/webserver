import tornado.ioloop
import tornado.web
import json

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


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(racks))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
