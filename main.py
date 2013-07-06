from get_handler import *
from downloader import Downloader

if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('0.0.0.0', 5454), GetHandler)
	print 'Starting server, use Control-C to stop'
	d = Downloader()
	d.daemon = True
	d.start() 
	server.serve_forever()