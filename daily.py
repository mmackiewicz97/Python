import time
import datetime
import _thread
import os
import shelve
class Task:
    def __init__(self):
        self.name = ""
        self.start =[] 
        self.stop = []
        self.delta = []
        self.current = 0
    def give(self):
        if self.current+1 == len(self.start):
            current_time = time.time()-self.start[self.current]
            print(self.name, time.strftime('%H:%M:%S', time.gmtime(self.start[self.current])), time.strftime(' %M:%S', time.gmtime(current_time)))
        else:
            if len(self.delta) != 0 and self.current>=1:
                print(self.name, time.strftime('%H:%M:%S', time.gmtime(self.delta[self.current-1])))
            else:
                print(self.name)

class Tasks:
    def __init__(self):
        self.tasks = []
        self.commands = { 
            "t": self.task,
            "b": self.begin,
            "s": self.stop,
            "c": self.check,
            "d": self.delete,
            "e": self.edit,
            "r": self.reset,
            "a": self.append,
            "o": self.open,
            "k": self.keys,
            "db": self.dbase
        }
    def task(self,task):
        a = Task()
        a.name = task
        self.tasks.append(a)
    def begin(self, x):
        x = int(x)
        start = time.time()+3600
        self.tasks[x].start.append(start)
        self.tasks[x].name = "\x1b[1;32m{}\x1b[0m".format(self.tasks[x].name)
    def stop(self, x):
        x = int(x)
        stop = time.time()+3600
        task = self.tasks[x]
        task.stop.append(stop)
        delta = task.stop[task.current]-task.start[task.current]
        task.delta.append(delta)
        task.current += 1
    def check(self, x): #mark as done
        x = int(x)
        #self.tasks[x].name = "\x1b[9;32m{}\x1b[0m".format(self.tasks[x].name[7:-4])
        self.tasks[x].name = self.tasks[x].name[7:-4]
        print(self.tasks[x].name[7:-4])
        tim = 0
        for x, i in enumerate(self.tasks[x].delta):
            tim += i
            print(time.strftime('%H:%M:%S', time.gmtime(self.tasks[x].start[x]))," - ", time.strftime('%H:%M:%S', time.gmtime(self.tasks[x].stop[x])),"\t\t",str(datetime.timedelta(seconds=i)).split(".", 1)[0])
        print("\t\t\tSummary: ", str(datetime.timedelta(seconds=tim)).split(".")[0])
        time.sleep(3)
    def reset(self, x):
        if x == "a":
            for t in self.tasks:
                t.name = t.name[7:-4]
                t.start = []
                t.stop = []
                t.delta = []
        else:
            x = int(x)
            t = self.tasks[x]
            t.name = t.name[7:-4]
            t.start = []
            t.stop = []
            t.delta = []
    def delete(self, x):
        x = int(x)
        del self.tasks[x]
    def edit(self, x, new):
        x = int(x)
        self.tasks[x].name = new
    def func(self,x, *args):
        funkcja=self.commands[x]
        return funkcja(*args)
    def show(self):
        os.system("clear")
        print('''\t\t"t":task,
               "b 0": begin,
               "s 0": stop,
               "c 0": check,
               "d 0": delete,
               "e 0": edit,
               "r 0": reset a #all tasks,
               "k 0": print database keys,
               "a [key]": append to database,
               "o [key]": restore from database
               "db [key]": delete database record''')
        for x, t in enumerate(self.tasks):
            print(x," ", end="")
            t.give()
    def append(self, x):
        db = shelve.open("/home/mateusz/pyton/_daily")
        x = str(x)
        #if x in db:
        #    print("Podaj inny klucz")
        #    x = str(input())
        db[x] = [time.strftime('%a %H:%M %d/%m/%y', time.gmtime(time.time())), self.tasks]
        db.close()
    def open(self, x):
        db = shelve.open("/home/mateusz/pyton/_daily")
        x = str(x)
        self.tasks = db[x][1]
        db.close()
    def keys(self, x):
        db = shelve.open("/home/mateusz/pyton/_daily")
        print("Keys in database:")
        for i in db.keys():
            print(i," - ", db[i][0])
        time.sleep(3)
    def check_key(self, x):
        db = shelve.open("/home/mateusz/pyton/_daily")
        if x in db:
            return True
        else:
            return False
        db.close()
    def dbase(self, x):
        db = shelve.open("/home/mateusz/pyton/_daily")
        del db[x]
        db.close()

a = Tasks()
if a.check_key("auto"): 
    a.open("auto")

try:
    while True:
        try:
            a.show()
            time.sleep(1)
        except KeyboardInterrupt:
            x, *r = input().split(" ")
            a.func(x, *r)
            continue
finally:
    a.append("auto")
    exit()
#def get(c):
#    while 1:
#        print(c)
#        x, *r = input().split(" ")
#        a.func(x, *r)
#        time.sleep(1)
#def print_time( threadName, delay):
#   count = 0
#   while count < 5:
#      time.sleep(delay)
#      count += 1
#      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
## Create two threads as follows
#try:
#   _thread.start_new_thread(a.show, ("d", ))
#   _thread.start_new_thread(get, ("Thread-2", ) )
#except:
#   print ("Error: unable to start thread")
#while 1:
#    pass
