from os import listdir
from os.path import isfile , join
files_list=[f for f in listdir('/Users/Zuha Butt//Desktop') if isfile(join('/Users/Zuha Butt/Desktop',f))]
print(files_list)
