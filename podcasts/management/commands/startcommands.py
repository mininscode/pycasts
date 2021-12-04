import ssl
import feedparser
from dateutil import parser
from django.core.management.base import BaseCommand

from podcasts.models import Episode



def save_new_episodes(feed):
        podcast_title = feed.channel.title
        podcast_image = feed.channel.image['href']

        for item in feed.entries:
            if not Episode.objects.filter(guid=item.guid).exists():
                episode = Episode(
                    title=item.title,
                    description=item.description,
                    pub_date=parser.parse(item.published),
                    link=item.link,
                    image=podcast_image,
                    podcast_name=podcast_title,
                    guid=item.guid,
                )
                episode.save()


def add_realpython_episodes():
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        _feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
        save_new_episodes(_feed)


def add_talkpython_episodes():
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        _feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
        save_new_episodes(_feed)


class Command(BaseCommand):
    def handle(self, *args, **options):
        add_realpython_episodes()
        add_talkpython_episodes()

