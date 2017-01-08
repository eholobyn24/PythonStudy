import os
import time
import datetime

paramfile = 'ParamFile.txt'
resultfile = 'Result.txt'

def OpenParamFile():
    
    path = os.path.join('C:/Users/erich/Documents/', paramfile)
    with open(path) as f:
        networks = f.read().splitlines()
    PingTest(networks)    

def PrinttoFile(x):
    
    path = os.path.join('C:/Users/erich/Documents/', resultfile)
    p = open(path, 'a')
    text = x + '\n'
    p.write(text)
    p.close()

def PingTest(y):
    while(True):
        
        for i in y:
            
            ping = os.system('ping ' + i)
            ts = datetime.datetime.utcnow()
            print(ts)
          
            if ping == 1:
                result = 1
                print('Ping could not reach ' + str(i) + ' Result: ' + str(ping))
                PrinttoFile(str(ts) + ': Failed to connect to network')
                time.sleep(60)
                
            else:
                result = 0
                print('Ping could reach ' + str(i) + ' Result: ' + str(ping))
                               
        time.sleep(15)
       
if __name__ == '__main__':
    OpenParamFile()
    




