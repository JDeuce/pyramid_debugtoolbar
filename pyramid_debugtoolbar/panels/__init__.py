"""Base DebugPanel class"""

from pyramid.renderers import render

class DebugPanel(object):
    """
    Base class for debug panels.
    """
    # name = Base
    has_content = False # If content returns something, set to true in subclass

    # If the client is able to activate/de-activate the panel
    user_enable = False

    # Panel methods
    def __init__(self, vars=None):
        if vars is None:
            vars = {}
        self.vars = vars

        # If the client enabled the panel
        self.is_active = False

    def render(self, template_name, vars):
        return render(template_name, vars)

    def dom_id(self):
        return 'flDebug%sPanel' % (self.name.replace(' ', ''))

    def nav_title(self):
        """Title showing in toolbar"""
        raise NotImplementedError

    def nav_subtitle(self):
        """Subtitle showing until title in toolbar"""
        return ''

    def title(self):
        """Title showing in panel"""
        raise NotImplementedError

    def url(self):
        raise NotImplementedError

    def content(self):
        raise NotImplementedError

    # Standard middleware methods
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass

    def process_beforerender(self, event):
        pass
    

