# Context managers - provide a way to manage resources ,
#  ensuring that they are properly set up and cleaned up.
#  They are commonly used with the 'with'statement.

# Assignment1. Context manager thatautomatically opens and closes a file

class FileContextManager:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode= mode

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Usage
with FileContextManager('example.txt', 'r') as file:
    contents = file.read()
    print(contents)


# 2.Database connection context manager

import sqlite3

class DatabaseConnection:
    def __init__(self,dbname):
        self.dbname = dbname

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbname)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

# Usage
with DatabaseConnection('mydatabase.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable")
    results = cursor.fetchall()
    print(results)

# 3.Multithreading and multiprocesssing that allows us to run a fn for diff amts of time

# Multithreading
import threading
import time

def count_down(name, duration):
    print(f"{name} started")
    for i in range(duration, 0,-1):
        print(f"{name}: {i} seconds remaining")
        time.sleep(i)
    print(f"{name} finished")

# Create thread objects
thread1 = threading.Thread(target=count_down,args= ("Thread 1",5))
thread2 = threading.Thread(target=count_down,args= ("Thread 2",3))

# Start the threads
thread1.start()
thread2.start()

# wait for both threads to complete
thread1.join()
thread2.join()

print("Threads completed")

# Multiprocessing ex

import multiprocessing
import time

def count_down(name, duration):
    print(f"{name} started")
    for i in range(duration, 0,-1):
        print(f"{name}: {i} seconds remaining")
        time.sleep(i)
    print(f"{name} finished")

# Create process objects
process1 = multiprocessing.Process(target=count_down,args= ("Process 1",5))
process2 = multiprocessing.Process(target=count_down,args= ("Process 2",3))

# Start the process
process1.start()
process2.start()

# wait for both process to complete
process1.join()
process2.join()



