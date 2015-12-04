import time
import core.core as core

api = core.get_api()

while True:
	
	try:
		mentions=core.get_mentions(api, 'RobotPaolon', None)
		for m in mentions:
			print m.text
		time.sleep(2)

	except TypeError, te:
		print 'Object is not iterable'
		time.sleep(2)
