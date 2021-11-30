from django.test import TestCase
from .models import Episode


class PodcastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title='My Awesome Podcast Episode',
            description='Look, I made it!',
            publication_date='2018-11-20T15:58:44.767594-06:00',
            link='https://mypodcastsexampleapp.com',
            image='https://image.mypodcastsexampleapp.com',
            podcast_name='My Python Podcast',
            unique_attribute='de194720-7b4c-49e2-a05f-432436d3fetr',
        )

    def test_episode_content(self):
        self.assertEqual(
            self.episode.title,
            'My Awesome Podcast Episode'
        )
        self.assertEqual(
            self.episode.description,
            'Look, I made it!'
        )
        self.assertEqual(
            self.episode.publication_date,
            '2018-11-20T15:58:44.767594-06:00'
        )
        self.assertEqual(
            self.episode.link,
            'https://mypodcastsexampleapp.com'
        )
        self.assertEqual(
            self.episode.image,
            'https://image.mypodcastsexampleapp.com'
        )
        self.assertEqual(
            self.episode.podcast_name,
            'My Python Podcast'
        )
        self.assertEqual(
            self.episode.unique_attribute,
            'de194720-7b4c-49e2-a05f-432436d3fetr'
        )

    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode),
            'My Python Podcast: My Awesome Podcast Episode'
        )

