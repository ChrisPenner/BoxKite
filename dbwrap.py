"""
Handles all data management.
"""

post_dict = {}
post_list = []
tags = set()
categories = set()


def put(name, post):
    """
    Adds new post to database and sorted list.
    """
    global post_dict, post_list, tags, categories
    post_dict[name] = post
    post_list.append(post)
    tags = tags.union(post.tags)
    categories = categories.union(post.categories)
    sort_post_list()


def get_post(name):
    """
    Returns a post from the post dictionary by name.
    """
    return post_dict.get(name)


def sort_post_list():
    """
    Sorts post_list by date.
    """
    def get_time_tuple(post):
        return post.sort_date
    post_list.sort(key=get_time_tuple, reverse=True)
