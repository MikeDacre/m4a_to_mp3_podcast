#  README.rst
# 
#  Created by:    Michael Dacre
#  Date Created:  2016-01-01 10:10
#  Last modified: 2016-01-01 10:19 
#

############################
m4a to mp3 podcast converter
############################

**Under active deveopment, do not use**


Plan:

- Integrate with Dropbox
- Parse rss feeds
- Download m4a podcasts from rss feed
- Convert m4a to mp3, maintaining tags
- Upload mp3 files to dropbox
- Create new rss with mp3 urls instead of m4a urls, otherwise identical to original
- Upload rss to dropbox or ftp server, allowing import into podcast app


The plan is that this script can be run by crontab or systemd on the user's computer.

************
Installation
************

First, install the package::

  setup.py install

If you do not use root, the scripts will be in ``~/.local/bin/``, you may want to put that in your path.

To get it to run on a schedule, you can use a crontab, or any other method of your choosing. To set a crontab, run ``crontab -e`` at the command line, and add a line like this::

  0 */6 * * * /usr/bin/convert_m4a_podcast_to_mp3.py >/dev/null 2>&1

This line will run the scrupt every 6 hours if your computer is on. Depending on how often your computer is on, and how ofter you expect your podcast to update, you may want to change this. A tool like http://crontab-generator.org/ makes this easy.

Operating systems have multiple methods of automation, there may be a better way to do this depending on your use case.

**Under active deveopment, do not use**
