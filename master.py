"""
Contains route handlers.
"""
import webapp2
import dbwrap
import posts
from handler import Handler


class Contents(Handler):
    """
    Serves table of contents.
    """
    def get(self):
        post_list = dbwrap.post_list
        tags = sorted(dbwrap.tags)
        categories = sorted(dbwrap.categories)
        self.render("contents.html", heading="All Posts", blog_posts=post_list,
                    tags=tags, categories=categories)


class PostHandler(Handler):
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


class TagHandler(Handler):
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


class CategoryHandler(Handler):
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


class RSS(Handler):
    """
    Serves RSS feed page.
    """
    def get(self):
        self.response.headers['Content-Type'] = "application/rss+xml"
        self.render('rss.xml', posts=dbwrap.post_list)


class FourOhFour(Handler):
    """
    Redirects all other URLs to contents page.
    """
    def get(self):
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', Contents),
    ('/post/([^/]+)', PostHandler),
    ('/tag/([^/]+)', TagHandler),
    ('/category/([^/]+)', CategoryHandler),
    ('/feed', RSS),
    ('.*', FourOhFour),
], debug=False)
