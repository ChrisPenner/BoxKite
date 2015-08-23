"""
Contains global values and settings.
"""

# ==============================
#           Site Info
# ==============================
# This info is used in metadata throughout the site and in the RSS feed.
site_root = "http://yourtopleveldomainhere.com"
site_title = "Box-Kite Blog"
site_description = "I made a box-kite once"
site_category = "Your site's category here."
author = "Your Name"

# The beacon appears in the top left corner of the site and links to
# the main page. You can use a few letters or a small image eg.
# '<img src="/images/logo.png" alt="Site-logo">' is valid (though may look
# a little strange).

beacon = 'BK'

# ==============================
#         Site Options
# ==============================

# Choose whether to use categories and tags
show_categories = True
show_tags = True

# Import gists from github account as posts? (set username below)
import_gists = True
github_username = "ChrisPenner"

# BoxKite will only import a gist if it has one of these strings in the gist
# description. Leave the list empty to use ALL gists.
gist_filter_strings = []

# ==============================
#          Social Media
# ==============================
facebook_share_buttons = False
twitter_share_buttons = False

# This allows tweets about your posts to show pictures and a description. Must
# fill in twitter_handle to use this.
include_twitter_metadata = True
twitter_handle = "twitterhandle"  # No @ symbol

use_disqus_comments = False
disqus_shortname = "disqus-shortname"
