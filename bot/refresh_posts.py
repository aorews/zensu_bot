import logging
from database import db_query
from datetime import time
from constants import JOB_DAYS_DURATION, POST_HOUR, POST_MINUTE, POST_WEEKDAY
from post_updater import PostUpdater

logger = logging.getLogger(__name__)

def refresh_posts(context):
    q = f"""select jobs.* , date_part('day', now()-created), 0, case when photo_id != 'None' then true else false end
                    from jobs left join post_templates on job_type = type
                    where date_part('day', now()-created) < {JOB_DAYS_DURATION} and type != 0"""
    rows = db_query(q)
    logger.info("Refreshing posts.")
    for row in rows:
        logger.info(f"Refreshing post: {row}")
        # Example of on demand PostUpdater
        upd = PostUpdater(row)
        upd.rebuild_message(context)

def refresh_posts_job(job):
    job.run_daily(callback = refresh_posts, time = time(POST_HOUR, POST_MINUTE), days = [x for x in range(POST_WEEKDAY)], name = 'refresh_posts')
