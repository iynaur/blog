import os
path = './bin_picking/jpg/'
count = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,str(count)+".jpg"))
    count+=1
	
path = './bin_picking/bmp/'
count = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,str(count)+".bmp"))
    count+=1