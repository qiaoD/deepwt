import os.path

dir = './val'

fileList = []
def getAllFiles(dir):
	if(os.path.isfile(dir)):
		fileList.append(dir[5:-16])
	else :
		for path in os.listdir(dir):
			getAllFiles(os.path.join(dir,path))
		
		

getAllFiles(dir)
#print(fileList)

with open('val.txt', 'w+') as fp:
	for img in fileList:
		fp.write(img+'\n')




