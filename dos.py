#byDT
import requests
import threading
 
class myThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print("开始" + self.name)
        while True:
            try:
                crawler(self.name)
            except:
                break
        print("结束" + self.name)
 
# 定义功能函数，访问固定url地址
def crawler(threadName):
    url = "http://doit.am"
    try:
        r = requests.get(url,timeout = 20)
        # 打印线程名和响应码
        print(threadName,r.status_code)
    except Exception as e:
        print(threadName,"错误:",e)
 
# 创建线程列表
threads = []
 
# 开启线程
for i in range(999):
    # 给每个线程命名
    tName="线程-"+str(i)
    thread=myThread(tName)
    thread.start()
    # 将线程添加到线程列表
    threads.append(thread)
    
#等待所有线程完成
for t in threads:
    t.join()