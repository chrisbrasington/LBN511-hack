from PIL import Image
import urllib,cStringIO
import time
import os
import shutil

# mplayer command for video feed
mplayer = "mplayer mf://*.jpg -mf fps=10"

try:
	# directory to images
	if os.path.exists('img'):
		shutil.rmtree('img')
	os.makedirs('img')
	os.chdir('img')

	#count = 0

	# will run until keyboard interrupt ^C
	while True:
		# ./tmp directory has 0-5 images in real time
		# one image is sequential, but low FPS
		# five images is refreshed out of order, becomes insequential
		for x in range(5):
			url = 'http://192.168.1.1/tmp/'
			url += '_' + `x` + '.jpeg'

			file = cStringIO.StringIO(urllib.urlopen(url).read())
			img = Image.open(file)
			ts = time.time()
			try:
				img.save(`ts` + '.jpg')
			except IOError:
				pass

		# idea for streaming
		# but currently just playing video afterwards

		# if count == 20:
		# 	firstPass = False
		# 	os.system(mplayer)
		# else:
		# 	count += 1
		#time.sleep(1)

except KeyboardInterrupt:
	print "\nFinished"

# play feed
os.system(mplayer)

