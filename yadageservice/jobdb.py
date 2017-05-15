import redis
import os
def wflow_job_db():
   return redis.StrictRedis(
                host = os.environ.get('YADAGE_JOBDB_REDIS_HOST','localhost'),
                db   = os.environ.get('YADAGE_JOBDB_REDIS_DB',0),
                port = os.environ.get('YADAGE_JOBDB_REDIS_PORT',6379),
)

db = wflow_job_db()

def register_job(jobguid, resultdir):
	db.set('yadagesvc:{}:resultdir'.format(jobguid),resultdir)

def resultdir(jobguid):
	return db.get('yadagesvc:{}:resultdir'.format(jobguid))
