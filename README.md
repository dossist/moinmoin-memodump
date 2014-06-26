moinmoin-memodump
=================

A simple [MoinMoin][] theme based on [Twitter Bootstrap][].  
Comes with responsive navbar and sidebar.

You can create your own sidebar by creating a page called 'SideBar'.

Tested with MoinMoin 1.9.7 on Python 2.7.5.

For details, please refer to [the project wiki][Wiki Home].


Screenshots
-----------

Normal view
![Main](https://github.com/dossist/moinmoin-memodump/wiki/memodump.png)

Automatically collapsed navbar and sidebar under narrow viewport
![Collapsed](https://github.com/dossist/moinmoin-memodump/wiki/memodump%20collapsed.png)


Install
-------

1. Get the files by cloning the repository or download a zip and unpack it.  
   To clone:

        git clone https://github.com/dossist/moinmoin-memodump.git

2. Copy memodump.py into `wiki/data/plugin/theme/`.

        cd moinmoin-memodump
        cp memodump.py YourMoinDirectory/wiki/data/plugin/theme/
    
3. Copy whole directory `memodump` into `MoinMoin/web/static/htdocs/`.

        cp -a memodump YourMoinDirectory/MoinMoin/web/static/htdocs/
    
4. Copy image files for default *modernized* theme into memodump directory.

        cd YourMoinDirectory/MoinMoin/web/static/htdocs
        cp -a modernized/img memodump/

5. Done!
   If you run MoinMoin in a server, you might have to terminate running MoinMoin processes to reflect changes.  
   e.g. On Ubuntu:
   
        pkill moin


How to use
----------

There are two ways to apply the theme.

### As your personal theme, keeping default theme unchanged ###

* Log into your wiki and go to user preferences page.
  (**Settings** near the upper left corner, then **Preferences**)
* Choose **memodump** from Preferred theme dropdown box.
* Hit *save* button at the bottom of the page.

### As the default theme ###

Edit `wikiconfig.py` to change `theme_default`.
(`wikiconfig.py` will be found in `YourMoinDirectory/wiki/config/`.)

        theme_default = 'memodump'

Please note that indentations are important in python codes, and here you must
indent the line by exactly 4 spaces.


Customization
-------------
For details, please refer to [the project wiki][Wiki Home].


### SideBar ###

Create a page named `SideBar` to create your own site-wide sidebar.
In sidebar, list items receive special menu-like styles.  


### Location area ###

On top of page contents, we have an area which shows where in the wiki you are now, and when it was updated last time.  
However, showing the info on every page feels a bit redundant.
You can define a list of pages which comes without the info.  
Define a list `memodump_hidelocation` in `wikiconfig.py`. The list has page names as its entries.  
Example:

        memodump_hidelocation = [page_front_page, u'SideBar', ]

By default, `page_front_page` is the only page in the list.


### Menu items ###

Basic knowledge of python language is required!

By defining `memodump_menuoverride` in `wikiconfig.py`, you can override menu entries.  
Example:

        memodump_menuoverride = [
            'raw',
            'print',
        ]

For details, please refer to [the project wiki][Wiki EditMenu].


Limitations
-----------

* Some words in the theme are not translated. (Can be translated via [WikiDictionary][Wiki Translation] pages, though)
* editbar and actionsMenu are replaced with the theme's own menu functionality, and settings
  on the replaced will not affect the new menu.
* SlideShow mode is not ready.
* Sidebar area is reserved even if `SideBar` page does not exist nor is accessible.
* Original actionsMenu were listing additional actions automatically, but the menu of this theme
  won't do so automatically.


License
-------

Copyright 2014 dossist.  
This theme is licensed under [GNU GPL][].  
[Twitter Bootstrap][] is copyrighted by Twitter, Inc and licensed under [the MIT license][MIT].  
[MoinMoin][] is copyrighted by [The MoinMoin development team](https://moinmo.in/MoinCoreTeamGroup).



[MoinMoin]: https://moinmo.in/
[Twitter Bootstrap]: http://getbootstrap.com/
[Wiki Home]: https://github.com/dossist/moinmoin-memodump/wiki
[Wiki EditMenu]: https://github.com/dossist/moinmoin-memodump/wiki/EditMenu
[Wiki Translation]: https://github.com/dossist/moinmoin-memodump/wiki/Translation
[GNU GPL]: http://www.gnu.org/licenses/gpl
[MIT]: https://github.com/twbs/bootstrap/blob/master/LICENSE
