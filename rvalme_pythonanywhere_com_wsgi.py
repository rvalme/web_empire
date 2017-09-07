import tornado.ioloop
import tornado.wsgi
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="My title")

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
	    self.render("about.html", title="My title")

class DiscoHandler(tornado.web.RequestHandler):
    def get(self):
	    self.render("discography.html", title="My title")

class ShowHandler(tornado.web.RequestHandler):
    def get(self):
	    self.render("shows.html", title="My title")

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
	self.render("contact.html", title="My title")
def make_app():
    settings = {'debug': False }
    handlers = [
		(r"/", MainHandler),
		(r"/about.html", AboutHandler),
		(r"/discography.html", DiscoHandler),
		(r"/shows.html", ShowHandler),
		(r"/index.html", MainHandler),
		(r"/contact.html", ContactHandler),
		(r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ]
    return tornado.wsgi.WSGIApplication(handlers, **settings)

application = make_app()
