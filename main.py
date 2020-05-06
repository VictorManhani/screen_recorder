import numpy as np
import cv2
from PIL import ImageGrab
import datetime

# get time now
now = datetime.datetime.now()

# define the filename
filename = f'output {now.day:02d}.{now.month:02d}.{now.year:04d}.avi'

# define the codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# create the video write object
out = cv2.VideoWriter(filename, fourcc, 15.0, (1366,768))

while True:
	# grab the screen image
	img = ImageGrab.grab()
	
	# convert the pixels to numpy array
	img_np = np.array(img)
	
	# colorize the video with the screen color
	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
	
	# write the frame
	out.write(frame)
	
	# show the result
	cv2.imshow("frame", frame)
	
	# press 'q' to finish the record
	if cv2.waitKey(1) == ord('q'):
		break

# make sure everything is closed when exited
out.release()
cv2.destroyAllWindows()
	
