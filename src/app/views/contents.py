""" Contains views for the table of contents """
from base_view import BaseView
from app.domain import dbwrap

class ContentsView(BaseView):
    """
    Serves table of contents.
    """
    def get(self):
        post_list = dbwrap.post_list
        tags = sorted(dbwrap.tags)
        categories = sorted(dbwrap.categories)
        self.render("contents.html", heading="All Posts", blog_posts=post_list,
                    tags=tags, categories=categories)


class TagView(BaseView):
    """
    Serves posts associated with a tag.
    """
    def get(self, tag):
        if not tag:
            self.redirect('/')

        tags = sorted(dbwrap.tags)
        categories = sorted(dbwrap.categories)
        tag = tag.lower()
        posts = dbwrap.post_list
        related_posts = filter(lambda p: tag in p.tags, posts)
        if len(related_posts) == 0:
            self.redirect('/')
        self.render("contents.html", heading=tag, blog_posts=related_posts,
                    tags=tags, categories=categories)


class CategoryView(BaseView):
    """
    Serves posts associated with a category.
    """
    def get(self, category):
        if not category:
            self.redirect('/')

        tags = sorted(dbwrap.tags)
        categories = sorted(dbwrap.categories)
        category = category.lower()
        posts = dbwrap.post_list
        related_posts = filter(lambda c: category in c.categories, posts)
        if len(related_posts) == 0:
            self.redirect('/')
        self.render("contents.html", heading=category, blog_posts=related_posts,
                    tags=tags, categories=categories)
