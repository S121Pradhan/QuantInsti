#!/usr/bin/env python
 
import sys, time
from daemon import runner
from Algorithm import Algorithm
from DataManager import DataManager
import redis

class Scheduler():

    def __init__(self):
        self.tickNo = 1
        self.dbm = DataManager()
        self.algo = Algorithm(self.dbm)
        self.rCon = redis.Redis(host='localhost', port=6379, db=0)
    
    def run(self):
        while True:
            self.algo.execute(self.tickNo)
            time.sleep(5)
            self.tickNo = self.tickNo + 1

if __name__ == "__main__":
    ns = Scheduler()
    ns.run()
    r.flushdb()