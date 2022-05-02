import time
import os
def removeFile():
    fileName = input('Do you want to remove test.txt or test2.txt?: ')
    path = "c:/Users/appro/OneDrive/Desktop/Coding/Project 99/test/" + fileName
    time.time()
    os.path.exists(path)
    os.walk(path)
    os.path.join(path)
    ctime = os.stat(path).st_ctime
    os.path.isfile(path)
    if(os.path.isfile(path)==True):
        os.remove(path)
        print('removal has been successful')
    else:
        print('path not found')
    return ctime
removeFile()