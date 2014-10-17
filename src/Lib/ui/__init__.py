from browser import html
from javascript import JSObject

# jQuery and Semantic-ui must be available
jq = jQuery.noConflict(True)
# DOMNode ELEMENTS are wrapped in jQuery JSObjects for use with JS libraries
jso = lambda x: JSObject(jq(x.elt))

class Semantic(object):
    'Base class for class-controlled widget in Semantic-UI'
    def __init__(self, function=None):
        self.this = jso(self)
        if function is not None: # Class names are sometimes used as functions
            setattr(self, function, getattr(self.this, function))

    def add_class(self, klass):
        self.set_class_name(self.class_name + ' ' + klass)

    def animation(self, *args):
        'jQuery .animate wrapper'
        if len(args) < 2: # Splat operator causes failure for JSObject
            raise TypeError("At least two arguments for animate")
        elif len(args) == 2: # Switch-like serial if used instead
            self.this.animate(args[0], args[1])
        elif len(args) == 3:
            self.this.animate(args[0], args[1], args[2])
        elif len(args) == 4:
            self.this.animate(args[0], args[1], args[2], args[3])
        return self

    def fadeOut(self):
        self.this.fadeOut()

    def hide(self):
        'jQuery .hide() wrapper'
        # TODO: implement all functionality
        self.this.hide()
        return self

    def on(self, name, function):
        'Semantic .on() wrapper'
        # TODO: replace with Brython binding
        self.this.on(name, function)
        return self

    def remove_class(self, klass):
        self.set_class_name(self.class_name.replace(klass, ''))

    def show(self):
        'jQuery .show() wrapper'
        # TODO: implement all functionality
        self.this.show()
        return self

    def stop(self):
        'jQuery .stop() wrapper'
        # TODO: implement all functionality
        self.this.stop()

    @staticmethod
    def setup(required, **kwargs):
        'Setup classes for Semantic Widgets'
        if not 'Class' in kwargs: # Class variable created if not provided
            kwargs['Class'] = ' '.join(reversed(required))
            return kwargs

        for klass in required: # Requred classes are added
            if not klass in kwargs['Class']:
                kwargs['Class'] = klass + ' ' + kwargs['Class']

        return kwargs

# Heere thar be Widgets!
# TODO: implement transition as an effect for Semantics
# TODO: implement form validation
class Accordion(Semantic, html.DIV):
    'Semantic UI Accordion'
    def __init__(self, *args, titles=None, contents=None, dropdown=None,
                 debug=False, performance=False, verbose=False, **kwargs):
        kwargs = Semantic.setup(['accordion', 'ui'], **kwargs)
        if titles is None: titles = []
        if contents is None: contents = []
        if dropdown is None: dropdown = Icon(Class='dropdown')
        self.titles, self.contents = [], []

        for title, content in zip(titles, contents):
            self.titles.append(html.DIV(dropdown.clone() + title,
                                        Class='title'))
            self <= self.titles[-1]

            if isinstance(content, Accordion):
                content.remove_class('ui') #Subaccordions break with this class
                content.accordion()
            self.contents.append(html.DIV(content, Class='content'))
            self <= self.contents[-1]
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self, 'accordion')
        self.accordion(debug, performance, verbose)

    def open(self, index):
        self.accordion('open', index)

    def close(self, index):
        self.accordion('close', index)

    def toggle(self, index):
        self.accordion('toggle', index)

class Breadcrumb(Semantic, html.DIV):
    'Semantic UI Breadcrumb'
    def __init__(self, *args, crumbs=None, divider=None, **kwargs):
        kwargs = Semantic.setup(['breadcrumb', 'ui'], **kwargs)
        if divider is None: divider = html.DIV('/', Class="divider")
        if crumbs is None: crumbs = []
        self.divider = divider
        for crumb in crumbs:
            self.append_section(crumb)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

    def append_section(self, value):
        if len(self.children) > 0: # Dividers are automatically added
            self <= self.divider.clone()
        if isinstance(value, str):
            self <= html.A(value, Class="section")
        else:
            self <= value

    def clear_class(self, klass):
        for index in [x for x in range(len(self.children)) if (x % 2)]:
            self.children[index].class_name = \
                self.children[index].class_name.replace(klass, '')

    def get(self, index):
        index = 2 * index - 1 if index > 0 else index
        return self.children[index]

    def place_class(self, klass):
        for index in [x for x in range(len(self.children)) if (x % 2)]:
            self.children[index].class_name += ' ' + klass

    def remove(self, index):
        index = 2 * index - 1 if index > 0 else index
        self.remove(self.children[index])
        if index > 0:
            self.remove(self.children[index - 1])

