from browser import html
from javascript import JSObject

jq = jQuery.noConflict(True)

class Semantic(object):
    'Base class for class-controlled widget in Semantic-UI'
    def __init__(self):
        self._this = JSObject(jq(self.elt))

    def add_class(self, klass):
        self.set_class(self.class_name + ' ' + klass)

    def animate(self, test):
        print("I'm gunna wreck it:", test)
        #self._this.animate(*args)

    def hide(self):
        self._this.hide()

    def on(self, name, function):
        self._this.on(name, function)

    def remove_class(self, klass):
        self.set_class(self.class_name.replace(klass, ''))

    def show(self):
        self._this.show()

    def stop(self):
        self._this.stop()

    @staticmethod
    def setup(required, **kwargs):
        'Setup classes for Semantic Widgets'
        if not 'Class' in kwargs: # Class variable created if not provided
            print("Failed to find Class in",kwargs)
            kwargs['Class'] = ' '.join(reversed(required))
            return kwargs

        for klass in required: # Requred classes are added
            if not klass in kwargs['Class']:
                kwargs['Class'] = klass + ' ' + kwargs['Class']

        return kwargs

# Heere thar be Widgets!
# TODO: implement transition as an effect for Semantics
# TODO: implement form validation
# TODO: verify that this module meets with the style guides
class Accordion(Semantic, html.DIV):
    'Semantic UI Accordion'
    # TODO: implement
    pass


class Breadcrumb(Semantic, html.DIV):
    'Semantic UI Breadcrumb'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['breadcrumb', 'ui'], **kwargs)
        if 'divider' in kwargs: # Divider class is provided at creation
            self.divider = kwargs['divider']
            if not 'divider' in self.divider:
                self.divider += ' divider'
        else:
            self.divider = 'divider'
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

    def appendSection(self, value, **kwargs):
        if len(self.children) > 0: # Dividers are automatically added
            self <= html.I(Class=self.divider)
        kwargs = Semantic.setup(['section'], **kwargs) # Sections are added
        self <= html.A(value, **kwargs)

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

class Button(Semantic, html.DIV):
    'Semantic UI Button'
    # TODO: support animation
    def __init__(self, *args, **kwargs):
        print("Starting an icon with args:", args, "and kwargs:", kwargs)
        kwargs = Semantic.setup(['button', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class ButtonGroup(Semantic, html.DIV):
    'Semantic UI Buttons'
    # TODO: add cool or feature
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['buttons', 'ui'])
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Checkbox(Semantic, html.DIV):
    'Semantic UI Checkbox'
    # TODO: implement
    pass

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
        kwargs = Semantic.setup(['divider', 'ui'])
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Dropdown(Semantic, html.DIV):
    'Semantic UI Dropdown'
    # TODO: implement
    pass

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

class Item(Semantic, html.DIV):
    'Semantic UI Item'
    # TODO: implement
    pass

class Label(Semantic, html.DIV):
    'Semantic UI Label'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['label', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class List(Semantic, html.UL):
    'Semantic UI List'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['list'], **kwargs)
        html.UL.__init__(*args, **kwargs)
        Semantic.__init__(self)

class Loader(Semantic, html.DIV):
    'Semantic UI Loader'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['loader', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Menu(Semantic, html.DIV):
    'Semantic UI Menu'
    # TODO: implement
    pass

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
        Semantic.__init__(self)

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
        Semantic.__init__(self)

class Shape(Semantic, html.DIV):
    'Semantic UI Shape'
    # TODO: implement
    pass

class Sidebar(Semantic, html.DIV):
    'Semantic UI Sidebar'
    # TODO: implement
    pass

class Segment(Semantic, html.DIV):
    'Semantic UI Segment'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['segment', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Step(Semantic, html.DIV):
    'Semantic UI Step'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['step', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Steps(Semantic, html.DIV, list):
    'Semantic UI Step'
    def __init__(self, *args, **kwargs):
        kwargs = Semantic.setup(['steps', 'ui'], **kwargs)
        html.DIV.__init__(self, *args, **kwargs)
        Semantic.__init__(self)

class Table(Semantic, html.TABLE):
    'Semantic UI Table'
    # TODO: implement
    pass
