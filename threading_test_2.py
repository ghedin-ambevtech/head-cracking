import threading
import time

ls = []

def count(n:int):
   for i in range(1, n+1) :
       print(f'pri contagem {i}')
       ls.append(f'pri contagem {i}')
       time.sleep(0.01)

def count_2(n:int):
   for i in range(1, n+1) :
       print(f'seg contagem {i}')
       ls.append(f'seg contagem {i}')
       time.sleep(0.02)
       
x = threading.Thread(target=count, args=(10, ))
x.start()

y = threading.Thread(target=count_2, args=(10, ))
y.start()


x.join()
y.join()
    
print("Done!!")    
print(ls)
