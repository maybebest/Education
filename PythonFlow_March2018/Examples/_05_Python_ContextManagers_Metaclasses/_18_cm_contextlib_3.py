
"""Context Manager with contextlib"""

from contextlib import ContextDecorator

class TagWrapper(ContextDecorator):
    def __init__(self, tag):
        self.tag = tag

    def __enter__(self):
        print('<%s>' % self.tag)
        return self

    def __exit__(self, *exc):
        print('</%s>' % self.tag)
        return False


@TagWrapper('div')
def emit_html():
    print('Here is some non-HTML')

emit_html()
# <div>
# Here is some non-HTML
# </div>

