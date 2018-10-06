import os.path

dirVal = './val'

dirTrain = './train'

fileList = []
def getAllFiles(dir):
	if(os.path.isfile(dir)):
		fileList.append(dir[5:-16])
	else :
		for path in os.listdir(dir):
			getAllFiles(os.path.join(dir,path))
		
		

		
if __name__ == '__main__':
	getAllFiles(dirVal)
	ValTxt = '../val.txt'
	with open(ValTxt, 'w+') as fp:
		for img in fileList:
			fp.write(img+'\n')




