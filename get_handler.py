from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import url_validator
import time
import os

class GetHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		message = '<html><body><form method="POST"> <input type="text" name="url"/></form><body></html>' 
		self.send_response(200)
		self.end_headers()
		self.wfile.write(message)
		return
	def do_POST(self):
		video = None
		length = int(self.headers['Content-Length'])
		post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
		for key, value in post_data.iteritems():
			if(key=="url" and value[0] and url_validator.validate(value[0])):
				video = value[0]
		if (video):
			self.send_response(200)
			self.end_headers()
			self.wfile.write("will download "+video)
			self.wfile.flush()
			job = open("pending.txt","a")
			job.write(video + "\n")
			job.close()
			#download = Popen(['youtube-dl',video], stdout=PIPE)
		else:
			self.wfile.write("error")
		return