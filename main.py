from get_handler import *
if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('localhost', 5454), GetHandler)
	print 'Starting server, use  to stop'
	server.serve_forever()