__author__ = 'luosm'
import random
import redis

def setRedisRandom(r):
    for x in xrange(95, 100):
        rv = random.uniform(x , x + 10)
        r.zadd('myZaddTest', x, rv)
        print 'random is %r' % random.uniform(10, x)

    #
    index = 0
    for x in r.zrange('myZaddTest', 0, -1, True):
        index = index + 1
        print 'index %r myZaddTest is' % index , x
