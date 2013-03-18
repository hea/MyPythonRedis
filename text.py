__author__ = 'luosm'

import config
import time
import datetime
import redis
import randomTest


pool = redis.ConnectionPool(host=config.REDIS_IP, port=config.REDIS_PORT, db=config.REDIS_DBINDEX)
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    # simple key test
    r.set('key', 'value')
    #print ('key value is %s', r.get('key'))
    #print some random
    randomTest.setRedisRandom(r)

    print r.get('key2')
    # create pipeline##
    pipe = r.pipeline()
    pipe.set('pipeTest', 'pipeValue')
    print pipe.get('pipeTest')
    print pipe.execute()
    #print ('current time is %i', datetime.datetime.now())

