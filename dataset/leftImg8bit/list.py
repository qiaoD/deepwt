import os.path

dirVal = './val'

dirTrain = './train'

fileList = []
def getAllFiles(dir):
	if(os.path.isfile(dir)):
		fileList.append(dir[7:-16])
	else :
		for path in os.listdir(dir):
			getAllFiles(os.path.join(dir,path))
		
		

		
if __name__ == '__main__':
	getAllFiles(dirTrain)
	ValTxt = '../val.txt'
	TrainTxt = '../train.txt'
	with open(TrainTxt, 'w+') as fp:
		for img in fileList:
			fp.write(img+'\n')




