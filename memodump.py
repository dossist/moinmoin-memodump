# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - memodump theme

    Based on modernized theme in MoinMoin

    config variables:
        following variables in wikiconfig.py will change something in the theme.

        memodump_menuoverride
            overrides menu elements. see self.menu() for details.

        memodump_hidelocation
            overrides list of page names that have no location area.
            e.g. [page_front_page, u'SideBar', ]

    @copyright: 2014 dossist.
    @license: GNU GPL, see http://www.gnu.org/licenses/gpl for details.
"""

from MoinMoin.theme import ThemeBase
import StringIO, re
from MoinMoin import wikiutil
from MoinMoin.action import get_available_actions
from MoinMoin.Page import Page

class Theme(ThemeBase):

    name = "memodump"

    _ = lambda x: x     # We don't have gettext at this moment, so we fake it
    icons = {
        # key         alt                        icon filename      w   h
        # FileAttach
        'attach':     ("%(attach_count)s",       "moin-attach.png",   16, 16),
        'info':       ("[INFO]",                 "moin-info.png",     16, 16),
        'attachimg':  (_("[ATTACH]"),            "attach.png",        32, 32),
        # RecentChanges
        'rss':        (_("[RSS]"),               "moin-rss.png",      16, 16),
        'deleted':    (_("[DELETED]"),           "moin-deleted.png",  16, 16),
        'updated':    (_("[UPDATED]"),           "moin-updated.png",  16, 16),
        'renamed':    (_("[RENAMED]"),           "moin-renamed.png",  16, 16),
        'conflict':   (_("[CONFLICT]"),          "moin-conflict.png", 16, 16),
        'new':        (_("[NEW]"),               "moin-new.png",      16, 16),
        'diffrc':     (_("[DIFF]"),              "moin-diff.png",     16, 16),
        # General
        'bottom':     (_("[BOTTOM]"),            "moin-bottom.png",   16, 16),
        'top':        (_("[TOP]"),               "moin-top.png",      16, 16),
        'www':        ("[WWW]",                  "moin-www.png",      16, 16),
        'mailto':     ("[MAILTO]",               "moin-email.png",    16, 16),
        'news':       ("[NEWS]",                 "moin-news.png",     16, 16),
        'telnet':     ("[TELNET]",               "moin-telnet.png",   16, 16),
        'ftp':        ("[FTP]",                  "moin-ftp.png",      16, 16),
        'file':       ("[FILE]",                 "moin-ftp.png",      16, 16),
        # search forms
        'searchbutton': ("[?]",                  "moin-search.png",   16, 16),
        'interwiki':  ("[%(wikitag)s]",          "moin-inter.png",    16, 16),

        # smileys (this is CONTENT, but good looking smileys depend on looking
        # adapted to the theme background color and theme style in general)
        #vvv    ==      vvv  this must be the same for GUI editor converter
        'X-(':        ("X-(",                    'angry.png',         16, 16),
        ':D':         (":D",                     'biggrin.png',       16, 16),
        '<:(':        ("<:(",                    'frown.png',         16, 16),
        ':o':         (":o",                     'redface.png',       16, 16),
        ':(':         (":(",                     'sad.png',           16, 16),
        ':)':         (":)",                     'smile.png',         16, 16),
        'B)':         ("B)",                     'smile2.png',        16, 16),
        ':))':        (":))",                    'smile3.png',        16, 16),
        ';)':         (";)",                     'smile4.png',        16, 16),
        '/!\\':       ("/!\\",                   'alert.png',         16, 16),
        '<!>':        ("<!>",                    'attention.png',     16, 16),
        '(!)':        ("(!)",                    'idea.png',          16, 16),
        ':-?':        (":-?",                    'tongue.png',        16, 16),
        ':\\':        (":\\",                    'ohwell.png',        16, 16),
        '>:>':        (">:>",                    'devil.png',         16, 16),
        '|)':         ("|)",                     'tired.png',         16, 16),
        ':-(':        (":-(",                    'sad.png',           16, 16),
        ':-)':        (":-)",                    'smile.png',         16, 16),
        'B-)':        ("B-)",                    'smile2.png',        16, 16),
        ':-))':       (":-))",                   'smile3.png',        16, 16),
        ';-)':        (";-)",                    'smile4.png',        16, 16),
        '|-)':        ("|-)",                    'tired.png',         16, 16),
        '(./)':       ("(./)",                   'checkmark.png',     16, 16),
        '{OK}':       ("{OK}",                   'thumbs-up.png',     16, 16),
        '{X}':        ("{X}",                    'icon-error.png',    16, 16),
        '{i}':        ("{i}",                    'icon-info.png',     16, 16),
        '{1}':        ("{1}",                    'prio1.png',         15, 13),
        '{2}':        ("{2}",                    'prio2.png',         15, 13),
        '{3}':        ("{3}",                    'prio3.png',         15, 13),
        '{*}':        ("{*}",                    'star_on.png',       16, 16),
        '{o}':        ("{o}",                    'star_off.png',      16, 16),
    }
    del _

    stylesheets = (
        # media         basename
        ('all',         'bootstrap.min'),
        ('all',         'bootstrap-theme.min'),
        ('all',         'memodump'),
        ('all',         'moinizer'),
        )
    stylesheets_print = (
        ('all',         'bootstrap.min'),
        ('all',         'bootstrap-theme.min'),
        ('all',         'memodump'),
        ('all',         'moinizer'),
        ('all',         'memoprint'),
        )

    def header(self, d, **kw):
        """ Assemble wiki header
        header1: supported.
        header2: supported.

        @param d: parameter dictionary
        @rtype: unicode
        @return: page header html
        """

        html = u"""
  <div id="outbox">
    <!-- Bootstrap navbar -->
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="row">

          <!-- Navbar header -->
          <div class="col-md-2">
            <div class="navbar-header">
              <!-- Button to show navbar controls when collapsed -->
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <!-- Sitename -->
              %(sitename)s
            </div> <!-- /.navbar-header -->
          </div> <!-- /.col-* -->

          <!-- Body of navbar -->
          <div class="collapse navbar-collapse">

            <!-- Global menu and user menu -->
            <ul class="nav navbar-nav navbar-right">
              <!-- Menu -->
