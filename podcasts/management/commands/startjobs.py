import ssl
import logging
import feedparser

from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from django.conf import settings
from django.core.management.base import BaseCommand

from podcasts.models import Episode


logger = logging.getLogger(__name__)

def save_new_episodes(feed):
        podcast_title = feed.channel.title
        podcast_image = feed.channel.image['href']

        for item in feed.entries:
            if not Episode.objects.filter(unique_attribute=item.guid).exists():
                episode = Episode(
                    title=item.title,
                    description=item.description,
                    publication_date=parser.parse(item.published),
                    link=item.link,
                    image=podcast_image,
                    podcast_name=podcast_title,
                    unique_attribute=item.guid,
                )
                episode.save()


def add_realpython_episodes():
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        _feed = feedparser.parse('https://realpython.com/podcasts/rpp/feed')
        save_new_episodes(_feed)


def add_talkpython_episodes():
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        _feed = feedparser.parse('https://talkpython.fm/episodes/rss')
        save_new_episodes(_feed)


def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = 'Runs apscheduler.'

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')

        scheduler.add_job(
            add_realpython_episodes,
            trigger='interval',
            minutes=240,
            id='The Real Python Podcast',
            max_instances=1,
            replace_existing=True,
        )
        logger.info('Added job: The Real Python Podcast.')

        scheduler.add_job(
            add_talkpython_episodes,
            trigger='interval',
            minutes=240,
            id='Talk Python Feed',
            max_instances=1,
            replace_existing=True,
        )
        logger.info('Added job: Talk Python Feed.')

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week='mon', hour='00', minute='00'
            ), # Midnaiht on Monday, before start of the next work week
            id='Delete Old Job Executions',
            max_instances=1,
            replace_existing=True,
        )
        logger.info('Added weekly job: Delete Old Job Executions.')

        try:
            logger.info('Starting scheduler...')
            scheduler.start()
        except KeyboardInterrupt:
            logger.info('Stopping scheduler...')
            scheduler.shutdown()
            logger.info('Scheduler shut down succesfully!')

