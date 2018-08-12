import redis

class DataManager:

    def __init__(self):
        self.filepath = 'data.csv'
        self.redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
        self.queueSize = 5
        self.fileP = open(self.filepath)
        self.fileP.readline()
    
    def triggerTick(self, tickNo):
        line = self.fileP.readline().strip()
        if not(line):
            return
        tStampPrice = line.split(',')
        tStamp = int(tStampPrice[0])
        price = float(tStampPrice[1])
        self.redis_db.rpush("prices", price)
        if(tickNo >= self.queueSize):
            self.redis_db.lpop("prices")