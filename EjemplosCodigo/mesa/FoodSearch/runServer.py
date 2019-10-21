# -*- coding: utf-8 -*-
#runServer.py: starts the server (visualisation in the web-browser)

from server import server   #Imports the setup of the server
server.port = 8521  # Sets the port on which the server will listen
server.launch()     # launches the server