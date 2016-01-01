#  README.rst
# 
#  Created by:    Michael Dacre
#  Date Created:  2016-01-01 10:10
#  Last modified: 2016-01-01 10:19 
#

############################
m4a to mp3 podcast converter
############################

*Under active deveopment, do not use*


Plan:

- Integrate with Dropbox
- Parse rss feeds
- Download m4a podcasts from rss feed
- Convert m4a to mp3, maintaining tags
- Upload mp3 files to dropbox
- Create new rss with mp3 urls instead of m4a urls, otherwise identical to original
- Upload rss to dropbox or ftp server, allowing import into podcast app


The plan is that this script can be run by crontab or systemd on the user's computer.
