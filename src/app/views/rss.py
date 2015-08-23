""" Contains views for the RSS feed. """

from base_view import BaseView

class RSSView(BaseView):
    """
    Serves RSS feed page.
    """
    def get(self):
        self.response.headers['Content-Type'] = "application/rss+xml"
        self.render('rss.xml', posts=dbwrap.post_list)


