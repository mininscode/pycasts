from django.test import TestCase
from django.urls.base import reverse

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

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')

    def test_home_page_list_contents(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'My Awesome Podcast Episode')

