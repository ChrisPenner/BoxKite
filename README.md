BoxKite Blog Framework
======================
A very simple blog framework that emphasizes managing posts in a plain-text
directory structure. Runs on Google App Engine, but can also be exported as a
static site.

Installation
------------
Simply clone this repo into the place you'd like to work on it:
```
git clone https://github.com/ChrisPenner/BoxKite.git
```

Next, take a look at ```boxkite/content/posts/helloworld.md``` to get an idea
of how to structure your posts.

In order to test and upload your blog you'll need to install Google App
Engine (the **python** version) on your machine. You can download it and find
instructions [HERE](https://cloud.google.com/appengine/downloads). If it asks
you if you'd like to make symlinks, say yes, it's important for later.

After App Engine is installed, you need to add your BoxKite blog as a project.
Run the GoogleAppEngineLauncher program and choose File>Add Existing
Application, then browse to the directory you cloned earlier. I recommend
setting:
```Admin Port: 8081
Port: 8080 ```
Now you can select the project and choose the "Run" option from the main menu.
At this point you can choose the 'browse' option, or navigate to
```http://localhost:8080/``` in your browser to see your blog.

Getting it Online
-----------------
If you've followed the installation instructions without problems, then you can
now upload your site to the web! If you'd like to use Google App Engine to
manage your site, you need to register a new application at
https://appengine.google.com/. Remember the name you use for your app here, and
enter it as your application name in ```app.yaml```. You'll also want to set
```appname.appspot.com``` as your site_root in ```config.py``` unless you've
got a custom domain. If you want to set up a custom domain, follow Google's
instructions here: https://cloud.google.com/appengine/docs/domain

If instead you'd prefer to upload your blog as a static set of files, see
**Rendering to Static Site**.

Rendering to static site
------------------------
If you don't want to use Google App Engine to serve your site to the web, it is
possible to export your blog as a set of static files which can be served from
any basic web-server (or can be sent as a set of files to your friends). This
is done in BoxKite by simply running the App Engine webserver locally on your
machine, then downloading the whole site from the server using wget. Needless
to say you'll need wget for this to work, Windows users can try cygwin, though
I haven't tested it.

To do this, open a terminal (or cygwin) and navigate to your app's directory.
Then simply run ```./staticize.sh```

Your terminal will buzz away for a few moments (this can take a few minutes as
your site gets larger) and your static site will appear in a ```/static-site```
directory, probably labeled ```localhost:8080```. This folder can be uploaded
to your hosting provider of choice.

Post Format
------------
```
title: My Title
author: My Author
date: August 2nd 2014
tags: awesome, words, here,

^ Leave one blank line between metatags and content
<markdown formatted content goes here>
```

Organization
------------
The organizational structure of the framework is pretty easy to understand,
posts in ```content/posts``` will be processed and posted, ordered by
their date tag. Posts in ```content/drafts``` are ignored, feel free to
store unfinished work there. Images are placed in ```content/images```
and are accessed as ``` <img src="/images/mypic.png"> ``` **Note** that's
```/images```, not ```/content/images```. If you follow this structure,
everything should pretty much just work.

Anything stored under the ```content/other``` folder will be uploaded and will
be available online. For example ```content/other/page.html``` is available at
```www.yoursite.com/other/page.html```. See **Customization** to learn how to
add your own site routes.

Customization
-------------
BoxKite is just a starting place, customizing it is actually a great way to
learn a bit about web-development. It provides a foundation, but everything you
build on top will be done using basic web technologies like js, css, and html.

Unlike other systems (e.g. Wordpress) you controll everything with basic html
and css and it's easy to change anything you like. Feel free to edit the css,
edit the html templates, etc.

To get started though, there's a couple easy options you can change. These are
stored in ```config.py```, here are the options with their default values:

```
# These properties are used primarily for the RSS feed and social media
# metadata.
# The domain name the site will served from
site_root = "http://yourtopleveldomainhere.com"
site_title = "Box-Kite Blog"
site_description = "I made a box-kite once"
site_category = "Your site's category here."
author = "Your Name"

# The beacon is the short logo on the top left of the screen that links to the
# table of contents.
beacon = 'BK'

# Choose whether to use categories and tags
show_categories = False
show_tags = True

# Show or hide social media buttons
facebook_share_buttons = False
twitter_share_buttons = False

# Twitter metadata allows fancy pictures/descriptions to show when your blog is
# linked on twitter.
include_twitter_metadata = True
twitter_handle = "twitterhandle"

# BoxKite uses Disqus for comment integration, you'll have to sign up there and
# enter your shortname here.
use_disqus_comments = False
disqus_shortname = "disqus-shortname"
```

### Other forms of customization:
### CSS
ALL of the css for BoxKite is stored in ```css/style.scss```. It's written in
[Sassy-CSS](http://sass-lang.com/), so if you make any changes there you'll
need to recompile the .css file. If you prefer to work with basic css, simply
change the style.css file and ignore the .scss file. You'll note that at the
top of the style.scss there are several $variables, you can change these
variables to alter the colours used in the site, note that this will have mixed
results and may take some experimentation to get it working right, but feel
free to make any changes you like.

### HTML
BoxKite uses the wonderful [Jinja2](http://jinja.pocoo.org/docs/dev/) html
templating language which allows html pages to accept variables and use
inheritance. Every page on the site inherits from base.html, so any changes
made there will affect every page. The post-page.html, contents.html, and
rss.xml correspond to the post-viewing page, table-of-contents and rss feed
respectively.

### Javascript
If you need any sort of scripting/behaviour on your site you can go ahead and
put any scripts you want into the js/ directory and reference it with
```<script src="/js/yourscript.js"></script>```.

### Site Routing / Handlers
If you need to define custom site routes or modify back-end behaviour
you can do so in app.yaml or master.py. For static resources simply
add a rule into app.yaml following the format of the /other route. For
dynamic handlers you'll need to read some documentation about [Google App
Engine](https://cloud.google.com/appengine/docs/python/).

Performance
-----------
A note regarding performance. This is a simple framework that does NOT use a
database to store ANYTHING. It generates post data upon deployment and holds
every post in the memory of the web-server, while this makes it very fast and
easy to use for small projects, this also makes it very unsuitable for huge
blogs with hundreds and hundreds of posts. I haven't tested this with anything
on a large magnitude, but it should work just fine for any form of hobby
writing. If you do end up running into issues, try exporting your site
statically on your local machine and simply uploading the resultant files.