%(menu)s
              <!-- Login user -->
%(usermenu)s
            </ul>

            <!-- Search form -->
%(search)s

            <!-- Edit button -->
%(edit)s

            <!-- Comment toggle button -->
%(commentbutton)s

          </div> <!-- /.collapse -->
        </div> <!-- /.row -->
      </div> <!-- /.container -->
    </div> <!-- /.navbar -->
    <!-- End of navbar -->

    <div class="container">
      <button class="btn btn-default btn-xs offcanvas-trigger" data-toggle="offcanvas">
        <span class="glyphicon glyphicon-th-list"></span>
      </button>
%(custom_pre)s
      <div class="row offcanvas" id="pagebox">

        <!-- Sidebar -->
        <div class="col-md-2" id="sidebar" role="navigation">
          <div id="sidebarpage">
<!-- SideBar contents -->
%(sidebar)s
<!-- End of SideBar contents -->
          </div>
%(navilinks)s
%(trail)s
        </div> <!-- /#sidebar -->
        <!-- End of sidebar -->

        <!-- Content body -->
        <div class="col-xs-6 col-md-10" id="contentbox">
%(custom_post)s
%(msg)s
%(location)s

<!-- Page contents -->
""" % { 'sitename': self.logo(),
        'location': self.location(d),
        'menu': self.menu(d),
        'usermenu': self.username(d),
        'search': self.searchform(d),
        'edit': self.editbutton(d),
        'commentbutton': self.commentbutton(),
        'sidebar': self.sidebar(d),
        'trail': self.trail(d),
        #'quicklinks': self.quicklinks(d),
        'navilinks': self.navibar(d),
        'msg': self.msg(d),
        'custom_pre': self.emit_custom_html(self.cfg.page_header1), # custom html just below the navbar, not recommended!
        'custom_post': self.emit_custom_html(self.cfg.page_header2), # custom html just before the contents, not recommended!
      }

        return html

    editorheader = header

    def footer(self, d, **keywords):
        """ Assemble wiki footer
        footer1: supported.
        footer2: supported.

        @param d: parameter dictionary
        @keyword ...:...
        @rtype: unicode
        @return: page footer html
        """
        page = d['page']

        html = u"""
