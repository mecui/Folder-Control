import os 
import shutil

#name="Scene"
#for a in range (1,31):

  #print (str(name)+str(a))

  #os.makedirs(a)

#src_files=os.listdir("c:\users\mengyaoc\desktop\Camera\in_Door")

#for i in range(1):
#os.mkdir("Scene"+str[])

for ff in range(1,25):  # base on the number of folders. 
  for cc in range(1,11): # base on the number that files you want to move
    path_i = "c:\users\mengyaoc\desktop\Camera\out_Door"   # Here is the directory which you keep your files. 
    path_f= os.path.join(path_i,"Scene"+str(ff))
    fname = os.listdir(path_i)[1]
    before = os.path.join(path_i,fname)
    after = os.path.join(path_f,fname)
    shutil.move(before, after)
    cc = cc+1
  ff = ff + 1 


