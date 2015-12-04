import core.core as core
import time

def main():
        TIME=15
	print 'Executing RobotPaolon...'
	api = core.get_api()
	last_mention=core.get_last_mention('RobotPaolon')
	print 'Ultima mencion: '+last_mention.text+' por '+last_mention.user.screen_name
	print '*************************'
	while True:
		print 'Ultima mencion: '+last_mention.text+' por '+last_mention.user.screen_name
		current_last_mention=core.get_last_mention('RobotPaolon')
		print 'Ultima nueva mencion: '+current_last_mention.text+' por '+current_last_mention.user.screen_name
		time.sleep(TIME)
		print 'Nuevo chequeo en 15 segundos...'
		if last_mention.id <> current_last_mention.id:
			mentions=core.get_mentions('RobotPaolon', last_mention.id)
			for m in mentions:
				if m.text.upper() == '@ROBOTPAOLON PIROPEAME':
					print 'Piropeando a '+m.user.screen_name
					core.reply_from_file(m.user.screen_name, 'piropos.txt')
			last_mention=current_last_mention
		else:
			print 'No hay nuevas menciones'


if __name__ == "__main__":
       main()
