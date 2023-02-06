import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import os
import string
import os
import moviepy.video.io.ImageSequenceClip
from PIL import Image
import glob





def makeMovie_GWcatalogSize(fps=20, duration=60):
	'''
	whichRate = 'intrinsic' or 'observed'
	fps=0.4, frames per second
	duration = duration of the movie 
	'''




  
	image_folder = '/Users/floorbroekgaarden/Projects/GitHub/OtherPlots/GWcatalogMovie/'

	images = []

	for ind_im  in range(200):
			images.append(image_folder +   'GWcatalogSize_'  + str(ind_im) + '.png')



	image_files = images
	clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
	clip.write_videofile(image_folder+'movie_'+ 'GWcatalogSize'  + '.mp4')


	# make also gif:
 
	# Create the frames
	frames = []
	# imgs = glob.glob("*.png")
	for i in images:
	    new_frame = Image.open(i)
	    frames.append(new_frame)
	 
	# Save into a GIF file that loops forever
	frames[0].save(image_folder+'gif_'+ 'GWcatalogSize' +  '.gif', format='GIF',
	               append_images=frames[1:],
	               save_all=True,
	               duration=duration, loop=0)


	print('done')
	return 




def makeMovie_GWcatalogSize_log(fps=20, duration=60):
	'''
	whichRate = 'intrinsic' or 'observed'
	fps=0.4, frames per second
	duration = duration of the movie 
	'''




  
	image_folder = '/Users/floorbroekgaarden/Projects/GitHub/OtherPlots/GWcatalogMovie/'

	images = []

	for ind_im  in range(200):
			images.append(image_folder +   'GWcatalogSize_log_'  + str(ind_im) + '.png')



	image_files = images
	clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
	clip.write_videofile(image_folder+'movie_'+ 'GWcatalogSize_log'  + '.mp4')


	# make also gif:
 
	# Create the frames
	frames = []
	# imgs = glob.glob("*.png")
	for i in images:
	    new_frame = Image.open(i)
	    frames.append(new_frame)
	 
	# Save into a GIF file that loops forever
	frames[0].save(image_folder+'gif_'+ 'GWcatalogSize_log' +  '.gif', format='GIF',
	               append_images=frames[1:],
	               save_all=True,
	               duration=duration, loop=0)


	print('done')
	return 





#####




Movie_GWcatalogSize=True








# Run rhis using python 3!! 

if Movie_GWcatalogSize==True:
	makeMovie_GWcatalogSize()
	makeMovie_GWcatalogSize_log()



