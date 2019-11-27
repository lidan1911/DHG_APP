import time
import datetime

t = time.time()
print(t)
print(time.localtime(time.time()))
print(time.localtime())
print(time.asctime(time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("==", datetime.datetime.now())
print(datetime.datetime.today())
print("=====================")
print((datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))