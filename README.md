moinmoin-memodump
=================

A simple MoinMoin theme based on Twitter Bootstrap.  
Comes with responsive navbar and sidebar.

You can create your own sidebar by creating a page called 'SideBar'.

Tested with MoinMoin 1.9.7 on Python 2.7.5.


Preview
-------

Will add some screen shots later.


Install
-------

1. Get the files by cloning the repository or download a zip and unpack it.  
   To clone the repository, run the command below. (Files will be stored under your current directory.)

        git clone https://github.com/dossist/moinmoin-memodump.git

2. Copy memodump.py into wiki/data/plugin/theme/ .  
   Assuming that cloned repository is stored in memodump-xxx (where xxx holds version number):

        cd memodump-xxx
        cp memodump.py YourMoinDirectory/wiki/data/plugin/theme/
    
3. Copy whole directory 'memodump-xxx/memodump' into MoinMoin/web/static/htdocs/

        cp -a memodump YourMoinDirectory/MoinMoin/web/static/htdocs/
    
4. Copy image files for default 'modernized' theme into memodump directory.

        cd YourMoinDirectory/MoinMoin/web/static/htdocs
        cp -a modernized/img memodump/

5. Done!
   If you run MoinMoin in a server, you might have to terminate running MoinMoin processes to reflect changes.  
   For example, on Ubuntu, run the following command on the shell to terminate MoinMoin processes.
   
        pkill moin


How to use
----------

There are two ways to apply the theme.

### As your personal theme, keeping default theme unchanged ###

* Log into your wiki and go to user preferences page.
  ('Settings' near the upper left corner, then 'Preferences')
* Choose 'memodump' from Preferred theme dropdown box.
* Hit 'save' button at the bottom of the page.

### As the default theme ###

Edit wikiconfig.py to change theme_default.
wikiconfig.py will be found in YourMoinDirectory/wiki/config/ .

        theme_default = 'memodump'

Please note that indentations are important in python codes, and here you must
indent the line by exactly 4 spaces.


Customization
-------------

### SideBar ###

Create a page named 'SideBar' to create your own site-wide sidebar.
In sidebar, list items receive menu-like styles.  
Example:
```
{{attachment:prettylogo.jpg}}
 * [[FrontPage]]
 * [[Project1]]
   * [[Project1/Topic1]]
   * [[Project1/Topic2]]
 * [[Project2]]

==== Utility ====
 * [[SideBar?action=edit | Edit Sidebar]]
```

### Location area ###

On top of page contents, we have an area which shows where in the wiki you are now, and when it was updated last time.  
However, showing the info on every page feels a bit redundant.
You can define a list of pages which comes without the info.
Define a list named 'memodump_hidelocation' in wikiconfig.py. The list has page names as its entries.  
Example:

        memodump_hidelocation = [page_front_page, u'SideBar', ]

By default, page_front_page is the only page in the list.

### Menu items ###

Basic knowledge of python language is required!

By defining a variable named 'memodump_menuoverride' in wikiconfig.py, you can override menu entries.  
Example:

        memodump_menuoverride = [
            'raw',
            'print',
        ]

For details, please refer to menu() method in memodump.py.


Tips
----

### Trails and quick links ###

They are moved into sidebar area, and will be displayed below the site-wide SideBar if user has something to be shown.

### Logo ###

If you use the default image logo, it's most likely that your logo will run off the navbar height.
By disabling the logo, MoinMoin will use your site name as a text logo with a link to the FrontPage.
Just comment out logo_string in wikiconfig.py:

        logo_string = ...

↓

    #   logo_string = ...

### I don't like backlinks! ###

If you get the latest code of MoinMoin (as of June 2014) [from the repository](https://bitbucket.org/thomaswaldmann/moin-1.9), you can disable backlinking behavior in location area by adding a line to wikiconfig.py:

        backlink_method = lambda self, req: 'pagelink'

This is not specific for this theme, but viable for other themes as well.
Please note that this is not implemented in 1.9.7. Will work only with the latest code pulled directly from the repository.


Limitations
-----------

* Some words in the theme are not translated.
* navibar, editbar, actionsMenu are replaced with the theme's own functionality, and settings
  on those replaced functions will not affect new ones.
* SlideShow mode is not ready.
* Sidebar area is reserved even if 'SideBar' page does not exist nor is accessible.
* Original actionsMenu were listing additional actions automatically, but the menu of this theme
  won't do so automatically.


License
-------

Copyright 2014 dossist.  
This theme is licensed under [GNU GPL](http://www.gnu.org/licenses/gpl).  
[Twitter Bootstrap](http://getbootstrap.com/) is copyrighted by Twitter, Inc and licensed under [the MIT license](https://github.com/twbs/bootstrap/blob/master/LICENSE).  
[MoinMoin](https://moinmo.in/) is copyrighted by [The MoinMoin development team](https://moinmo.in/MoinCoreTeamGroup).
