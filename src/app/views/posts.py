""" Contains handlers for post related pages. """
from base_view import BaseView
from app.domain import posts


class PostView(BaseView):
    """
    Serves a specific post by post-name.
    """
    def get(self, post_name):
        if not post_name:
            self.redirect('/')

        post_name = post_name.lower()
        post_dict = dbwrap.post_dict
        if post_name in post_dict:
            post = dbwrap.get_post(post_name)
            prev_post, next_post = posts.get_adj_posts(post_name)
            self.render("post-page.html",
                        post=post,
                        prev_post=prev_post,
                        next_post=next_post,
                        url=self.request.url,
                        )
        else:
            self.redirect('/')
