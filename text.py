__author__ = 'luosmT'

import time
import datetime
import redis


pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    # simple key test
    r.set('key', 'value')
    #print ('key value is %s', r.get('key'))


    # create pipeline##
    pipe = r.pipeline()
    pipe.set('pipeTest', 'pipeValue')
    print pipe.get('pipeTest')
    print pipe.execute()
    #print ('current time is %i', datetime.datetime.now())