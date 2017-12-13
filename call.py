import os

# we declare a variable which stores the image captured by name cap_image.jpg
img='/home/cool/cap_image.jpg'


while True:

# we run an opencv programe to capture the image
  os.system('python cam1.py')

# we supply the captured image to tensorflow program for image classification
  os.system('python tf_files/label_image.py '+img+'>a')

# finally we write the prediction on the image to display
  os.system('python cam.py')
  
