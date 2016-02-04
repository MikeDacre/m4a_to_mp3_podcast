"""
A class to hold an existing podcast, to allow comparison.

       Created: 2016-11-04 14:02
 Last modified: 2016-02-04 14:27

Uses pickle.
"""
import os
try:
    import cPickle as pickle
except ImportError:
    import pickle
import feedparser


class Podcast(object):

    """Preserve a podcast."""

    def __init__(self, url, file):
        """Initialize a feedparser object and save to file.

        :url:  The URL of the podcast.
        :file: File to save to.

        """
        self.url  = url
        self.file = file
        if os.path.isfile(file):
            self = self.load(file)
            return
        self.feed = feedparser.parse(self.url)
        self.episodes = []
        for episode in self.feed['entries']:
            self.episodes.append(Episode[episode])

    def load(self, file):
        """Overwrite self with the contentes of file."""
        with open(file, 'rb') as fin:
            self = pickle.load(file)

    def save(self):
        """Save self with pickle."""
        with open(self.file, 'wb') as fout:
            pickle.dump(self, fout)


class Episode(object):

    """A podcast episode from a feed."""

    def __init__(self, episode):
        """Set up self from feedparser entry.

        :episode: A feedparser['entries'] list item.

        """
        self.entry = episode
        self.title = episode['title']
        self.audio = []
        for link in episode['links']:
            if link['type'].startswith('audio'):
                self.audio.append(link)


def compare_podcasts(podcast1, podcast2):
    """Compare two podcasts, return

    :returns: Different entries.

    """
    pass