<!-- End of page contents -->

        </div> <!-- /#contentbox -->
        <!-- End of content body -->
      </div> <!-- /#pagebox -->
    </div> <!-- /.container -->

    <!-- pageinfo -->
    <div id="pageinfo-container">
      <div class="container">
        %(pageinfo)s
      </div>
    </div>
    <!-- End of pageinfo -->

%(custom_pre)s

    <!-- Footer -->
    <div id="footer">
      <div class="container-fluid">
        <div class="container text-right text-muted">
          %(credits)s
          %(version)s
%(custom_post)s
        </div> <!-- /.container -->
      </div> <!-- /.container-fluid -->
    </div> <!-- /#footer -->
    <!-- End of footer -->

    <!-- Bootstrap core JavaScript -->
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="%(prefix)s/%(theme)s/js/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="%(prefix)s/%(theme)s/js/bootstrap.min.js"></script>
    <!-- Offcanvas toggler, originally from http://getbootstrap.com/examples/offcanvas/offcanvas.js -->
    <script src="%(prefix)s/%(theme)s/js/offcanvas.js"></script>
    <!-- End of JavaScript -->

  </div> <!-- /#outbox -->
""" % { 'pageinfo': self.pageinfo(page),
        'custom_pre': self.emit_custom_html(self.cfg.page_footer1), # Pre footer custom html (not recommended!)
        'credits': self.credits(d),
        'version': self.showversion(d, **keywords),
        'custom_post': self.emit_custom_html(self.cfg.page_footer2), # In-footer custom html (not recommended!)
        'prefix': self.cfg.url_prefix_static,
        'theme': self.name,
      }

        return html

    def logo(self):
        """ Assemble logo with link to front page
        Using <a> tag only instead of wrapping with div

        The logo may contain an image and or text or any html markup.
        Just note that everything is enclosed in <a> tag.

        @rtype: unicode
        @return: logo html
        """
        html = u''
        if self.cfg.logo_string:
            page = wikiutil.getFrontPage(self.request)
            html = page.link_to_raw(self.request, self.cfg.logo_string, css_class="navbar-brand")
        return html

    def location(self, d):
        """ Assemble location area on top of the page content.
        Certain pages shouldn't have location area as it feels redundant.
        Location area is excluded in FrontPage by default.
        Config variable memodump_hidelocation will override the list of pages to have no location area.
        """
        html = u''
        page = d['page']
        pages_hide = [self.request.cfg.page_front_page,]
        try:
            pages_hide = self.request.cfg.memodump_hidelocation
        except AttributeError:
            pass
        if not page.page_name in pages_hide:
            html = u'''
        <div id="location">
%(interwiki)s
%(pagename)s
          %(lastupdate)s
        </div>
''' % {'interwiki': self.interwiki(d), 'pagename': self.title(d), 'lastupdate': self.lastupdate(d),}
        return html

    def interwiki(self, d):
        """ Assemble the interwiki name display, linking to page_front_page

        @param d: parameter dictionary
        @rtype: string
        @return: interwiki html
        """
        if self.request.cfg.show_interwiki:
            page = wikiutil.getFrontPage(self.request)
            text = self.request.cfg.interwikiname or 'Self'
            link = page.link_to(self.request, text=text, rel='nofollow')
            html = u'<span id="interwiki">%s<span class="sep">:</span></span>' % link
        else:
            html = u''
        return html

    def lastupdate(self, d):
        """ Return html for last update in location area, if conditions are met. """
        _ = self.request.getText
        page = d['page']
        html = u''
        if self.shouldShowPageinfo(page):
            info = page.lastEditInfo()
            if info:
                html = u'<span class="lastupdate">%s %s</span>' % (_('Last updated at'), info['time'])
        return html

    def searchform(self, d):
        """
        assemble HTML code for the search form

        @param d: parameter dictionary
        @rtype: unicode
        @return: search form html
        """
        _ = self.request.getText
        form = self.request.values
        updates = {
            'search_label': _('Search:'),
            'search_hint': _('Search'),
            'search_value': wikiutil.escape(form.get('value', ''), 1),
            'search_full_label': _('Text'),
            'search_title_label': _('Titles'),
            'url': self.request.href(d['page'].page_name)
            }
        d.update(updates)

        html = u'''
            <div class="navbar-form navbar-right">
              <form class="form-search" role="search" id="searchform" method="get" action="%(url)s">
                <input type="hidden" name="action" value="fullsearch">
                <input type="hidden" name="context" value="180">
                <div class="form-group">
                  <label class="sr-only" for="searchinput">%(search_label)s</label>
                  <input id="searchinput" type="text" class="form-control form-search" placeholder="%(search_hint)s" name="value" value="%(search_value)s">
                </div>
              </form>
            </div>
''' % d
        return html

    def editbutton(self, d):
        """ Return an edit button html fragment.

        If the user can't edit, return a disabled edit button.
        """
        page = d['page']

        if 'edit' in self.request.cfg.actions_excluded:
            return u""

        button = u''
        li_attr = u''

        if not (page.isWritable() and
                self.request.user.may.write(page.page_name)):
            button = self.disabledEdit()
            li_attr = u' class="disabled"'
        else:
            _ = self.request.getText
            querystr = {'action': 'edit'}
            text = _('Edit')
            querystr['editor'] = 'text'
            attrs = {'name': 'texteditlink', 'rel': 'nofollow', 'css_class': 'menu-nav-edit'}
            button = page.link_to_raw(self.request, text=text, querystr=querystr, **attrs)

        html = u'''
            <ul class="nav navbar-nav navbar-right">
              <li%s>
                %s
              </li>
            </ul>
''' % (li_attr, button)

        return html

    def disabledEdit(self):
        """ Return a disabled edit link """
        _ = self.request.getText
        html = u'%s%s%s' % (self.request.formatter.url(1, css="menu-nav-edit"),
                            _('Immutable Page'),
                            self.request.formatter.url(0)
                           )
        return html

    def commentbutton(self):
        """
        Return a comment toggle button html.
        Don't check if 'Comment' is present in self.request.cfg.edit_bar
        The button is display:none; (i.e. disappeared) by default, but will automatically appear
        when default javascript notices there is a comment in the source.
        """
        _ = self.request.getText
        html = u'''
            <ul class="nav navbar-nav navbar-right toggleCommentsButton" style="display:none;">
              <li>
                <a href="#" class="menu-nav-comment nbcomment" rel="nofollow" onClick="toggleComments();return false;">%s</a>
              </li>
            </ul>
''' % _('Comments')
        return html

    def username(self, d):
        """ Assemble the username / userprefs link as dropdown menu
        Assemble a login link instead in case of no login user.

        @param d: parameter dictionary
        @rtype: unicode
        @return: username html
        """
        request = self.request
        _ = request.getText

        userlinks = []
        userbutton = u''
        loginbutton = u''

        # Add username/homepage link for registered users. We don't care
        # if it exists, the user can create it.
        if request.user.valid and request.user.name:
            interwiki = wikiutil.getInterwikiHomePage(request)
            name = request.user.name
            aliasname = request.user.aliasname
            if not aliasname:
                aliasname = name
            title = "%s @ %s" % (aliasname, interwiki[0])
            # make user button
            userbutton = u'%s<span class="nav-maxwidth-100">%s</span><span class="padding"></span><span class="caret"></span>%s' % (
                request.formatter.url(1, url="#", css="menu-nav-user dropdown-toggle", **{"data-toggle": "dropdown", "rel": "nofollow"}),
                request.formatter.text(name),
                request.formatter.url(0),
                )
            # link to (interwiki) user homepage
            wikitag, wikiurl, wikitail, wikitag_bad = wikiutil.resolve_interwiki(self.request, *interwiki)
            wikiurl = wikiutil.mapURL(self.request, wikiurl)
            href = wikiutil.join_wiki(wikiurl, wikitail)
            homelink = (request.formatter.url(1, href, title=title, css='menu-dd-userhome', rel="nofollow") +
                       request.formatter.text(name) +
                       request.formatter.url(0))
            userlinks.append(homelink)

            # link to userprefs action
            if 'userprefs' not in self.request.cfg.actions_excluded:
                userlinks.append(d['page'].link_to_raw(request, text=_('Settings'), css_class='menu-dd-userprefs',
                                                       querystr={'action': 'userprefs'}, rel='nofollow'))
            # logout link
            if request.user.auth_method in request.cfg.auth_can_logout:
                userlinks.append(d['page'].link_to_raw(request, text=_('Logout'), css_class='menu-dd-logout',
                                                       querystr={'action': 'logout', 'logout': 'logout'}, rel='nofollow'))
        else:
            query = {'action': 'login'}
            # special direct-login link if the auth methods want no input
            if request.cfg.auth_login_inputs == ['special_no_input']:
                query['login'] = '1'
            if request.cfg.auth_have_login:
                loginbutton = (d['page'].link_to_raw(request, text=_("Login"),
                                                 querystr=query, css_class='menu-nav-login', rel='nofollow'))

        if userbutton:
            userlinks_html = u'</li>\n                  <li>'.join(userlinks)
            html = u'''
              <li class="dropdown">
                %s
                <ul class="dropdown-menu">
                  <li>%s</li>
                </ul>
              </li> <!-- /dropdown -->
''' % (userbutton, userlinks_html)

        elif loginbutton:
            html = u'''
              <li>
                %s
              </li>
''' % loginbutton

        else:
            html = u''

        return html

    def menu(self, d):
        """
        Build dropdown menu html. Incompatible with original actionsMenu() method.

        Menu can be customized by adding a config variable 'memodump_menuoverride'.
        The variable will override the default menu set.

        @param d: parameter dictionary
        @rtype: string
        @return: menu html
        """
        request = self.request
        _ = request.getText
        rev = request.rev
        page = d['page']

        page_recent_changes = wikiutil.getLocalizedPage(request, u'RecentChanges')
        page_find_page = wikiutil.getLocalizedPage(request, u'FindPage')
        page_help_contents = wikiutil.getLocalizedPage(request, u'HelpContents')
        page_help_formatting = wikiutil.getLocalizedPage(request, u'HelpOnFormatting')
        page_help_wikisyntax = wikiutil.getLocalizedPage(request, u'HelpOnMoinWikiSyntax')
        page_title_index = wikiutil.getLocalizedPage(request, u'TitleIndex')
        page_word_index = wikiutil.getLocalizedPage(request, u'WordIndex')
        page_front_page = wikiutil.getFrontPage(request)
        page_sidebar = Page(request, request.getPragma('sidebar', u'SideBar'))
        quicklink = self.menuQuickLink(page)
        subscribe = self.menuSubscribe(page)

        try:
            menu = request.cfg.memodump_menuoverride
        except AttributeError:
            # default list of items in dropdown menu
            menu = [
                '__title_navigation__',
                'RecentChanges',
                'FindPage',
                'LocalSiteMap',
                '__separator__',
                '__title_display__',
                'raw',
                'print',
                '__separator__',
                '__title_help__',
                'HelpContents',
                'HelpOnMoinWikiSyntax',
                '__separator__',
                '__title_edit__',
                'RenamePage',
                'DeletePage',
                'CopyPage',
                'Load',
                'Save',
                '__separator__',
                '__title_admin__',
                'Despam',
                'editSideBar',
                '__separator__',
                '__title_page__',
                'AttachFile',
                'info',
                'quicklink',
                ]

        # menu element definitions
        menu_def = {
            # actions
            'raw': {'title': _('Raw Text'), # title for menu entry
                    'href': '', # nonexistant or empty for current page
                    'args': 'action=raw&rev=%s' % (rev or ''), # optionally specify this for <a href="href?args">
                    'special': self.menuActionIsRemoved(page, 'raw')
                    #'special' can be:
                    #  'disabled', 'removed', 'separator' or 'header' for whatever they say,
                    #  False, None or nonexistant means normal menu display
                    # 'separator' and 'header' are automatically removed when there are no entries to show among them.
                   },
            'print':           {'title': _('Print View'), 'args': 'action=print&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'print')},
            'refresh':         {'title': _('Delete Cache'), 'args': 'action=refresh&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'refresh', not page.canUseCache())},
            'SpellCheck':      {'title': _('Check Spelling'), 'args': 'action=SpellCheck&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'SpellCheck')},
            'RenamePage':      {'title': _('Rename Page'), 'args': 'action=RenamePage&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'RenamePage')},
            'CopyPage':        {'title': _('Copy Page'), 'args': 'action=CopyPage&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'CopyPage')},
            'DeletePage':      {'title': _('Delete Page'), 'args': 'action=DeletePage&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'DeletePage')},
            'LikePages':       {'title': _('Like Pages'), 'args': 'action=LikePages&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'LikePages')},
            'LocalSiteMap':    {'title': _('Local Site Map'), 'args': 'action=LocalSiteMap&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'LocalSiteMap')},
            'MyPages':         {'title': _('My Pages'), 'args': 'action=MyPages&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'MyPages')},
            'SubscribeUser':   {'title': _('Subscribe User'), 'args': 'action=SubscribeUser&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'Subscribe User', not request.user.may.admin(page.page_name))},
            'Despam':          {'title': _('Remove Spam'), 'args': 'action=Despam&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'Despam', not request.user.isSuperUser())},
            'revert':          {'title': _('Revert to this revision'), 'args': 'action=revert&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'revert', not request.user.may.revert(page.page_name))},
            'PackagePages':    {'title': _('Package Pages'), 'args': 'action=PackagePages&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'PackagePages')},
            'RenderAsDocbook': {'title': _('Render as Docbook'), 'args': 'action=RenderAsDocbook&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'RenderAsDocbook')},
            'SyncPages':       {'title': _('Sync Pages'), 'args': 'action=SyncPages&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'SyncPages')},
            'AttachFile':      {'title': _('Attachments'), 'args': 'action=AttachFile&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'AttachFile')},
            'quicklink':       {'title': quicklink[1], 'args': 'action=%s&rev=%s' % (quicklink[0], rev or ''),
                                'special': not quicklink[0] and 'removed'},
            'subscribe':       {'title': subscribe[1], 'args': 'action=%s&rev=%s' % (subscribe[0], rev or ''),
                                'special': not subscribe[0] and 'removed'},
            'info':            {'title': _('Info'), 'args': 'action=info&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'info')},
            'Load':            {'title': _('Load'), 'args': 'action=Load&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'Load')},
            'Save':            {'title': _('Save'), 'args': 'action=Save&rev=%s' % (rev or ''),
                                'special': self.menuActionIsRemoved(page, 'Save')},
            # menu decorations
            '__separator__':   {'title': _('------------------------'), 'special': 'separator', },
            '----':            {'title': _('------------------------'), 'special': 'separator', },
            '__title_navigation__': {'title': _('Navigation'), 'special': 'header', },
            '__title_help__':  {'title': _('Help'), 'special': 'header', },
            '__title_display__': {'title': _('Display'), 'special': 'header', },
            '__title_edit__':  {'title': _('Edit'), 'special': 'header', },
            '__title_user__':  {'title': _('User'), 'special': 'header', },
            '__title_page__':  {'title': _('Page'), 'special': 'header', },
            '__title_admin__': {'title': _('Administration'), 'special': 'header'},
            # useful pages
            'RecentChanges':   {'title': page_recent_changes.page_name, 'href': page_recent_changes.url(request)},
            'FindPage':        {'title': page_find_page.page_name, 'href': page_find_page.url(request)},
            'HelpContents':    {'title': page_help_contents.page_name, 'href': page_help_contents.url(request)},
            'HelpOnFormatting': {'title': page_help_formatting.page_name, 'href': page_help_formatting.url(request)},
            'HelpOnMoinWikiSyntax': {'title': page_help_wikisyntax.page_name, 'href': page_help_wikisyntax.url(request)},
            'TitleIndex':      {'title': page_title_index.page_name, 'href': page_title_index.url(request)},
            'WordIndex':       {'title': page_word_index.page_name, 'href': page_word_index.url(request)},
            'FrontPage':       {'title': page_front_page.page_name, 'href': page_front_page.url(request)},
            'SideBar':         {'title': page_sidebar.page_name, 'href': page_sidebar.url(request)},
            'editSideBar':     {'title': _('Edit SideBar'), 'href': page_sidebar.url(request),
                                'args': 'action=edit', 'special': not self.menuPageIsEdittable(page_sidebar) and 'removed'},
            }

        menubody = self.menuAssemble(d, menu, menu_def)
        if menubody:
            html = u'''
              <li class="dropdown">
                <!-- Menu button -->
                <a href="#" class="menu-nav-menu dropdown-toggle" data-toggle="dropdown">
                  %s<span class="padding"></span><span class="caret"></span>
                </a>
                <!-- Dropdown contents -->
                <ul class="dropdown-menu">
%s
                </ul>
              </li> <!-- /dropdown -->
''' % (_('Menu'), menubody)
        else:
            html = u''

        return html

    def menuAssemble(self, d, menu, menu_def):
        request = self.request
        page = d['page']

        # subroutines
        def switch_default():
            if not data.get('href'):
                data['href'] = page.url(request)
            if data.get('args'):
                data['href'] = u'%(href)s?%(args)s' % data
            data['key'] = key
            return u'                  <li><a href="%(href)s" class="menu-dd-%(key)s" rel="nofollow">%(title)s</a></li>' % data
        def switch_disabled():
            data['key'] = key
            return u'                  <li class="disabled"><a href="#" class="menu-dd-%(key)s" rel="nofollow">%(title)s</a></li>' % data
        def switch_separator():
            return switch_separator_check(number) and u'                  <li class="divider"></li>'
        def switch_header():
            return switch_header_check(number) and u'                  <li class="dropdown-header">%(title)s</li>' % data
        def switch_removed():
            return u''
        switch = {
            False:       switch_default,
            None:        switch_default,
            'disabled':  switch_disabled,
            'separator': switch_separator,
            'header':    switch_header,
            'removed':   switch_removed,
            }

        # subroutines to determine whether a separator (or a header) should be removed or not
        def switch_separator_check(pos):
            current = pos + 1
            if menu[current:]:
                check_data = menu_def[menu[current]]
                return separator_check[check_data.get('special')](current)
            return False
        def switch_header_check(pos):
            current = pos + 1
            if menu[current:]:
                check_data = menu_def[menu[current]]
                return header_check[check_data.get('special')](current)
            return False
        separator_check = {
            False:       lambda x: True,
            None:        lambda x: True,
            'disabled':  lambda x: True,
            'separator': lambda x: False,
            'header':    switch_header_check,
            'removed':   switch_separator_check,
            }
        header_check = {
            False:       lambda x: True,
            None:        lambda x: True,
            'disabled':  lambda x: True,
            'separator': lambda x: False,
            'header':    lambda x: False,
            'removed':   switch_header_check,
            }

        # let's start
        lines = []
        for number, key in enumerate(menu):
            data = menu_def[key]
            line = switch[data.get('special')]()
            if line:
                lines.append(line)
        return u'\n'.join(lines)

    def menuActionIsRemoved(self, page, action, removeif=False, whattodo='removed'):
        """
        Return whattodo (defaults to 'removed') if action is to be removed by config.
        Or if optional condition removeif is True, the method returns whattodo.
        If conditions are met, return False.
        """
        request = self.request
        excluded = request.cfg.actions_excluded
        available = get_available_actions(request.cfg, page, request.user)
        return (action in excluded or (action[0].isupper() and not action in available) or removeif) and whattodo

    def menuPageIsEdittable(self, page):
        """
        Return True if page is edittable for current user, False if not.

        @param page: page object
        """
        return page.isWritable() and self.request.user.may.write(page.page_name)

    def menuQuickLink(self, page):
        """
        Return quicklink action name and localized text according to status of page

        @param page: page object
        @rtype: unicode
        @return (action, text)
        """
        if not self.request.user.valid:
            return (u'', u'')

        _ = self.request.getText
        if self.request.user.isQuickLinkedTo([page.page_name]):
            action, text = u'quickunlink', _("Remove Link")
        else:
            action, text = u'quicklink', _("Add Link")
        if action in self.request.cfg.actions_excluded:
            return (u'', u'')

        return (action, text)

    def menuSubscribe(self, page):
        """
        Return subscribe action name and localized text according to status of page

        @rtype: unicode
        @return (action, text)
        """
        if not ((self.cfg.mail_enabled or self.cfg.jabber_enabled) and self.request.user.valid):
            return (u'', u'')

        _ = self.request.getText
        if self.request.user.isSubscribedTo([page.page_name]):
            action, text = 'unsubscribe', _("Unsubscribe")
        else:
            action, text = 'subscribe', _("Subscribe")
        if action in self.request.cfg.actions_excluded:
            return (u'', u'')

        return (action, text)

    def trail(self, d):
        """ Assemble page trail

        @param d: parameter dictionary
        @rtype: unicode
        @return: trail html
        """
        _ = self.request.getText
        request = self.request
        user = request.user
        html = u''
        li = u'              <li>%s</li>'

        if not user.valid or user.show_page_trail:
            trail = user.getTrail()
            if trail:
                items = []
                for pagename in trail:
                    try:
                        interwiki, page = wikiutil.split_interwiki(pagename)
                        if interwiki != request.cfg.interwikiname and interwiki != 'Self':
                            link = (self.request.formatter.interwikilink(True, interwiki, page) +
                                    self.shortenPagename(page) +
                                    self.request.formatter.interwikilink(False, interwiki, page))
                            items.append(li % link)
                            continue
                        else:
                            pagename = page

                    except ValueError:
                        pass
                    page = Page(request, pagename)
                    title = page.split_title()
                    title = self.shortenPagename(title)
                    link = page.link_to(request, title)
                    items.append(li % link)

                html = u'''
          <div id="pagetrail">
            <h4>%s</h4>
            <ul>
%s
            </ul>
          </div>
''' % (_('Trail'), u'\n'.join(items))

        return html

    def navibar(self, d):
        _ = self.request.getText
        navihtml = ThemeBase.navibar(self, d)
        html = u'''
          <div id="navilinks">
            <h4>%s</h4>
%s
          </div>
''' % (_('Navigation'), navihtml)
        return html

    def quicklinks(self, d):
        """ Assemble quicklinks

        @param d: parameter dictionary
        @rtype: unicode
        @return: quicklinks html
        """
        _ = self.request.getText
        html = u''
        li = u'              <li class="%s">%s</li>'
        found = {}
        items = []
        current = d['page_name']

        userlinks = self.request.user.getQuickLinks()
        for text in userlinks:
            # non-localized anchor and texts
            pagename, link = self.splitNavilink(text, localize=0)
            if not pagename in found:
                if pagename == current:
                    cls = 'userlink active'
                    link = u'<a>%s</a>' % pagename
                else:
                    cls = 'userlink'
                items.append(li % (cls, link))
                found[pagename] = 1

        if items:
            html = u'''
          <div id="quicklinks">
            <h4>%s</h4>
            <ul>
%s
            </ul>
          </div>
''' % (_('Quick links'), u'\n'.join(items))

        return html

    def msg(self, d):
        """ Assemble the msg display

        Display a message in an alert box with an optional close button.

        @param d: parameter dictionary
        @rtype: unicode
        @return: msg display html
        """
        _ = self.request.getText
        msgs = d['msg']

        msg_conv = {
            'hint': 'alert-success',
            'info': 'alert-info',
            'warning': 'alert-warning',
            'error': 'alert-danger',
            }

        result = []
        template = u'''
          <div class="alert %(dismiss)s%(color)s">
            %(close)s
            %(msg)s
          </div>
'''
        param = {
            'close': u'<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>',
            'dismiss': 'alert-dismissable ',
            'msg': '',
            'color': '',
            }

        for msg, msg_class in msgs:
            param['color'] = msg_conv['info']
            try:
                param['msg'] = msg.render()
                param['close'] = ''
                param['dismiss'] = ''
            except AttributeError:
                if msg and msg_class:
                    param['msg'] = msg
                    if msg_class in msg_conv:
                        param['color'] = msg_conv[msg_class]
                elif msg:
                    param['msg'] = msg
            finally:
                if msg:
                    result.append(template % param)
        if result:
            return u'\n'.join(result)
        else:
            return u''

    def send_title(self, text, **keywords):
        """ Capture original send_title() and rewrite DOCTYPE for html5 """
        buffer = StringIO.StringIO()
        self.request.redirect(buffer)
        try:
            ThemeBase.send_title(self, text, **keywords)
        finally:
            self.request.redirect()
        html = re.sub(ur'^<!DOCTYPE HTML .*?>\n', ur'<!DOCTYPE html>\n', buffer.getvalue())
        self.request.write(html)

    def guiEditorScript(self, d):
        """ Disable default skin javascript to prevent gui edit button from automatically appear """
        return u''

    def _stylesheet_link(self, theme, media, href, title=None):
        """ Removed charset attribute to satisfy html5 requirements """
        if theme:
            href = '%s/%s/css/%s.css' % (self.cfg.url_prefix_static, self.name, href)
        attrs = 'type="text/css" media="%s" href="%s"' % (
                media, wikiutil.escape(href, True), )
        if title:
            return '<link rel="alternate stylesheet" %s title="%s">' % (attrs, title)
        else:
            return '<link rel="stylesheet" %s>' % attrs

def execute(request):
    """
    Generate and return a theme object

    @param request: the request object
    @rtype: MoinTheme
    @return: Theme object
    """
    return Theme(request)