#byDT
import threading
import requests

def send_request(url):
    response = requests.get(url)
    print(f'{url}: {response.status_code}')

# 创建HTTP请求的URL列表
urls = ["http://doit.am"] * 100000

# 创建线程池
threads = []

# 启动线程发送请求
for url in urls:
    thread = threading.Thread(target=send_request, args=(url,))
    thread.start()
    threads.append(thread)

# 等待所有线程执行结束
for thread in threads:
    thread.join()