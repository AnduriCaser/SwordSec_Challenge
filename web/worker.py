from rq import Connection, Queue, Worker
import redis


redis_client = redis.Redis("redis", 6379)
qs = ['high', 'low', 'default']


if __name__ == '__main__':
    with Connection(redis_client):
        w = Worker(qs)
        w.work(burst=True)
