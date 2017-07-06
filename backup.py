#备份脚本.py
import os
import time
import sys
#备份的源文件路径
sourc = ['C://Other/test','C://Other/Android']
#备份放置路径
target_dir = 'C://'
A
#备份文件的名字
target = target_dir +time.strftime('%Y%m%d%H%M%S')+'.rar'
zip_command = "winrar a %s %s " % (target,' '.join(sourc))
print (zip_command)
if os.system(zip_command) ==0:
    print ("succeed!"+target)
else:
    print ("failed")
    
