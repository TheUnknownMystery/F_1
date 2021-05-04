import os
import shutil
import time

File_Path_Input = input("Please Enter File Path")
S = time.time()

if(os.path.exists(File_Path_Input)):

    FileAndFolder = os.walk(File_Path_Input)

    AllFiles = os.path.join(str(File_Path_Input) + '/' + str(FileAndFolder))
    C_Time_1 = os.stat(File_Path_Input).st_ctime

    if(C_Time_1 < 30):
        shutil.rmtree(File_Path_Input)
        print("Done")
else:
    print("Sorry Path not found")
