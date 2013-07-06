from BaseHTTPServer import BaseHTTPRequestHandler
from subprocess import Popen
import urlparse
import url_validator
import time

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
		self.send_response(200)
		self.end_headers()
		if (video):
			p = Popen(['youtube-dl',video])
			self.wfile.write("will download "+video)
			while(not Popen.poll(p)):
				time.sleep(1)
			os.system('chown agustin:users *.mp4')
			os.system('mv *.mp4 /volume1/Videos/')
		else:
			self.wfile.write("error")
		return