""" The Schema for a post object """
from app.domain.utils import parse_date
import config


class Post(object):
    """
    Holds all information regarding an individual blog post.
    """

    def __init__(self, metadata):
        parsed_dates = parse_date(metadata.get('date', ''))
        metadata['date'] = parsed_dates[0]
        metadata['sort_date'] = parsed_dates[1]
        metadata['pub_date'] = parsed_dates[2]
        link = config.site_root + "/post/" + metadata.get('name', '')
        metadata['link'] = link
        metadata['tags'] = metadata.get('tags', set())
        metadata['categories'] = metadata.get('categories', set())
        for key, value in metadata.iteritems():
            setattr(self, key, value)
