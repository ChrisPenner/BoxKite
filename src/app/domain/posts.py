"""
Parses and loads posts from files into storage.
"""
import markdown2
import json
import os
import re
import urllib2

from app.domain import dbwrap
from app.models.post import Post
import config


def init():
    """
    Scans and converts all post documents into post objects.
    Also pulls in Gists from Github.
    """
    posts = parse_posts()
    if config.import_gists:
        posts = posts + parse_gists()

    for post in posts:
        add_post(post)


def obj_from_url(url):
    try:
        file = urllib2.urlopen(url)
        object = json.load(file)
        return object
    except:
        return []


def convert_from_markdown(string):
    md = markdown2.Markdown()
    return md.convert(string)


def parse_posts():
    """
    Parse all posts in the content/posts directory and return a list of Post
    objects.
    """

    dir_path = 'content/posts'
    file_list = [f for f in os.listdir(dir_path) if not f.startswith('.')]
    posts = []
    for file_name in file_list:
        file_path = os.path.join(dir_path, file_name)
        with open(file_path) as f:
            # read title, author, and date from file before converting markdown.
            line = ''
            post_info = {}
            while not line.startswith('\n'):
                line = f.readline()
                # Check if it's a parameter line
                m = re.match(r'^(?P<key>\w+): (?P<value>.+)', line)
                if m:
                    gd = m.groupdict()
                    key = gd['key'].lower()
                    value = gd['value'].strip()
                    if key == 'tags' or key == 'categories':
                        value = value.split(' ')
                        value = map(str.strip, value)
                        value = map(str.lower, value)
                        value = filter(lambda x: '' != x, value)
                    post_info[key] = value

            s = f.read()
            content = convert_from_markdown(s)
            # split file name on . take the file name, lowercase
            post_info['name'] = file_name.rpartition('.')[0].lower()
            post_info['content'] = content

            # add all retrieved content to post
            post = Post(post_info)
            posts.append(post)
    return posts


def parse_gists():
    """
    Parse all posts in the content/posts directory and return a list of Post
    objects.
    """
    username = config.github_username
    filters = config.gist_filter_strings
    try:
        gists = obj_from_url("https://api.github.com/users/%s/gists" % username)
    except:
        return []
    if filters:
        valid_gists = \
            [g for g in gists if any([f in g['description'] for f in filters])]
    else:
        valid_gists = gists
    valid_gists = [obj_from_url(g['url']) for g in valid_gists]

    posts = []
    for gist in valid_gists:
        post_info = {}
        post_info['author'] = config.author
        post_info['name'] = gist['files'].items()[0][0].split('.')[0]
        post_info['title'] = \
            re.sub(r'\s?\[.+?\]|\{.+?\}', '', gist['description'])
        post_info['date'] = gist['created_at']
        tags = re.findall('\[(.+?)\]', gist['description'])
        post_info['tags'] = [t.strip().lower() for t in tags if t != '']
        categories = re.findall('\{(.+?)\{', gist['description'])
        post_info['categories'] = \
            [c.strip().lower() for c in categories if t != '']
        total_content = \
            [convert_from_markdown(file[1]['content'])
             for file in gist['files'].items()]
        post_info['content'] = '\n'.join(total_content)
        posts.append(Post(post_info))
    return posts


def add_post(post):
    """
    Adds a post to storage.
    """
    dbwrap.put(post.name, post)


def get_adj_posts(post_name):
    """
    Returns a tuple of (previous post, next post)
    """
    post_names = [p.name for p in dbwrap.post_list]
    if post_name in post_names:
        index = post_names.index(post_name)
        if index + 1 < len(post_names):
            next_post = post_names[index + 1]
        else:
            next_post = None

        if index - 1 >= 0:
            prev_post = post_names[index - 1]
        else:
            prev_post = None
        return (prev_post, next_post)
    else:
        return (None, None)


# Call init when booting up application.
init()
