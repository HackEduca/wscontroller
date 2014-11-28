import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import threading
import time
#import scratch
import json
import sys
import os
import socket
from Tkinter import *

s = None
scratchProgress = None
connectToScratch = None
webServerProgress = None

# Handle the WebSocket requests
class WSHandler(tornado.websocket.WebSocketHandler): 
	def on_message(self, message):
		global s
		data = json.loads (message)
		print (data)
		if (isinstance (data, list)):
			for toBroadcast in data:
				if (s is not None):
					s.broadcast (toBroadcast)
		if (isinstance (data, dict)):
				if (s is not None):
					s.sensorupdate (data)

class ConnectToScratch (threading.Thread):
	def run(self):
		global s
		global scratchProgress
		while (s == None):
			try:
				s = scratch.Scratch()
			except Exception:
				time.sleep (1)
		scratchProgress.set ("Connected")

class WebServer(threading.Thread):
	def run (self):
		if getattr(sys, 'frozen', None):
			basedir = sys._MEIPASS
			htDocs = basedir + "/htdocs/"
		else:
			htDocs = "./htdocs/"
 
		application = tornado.web.Application([
			(r'/ws', WSHandler),
			(r'/(.*)', tornado.web.StaticFileHandler, {'path': htDocs, "default_filename": "index.html"}),
		])
		http_server = tornado.httpserver.HTTPServer (application)
		http_server.listen(8888)
		webServerProgress.set ("Started")
		tornado.ioloop.IOLoop.instance ().start ()

# shut down the current tornado service
	def stop (self):
		tornado.ioloop.IOLoop.instance ().stop ()

class UI(Frame):
	web = None

	def runWebServer(self):
		self.web = WebServer()
		self.web.start ()

	def exitApplication (self):
		if (self.web is not None):
			self.web.stop ()
		sys.exit ()

	def createWidgets(self):
		global webServerProgress

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('google.com', 0))
		ip = s.getsockname()[0]

		self.IPLabel = Label (self, text="Address:").grid (row=0, column=0)
		self.IP = Label (self, text="http://" +ip + ":8888/").grid (row=0, column=1)

		scratchProgress = StringVar ()
		scratchProgress.set ("Connecting...")
		self.ScratchLabel = Label (self, text="Scratch:").grid (row=1, column=0)
		self.ScratchProgress = Label (self, textvariable=scratchProgress).grid (row=1, column=1)

		webServerProgress = StringVar ()
		webServerProgress.set ("Starting...")
		self.WebServerLabel = Label (self, text="Web Server:").grid (row=2, column=0)
		self.WebServerProgress = Label (self, textvariable=webServerProgress).grid (row=2, column=1)

		

		self.QUIT = Button(self)
		self.QUIT["text"] = "Quit"
		self.QUIT["fg"]   = "red"
		self.QUIT["command"] =  self.exitApplication

		self.QUIT.grid(row=3,column=1)


	def __init__(self, master=None):
		global connectToScratch
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		connectToScratch = ConnectToScratch ()
		connectToScratch.start()
		self.runWebServer ()


root = Tk ()
app = UI(master = root)
root.title ("HTML5 Controller")
app.mainloop ()
root.destroy ()
