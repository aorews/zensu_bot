from database import db_query
from datetime import time
from post_scheduler import JOB_DAYS_DURATION, POST_HOUR, POST_MINUTE, POST_WEEKDAY
from bot_functions import CollectData, rebuild_message

def refresh_posts(context):
    q = f"""select jobs.* , date_part('day', now()-created), 0, case when photo_id != 'None' then true else false end
                    from jobs left join post_templates on job_type = type
                    where date_part('day', now()-created) < {JOB_DAYS_DURATION} and type != 0"""
    rows = db_query(q)
    for i, row in enumerate(rows):
        data = CollectData(None, True, *row)
        rebuild_message(context, data)

def refresh_posts_job(job):
    job.run_daily(callback = refresh_posts, time = time(POST_HOUR, POST_MINUTE), days = [x for x in range(POST_WEEKDAY)], name = 'refresh_posts')