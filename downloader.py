from threading import *
import time
from subprocess import Popen
import re

class Downloader(Thread):
	run = True
	def run(self):
	#	try:
			while(self.run):
				try:
					queue = []
					patience = 2000
					pending = open("pending.txt","r+")
					for video in pending:
						queue.append(video)
					pending.truncate(0)	
					pending.close()
					for video in queue:
						download = Popen(['youtube-dl',video, '-o', "/volume1/Videos/%(title)s.%(ext)s"])
						while(download.poll() is None and patience > 0):
							time.sleep(3)
							patience -= 1
				except:
					print "No pending.txt file found, or other unknown error, sleeping 20 secs"
					time.sleep(15)
				finally:
					time.sleep(5)
	#	except (KeyboardInterrupt, SystemExit):
	#			self.run = False
