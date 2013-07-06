from threading import *
import time
from subprocess import Popen

class Downloader(Thread):
	run = True
	def run(self):
	#	try:
			while(self.run):
				try:
					pending = open("pending.txt","r+")
					for video in pending:
						download = Popen(['youtube-dl',video])
					pending.truncate(0)	
					pending.close()
					Popen(['chmod','agustin:users','*.mp4'])
					Popen(['mv','*.mp4','/volume1/Videos/'])
				except:
					print "No pending.txt file found, or other unknown error, sleeping 20 secs"
					time.sleep(15)
				finally:
					time.sleep(5)
	#	except (KeyboardInterrupt, SystemExit):
	#			self.run = False
