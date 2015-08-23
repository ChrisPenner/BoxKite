"""
Contains routes.
"""
import webapp2
import domain.posts
from views.base_view import BaseView
from views import contents, posts, rss

class FourOhFourView(BaseView):
    """
    Redirects all other URLs to contents page.
    """
    def get(self):
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', contents.ContentsView),
    ('/post/([^/]+)', posts.PostView),
    ('/tag/([^/]+)', contents.TagView),
    ('/category/([^/]+)', contents.CategoryView),
    ('/feed', rss.RSSView),
    ('.*', FourOhFourView),
], debug=False)
