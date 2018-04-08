#!/Users/dani14lks/anaconda2/bin/python

import numpy
import scipy
import cv2
import matplotlib
import sys
import os
import glob
import shutil

def clean_path(string):
	while string[-1] == '/':
		string = string[:len(string) - 1]

	return string

def load_videos(folder,ext):
	cv2.destroyAllWindows()
	names = []
	realnames = []
	if os.path.isdir(video):
		if ext == "*":
			ext = ""
		names = glob.glob(folder+'/*'+ext)#List
		names = sorted(names)#Sort the list
		realnames = []
		for i in names:
			i = i.replace(folder,'')
			i = i.replace(ext,'')
			i = i.replace('.','')
			i = i.replace('/','')
			realnames.append(i)
	
	return names, realnames

def name2realnames(i,ext):
	i = i.replace(folder,'')
	i = i.replace(ext,'')
	i = i.replace('.','')
	i = i.replace('/','')

	return i

def show_stats(video):
	filename, ext_video = os.path.splitext(video)
	cap = cv2.VideoCapture(video)
	frame_width = int(round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
	frame_height = int(round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
	frames_numbers = int(round(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
	duration = frames_numbers/fps
	print "*************************************"
	print "Video: "+filename+ext_video
	print "Width: "+str(frame_width)
	print "Height: "+str(frame_height)
	print "FPS: "+str(fps)
	print "Number of frames: "+str(frames_numbers)
	print "Duration (seconds): "+str(duration)
	print "*************************************"

def saveALLVideos2Images(video,folder,ext_images,dfolder):
	cv2.destroyAllWindows()
	#print "saveALLVideos2Images"
	ext_video = "mp4"
	if os.path.isdir(video):
		#print "DIR"
		names, realnames = load_videos(video,ext_video)
		if not os.path.exists(folder):
			os.mkdir(folder)
		for nam in names:
			realnam = name2realnames(os.path.basename(nam),ext_video)
			nfolder = folder+"/"+realnam
			saveVideo2Images(nam,nfolder,ext_images)
	elif os.path.isfile(video):
		#print "FILE"
		saveVideo2Images(video,folder,ext_images)
	else:
		exit(1)

def saveVideo2Images(video,folder,ext_images):
	cv2.destroyAllWindows()
	print "saveVideo2Images"
	print video
	print folder
	print ext_images
	if os.path.isfile(video):
		if not os.path.exists(folder):
			os.mkdir(folder)
		filename, ext_video = os.path.splitext(os.path.basename(video))
		cap = cv2.VideoCapture(video)
		show_stats(video)
		cont = 1
		while(1):
			ret, frame = cap.read()
			n_cont = str(cont).rjust(6,'0')
			if ret==False or cont>999999:
				cap.release()
				cv2.destroyAllWindows()
				break
			cv2.imwrite(folder+'/'+filename+'_frame'+n_cont+'.'+ext_images, frame)
			cont = cont + 1
	else:
		exit(1)

if len(sys.argv) > 4 or len(sys.argv) < 2:
	print len(sys.argv)
	print sys.argv
	print "USE: video2frames.py video [folder [ext_images]]"
	print "video: Name of the video or the folder with the original videos"
	print "folder: Name of the new folder to save the frames there. IF VOID: NAME OF THE 'VIDEO' WILL BE USED"
	print "ext_images: File extension of the frames. IF VOID: 'JPG' WILL BE USED"
	exit(1)

cv2.destroyAllWindows()
#print sys.argv
video = clean_path(sys.argv[1])
#print os.path.splitext(video)
filename, ext_video = os.path.splitext(video)
video = clean_path(sys.argv[1])
#print os.path.splitext(video)
folder = filename
dfolder = True#Says if the default folder will be used
ext_images = "jpg"

if len(sys.argv) == 4:
	folder = clean_path(sys.argv[2])
	dfolder = False#Says if the default folder will be used
	ext_images = sys.argv[3]

if len(sys.argv) == 3:
	folder = clean_path(sys.argv[2])
	dfolder = False#Says if the default folder will be used
	print sys.argv
	print "Param 'ext_images' void, 'jpg' will be used"
	print "*************************************************************************"

if len(sys.argv) == 2:
	print sys.argv
	print "Param 'folder' void, '"+video+"' will be used"
	print "Param 'ext_images' void, 'jpg' will be used"
	print "*************************************************************************"

saveALLVideos2Images(video,folder,ext_images,dfolder)
cv2.destroyAllWindows()
exit(0)

