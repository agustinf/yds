from BaseHTTPServer import BaseHTTPRequestHandler
import os
import urlparse
import url_validator

class GetHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		message = '<html><body><form method="POST"> <input type="text" name="url"/></form><body></html>' 
		self.send_response(200)
		self.end_headers()
		self.wfile.write(message)
		return
	def do_POST(self):
		execute = None
		length = int(self.headers['Content-Length'])
		post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
		for key, value in post_data.iteritems():
			if(key=="url" and value[0] and url_validator.validate(value[0])):
				execute = 'youtube-dl ' + value[0]
		self.send_response(200)
		self.end_headers()
		if (execute):
			os.system(execute)
			os.system('mv *.mp4 /@volume1/')
			self.wfile.write("executed " + execute)
		else:
			self.wfile.write("error")
		return