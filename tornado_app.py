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


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('129.241.104.233', 8888))
        s.send(b"hlep")
        s.close()
        s.shutdown(socket.SHUT_RDWR)
        self.write(json.dumps(racks))

class ReserveHandler(tornado.web.RequestHandler):
    def put(self):
        body = json.loads(self.request.body)
        print(body)
        self.write("All good")

class RackHandler(tornado.websocket.WebSocketHandler):
    conns = set()

    def open(self):
        self.conns.add(self)
        print("New connection")
        self.write("Connected!")

    def on_message(self, message):
        print("Got message: ", message)
        self.write_message("Received: " + message)

    def on_close(self):
        self.conns.remove(self)
        print("Closed!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/reserve/", ReserveHandler)
        (r"/ws", ReserveHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
