from rq import Queue
from rq.registry import FailedJobRegistry
import redis


redis_client = redis.Redis("redis", 6379)
redis_queue = Queue(connection=redis_client)

failed_registry = FailedJobRegistry(queue=redis_queue)


def rq_consume():
    job_ids = failed_registry.get_expired_job_ids()

    for job_id in job_ids:
        job = redis_queue.fetch_job(job_id)
        if job.is_failed:
            job.delete()


if __name__ == '__main__':
    while True:
        rq_consume()