class Button(Semantic, html.BUTTON):
    'Semantic UI Button'
    def __init__(self, *args, visible=None, hidden=None, state=None,
                 **kwargs):
        kwargs = Semantic.setup(['button', 'ui'], **kwargs)
        html.BUTTON.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

        if visible is not None: # Visible content is added
            if isinstance(visible, str):
                self <= html.DIV(visible, Class="visible content")
            else: # This must be a DOMElement, classes are added
                for klass in [k for k in ('visible', 'content')
                    if not k in visible.class_name]:
                    visible.set_class_name(visible.class_name + ' ' + klass)
                self <= visible

        if hidden is not None:
            if isinstance(hidden, str):
                self <= html.DIV(hidden, Class="hidden content")
            else: # This must be a DOMElement, classes are added
                for klass in [k for k in ('hidden', 'content')
                    if not k in hidden.class_name]:
                    hidden.set_class_name(hidden.class_name + ' ' + klass)
                self <= hidden

        if state is not None:
            self.state(state)

    def state(self, dictionary):
        self.this.state(dictionary)

class ButtonGroup(Semantic, html.DIV):
    'Semantic UI Buttons'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['buttons', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Checkbox(Semantic, html.DIV):
    'Semantic UI Checkbox'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['checkbox', 'ui'], **kwargs)
        html.DIV.__init__(self, **kwargs)
        Semantic.__init__(self, 'checkbox')

        self <= html.INPUT(type='checkbox')
        if len(args) > 0:
            self <= html.LABEL(args[0])

        self.checkbox()

    def disable(self):
        self.checkbox('disable')

    def enable(self):
        self.checkbox('enable')

    def toggle(self):
        self.checkbox('toggle')

class Comments(Semantic, html.DIV):
    'Semantic UI Comments'
    # TODO: implement
    pass

class Dimmer(Semantic, html.DIV):
    'Semantic UI Dimmer'
    # TODO: implement
    pass

class Divider(Semantic, html.DIV):
    'Semantic UI Button'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['divider', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Dropdown(Semantic, html.DIV):
    'Semantic UI Dropdown'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['dropdown', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self, 'dropdown')

class Form(Semantic, html.DIV):
    'Semantic UI Form'
    # TODO: implement
    pass

class Feed(Semantic, html.DIV):
    'Semantic UI Form'
    # TODO: implement
    pass

class Grid(Semantic, html.DIV):
    'Semantic UI Form'
    # TODO: implement
    pass

class Header(Semantic, html.DIV):
    'Semantic UI Header'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['header'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Icon(Semantic, html.I):
    'Semantic UI Icon'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['icon'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Image(Semantic, html.IMG):
    'Semantic UI Image'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['image', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Item(Semantic, html.A):
    'Semantic UI Item'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['item'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Label(Semantic, html.DIV):
    'Semantic UI Label'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['label', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class List(Semantic, html.UL):
    'Semantic UI List'
    def __init__(self, items=None, *args, **kwargs):
        kwargs = Semantic.setup(['list'], **kwargs)
        html.UL.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

        if items is None: items = []
        for item in items:
            self <= html.LI(item)

class Loader(Semantic, html.DIV):
    'Semantic UI Loader'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['loader', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self, 'loader')

class Menu(Semantic, html.DIV):
    'Semantic UI Menu'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['menu', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Message(Semantic, html.DIV):
    'Semantic UI Message'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['message', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Modal(Semantic, html.DIV):
    'Semantic UI Modal'
    # TODO: implement
    pass

class Popup(Semantic, html.DIV):
    'Semantic UI Popup'
    # TODO: implement by overriding the __le__ method
    pass

class Progress(Semantic, html.DIV):
    'Semantic UI Progress'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['progress', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self, 'progress')

class Rating(Semantic, html.DIV):
    'Semantic UI Rating'
    # TODO: implement
    pass

class Reveal(Semantic, html.DIV):
    'Semantic UI Reveal'
    # TODO: complete and test
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['reveal', 'ui'], **kwargs)
        if not [anim for anim in ['fade', 'move', 'rotate']
            if anim in kwargs['Class']]: # A reveal must have an animation
            kwargs['Class'] += ' fade'
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self, 'reveal')

class Segment(Semantic, html.DIV):
    'Semantic UI Segment'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['segment', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Shape(Semantic, html.DIV):
    'Semantic UI Shape'
    # TODO: implement
    pass

class Sidebar(Semantic, html.DIV):
    'Semantic UI Sidebar'
    # TODO: implement
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['sidebar', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self, 'sidebar')

class Step(Semantic, html.DIV):
    'Semantic UI Step'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['step', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self, 'step')

class Steps(Semantic, html.DIV, list):
    'Semantic UI Step'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['steps', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self, 'steps')

class Submenu(Semantic, html.DIV):
    'Semantic UI Submenu (simply omits the ui class so text is well shown'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['menu'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Table(Semantic, html.TABLE):
    'Semantic UI Table'
    # TODO: implement
    pass
