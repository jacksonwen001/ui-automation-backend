import datetime
import threading

thread_local = threading.local()
data = {}

def test(name: str): 
  data['name'] = name
  print('time: {}, thread: {}, data: {}'.format(datetime.datetime.now(), threading.current_thread().name, data))


if __name__ == "__main__":

  t = threading.Thread(target=test, args=('a'), name="thread-a")
  t2 = threading.Thread(target=test, args=('b'), name="thread-a")

  t.start()
  t2.start()
  t.join()
  t2.join()
  
