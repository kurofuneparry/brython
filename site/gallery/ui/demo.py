# -*- coding: utf-8 -*-
from browser import html
from javascript import JSObject
import ui

bug = '''
from browser import document, html

d = html.DIV()

# This list comprehension works outside of the exec statement
for a in [html.A("%s" % x) for x in ('a', 'b', 'c')]:
    d <= a

text = """
numbers = ['one', 'two', 'three']
print('This one works')
d <= html.A("Worked")
for a in [html.A("%s" % x) for x in range(1, 4)]:
    d <= a
"""

exec(text)

document['main'] <= d
'''

# Code to be evaluated to make the demo site
pages = {}

class Loader(object):
    "This class loads pages in the ui gallery example. Sorry, it's messy"
    # TODO: clean this up
    def __call__(self, page):
        return lambda event: self.load(page)

    def load(self, page):
        # The old contents of the page are removed
        self.segment.clear()
        self.main.clear()
        # Necessary data is gathered
        data = pages[page]
        # Header segment is added
        self.segment <= ui.html.DIV(
                    html.DIV(
                        html.H1(
                            page,
                            Class='ui dividing header') + html.P(data[0]),
                        Class='introduction',
                    ),
                    Class='container',
                )
        # Title is added
        self.main <= html.H2(
            'Examples' if not page in ('Overview','Advanced') else 'Details',
            Class="ui dividing header")
        # Examples are added
        for code in data[1]:
            hide_code = [] # mutable type may be changed by the code
            container = html.DIV(Class='example')
            exec(code) # code will put something in show_code to hide the code
            if not hide_code:
                # TODO: replace this with an ace-editor widget
                highlighted = ui.Segment(code, style={'height':'auto'})
                container <= highlighted
                self.main <= container
                editor = JSObject(ace).edit(highlighted.elt)
                editor.setTheme("ace/theme/chrome")
                editor.getSession().setMode("ace/mode/python")
                editor.setShowPrintMargin(False);
                editor.setReadOnly(True);
                editor.renderer.setShowGutter(False);
                editor.setHighlightActiveLine(False);
                editor.getSession().setUseWrapMode(True);
                editor.getSession().setTabSize(4);
                editor.getSession().setUseSoftTabs(True);
                length = editor.getSession().getScreenLength()
                length *= editor.renderer.lineHeight
                highlighted.style.height = length
                editor.resize()
            else:
                self.main <= container

    @staticmethod
    def make_menu():
        "Builds the elements in the sidebar menu. Sorry, it's messy"
        # TODO: remove submenu
        header = ui.Item(
                ui.Submenu(
                    ui.Item(ui.Image(src='../../brython_white.png'),
                    href="http://brython.info")))

        intros = Loader.build_menu_items('Introduction', [
            'Overview', 'Advanced'
        ])

        classes = Loader.build_menu_items('Classes', [
            'Accordion', 'Breadcrumb', 'Button', 'Checkbox',
            'Comments', 'Dimmer', 'Divider', 'Dropdown', 'Feed', 'Form',
            'Grid', 'Header', 'Icon', 'Image', 'Item', 'Label', 'List',
            'Loader', 'Menu', 'Message', 'Modal', 'Popup', 'Progress',
            'Rating', 'Reveal', 'Segment', 'Shape', 'Sidebar', 'Step',
            'Steps', 'Submenu', 'Table'
        ])

        behaviors = Loader.build_menu_items('Behaviors', ['Form Validation'])

        return header + intros + classes + behaviors

    @staticmethod
    def build_menu_items(title, items):
        items = [ui.Item(item) for item in items] # Menu items are made
        # TODO: replace submenu with just menu
        menu = ui.Submenu() # A submenu is created
        for each in items:
            menu <= each # And given all of the items
        # All of this is wrapped in a header
        menu = ui.Item(html.A(html.B(title)) + menu)

        # Click listeners are added to the menu items
        for item in items:
            item.bind('click', loader(item.text))

        return menu

loader = Loader()

# This is the data for the pages
pages['Overview'] = [
    "Brython's ui module wraps javascript's Semantic-ui/jQuery",
    [
"""
hide_code[0] = 'Hide'
text="Brython's ui module wraps the Semenatic-ui Javascript library."
container <= html.P(text)
""",
"""
container <= "This is a second example"
"""
    ],
]

pages['Advanced'] = [
    "Semantic-ui and jQuery methods can be used directly",
    [
"""
hide_code[0] = "Hide"
container <= html.P("The code for this section won't show up")
""",
    ],
]

pages['Accordion'] = [
    "Accordions include foldable content",
    [
"""
container <= html.H2("Generic Accordion")
dogs = {
    'titles' : (
        "What is a dog?",
        "What kinds of dogs are there?",
        "How do you acquire a dog?"
     ),

    'contents' :( # These will be the contents in the accordion sections
        html.P("A dog is a type of domesticated animal. Known for its loyalty and faithfulness, it can be found as a welcome guest in many households across the world."),
        html.P("There are many breeds of dogs. Each breed varies in size and temperament. Owners often select a breed of dog that they find to be compatible with their own lifestyle and desires from a companion."),
        html.P("Three common ways for a prospective owner to acquire a dog is from pet shops, private owners, or shelters.") + \
        html.P("A pet shop may be the most convenient way to buy a dog. Buying a dog from a private owner allows you to assess the pedigree and upbringing of your dog before choosing to take it home. Lastly, finding your dog from a shelter, helps give a good home to a dog who may not find one so readily.")
    )
}

container <=  ui.Accordion(**dogs)
""",
"""
container <= html.H2("Nesting")
container <= html.P('Accordions can be nested. Nested accordions must be reinitialized after being added to the DOM. This is done by calling .accordion()')
nested = ui.Accordion(titles=('Section 1', 'Section 2'),
    contents=(
        html.P('This is the first level of content') + ui.Accordion(
            debug=True, titles=('Section 1a', 'Section 1b'),
            contents=('This is Section 1a', 'This is Section 1b')
        ),
        ui.Accordion(debug=True, titles=('Section 2a', 'Section 2b'),
            contents=('This is Section 2a', 'This is Section 2b')
        ),
    )
)
container <= nested
nested.accordion()
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Variations")
container <= 'Variations on accordions are available:'
container <= "TODO: replace html lists with ui lists"
container <= html.UL(
    html.LI("Adding 'basic' to an accordion's classes removes any extra formatting.") + \
    html.LI("Adding 'fluid' to an accordion's classes makes it take up the width of it's container.")
)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Methods")
container <= 'Accordions present the following methods:' + \
html.UL(
    html.LI("open(index): Opens the content at index") + \
    html.LI("closes(index): Closes the content at index") + \
    html.LI("toggle(index): Toggles the content at index")
)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Settings")
container <= 'Accordions accept the following named settings:'
container <= html.UL(
    html.LI("exclusive=True: False allows multiple open sections") + \
    html.LI("collapsible=True: False allows no open section") + \
    html.LI("duration=500: Milliseconds for open/close transition") + \
    html.LI("easing=easeInOutQuint: See jQuery for other options")
)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Callbacks")
container <= 'Callbacks specify a function to occur after a behavior:' + \
html.UL(
    html.LI("onOpen(activeContent): When a section opens") + \
    html.LI("onClose(activeContent): When a section closes") + \
    html.LI("onChange(activeContent): When a section changes")
)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Debug Settings")
container <= 'Accordions have debug settings:' + \
html.UL(
    html.LI("debug=True: Provides standard debug output to console") + \
    html.LI("performance=True: Provides standard debug output to console") + \
    html.LI("verbose=True: Provides ancillary debug output to console")
)
""",
    ],
]

pages['Breadcrumb'] = [
    "A breadcrumb shows the location of the current section in relation to other sections.",
    [
"""
container <= html.H2("Generic Breadcrumb")
container <= html.P("A simple breadcrumb")
container <= ui.Breadcrumb(crumbs=['Food', 'Fruit', 'Apples'])
""",
"""
container <= html.H2("Custom Sections")
container <= html.P("Sections can be text or arbitrary DOM elements. The following sections will print their name to the javascript console when clicked.")
crumbs = [html.A('Food'), html.A('Fruit'), html.A('Apples')]
for crumb in crumbs:
    crumb.bind('click', lambda event: print(crumb.text))
container <= ui.Breadcrumb(crumbs=crumbs)
""",
"""
container <= html.H2("Custom Icons")
container <= html.P("Custom icons can be provided for a divider.")
divider = ui.Icon(Class="right arrow divider")
container <= ui.Breadcrumb(crumbs=['Food', 'Fruit', 'Apples'], divider=divider)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Variations")
container <= 'Variations on breadcrumbs are available:'
container <= html.UL(
    html.LI("Adding 'small'/'large'/'huge' to an breadcrumbs' classes changes size.") + \
    html.LI("The class 'active' can be added to any section.")
)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Methods")
container <= 'Breadcrumbs present the following methods:' + \
html.UL(
    html.LI("append_section(value): Appends a string or DOMElement as a section") + \
    html.LI("clear_class(klass): removes klass from all section's class list") + \
    html.LI("get(index): gets the section at the index value") + \
    html.LI("place_class(klass): adds klass to all section's class list") + \
    html.LI("remove(index): removes the section at the index value")
)
""",
    ],
]

pages['Button'] = [
    "Buttons indicate a possible user action.",
    [
"""
container <= html.H2("Generic Button")
container <= html.P("A standard button")
button = ui.Button('Follow')
button.state({
      'text': {
        'inactive' : 'Follow',
        'active'   : 'Following'
      }
    })
container <= button
""",
"""
container <= html.H2("Animation")
container <= html.P("A button can animate to show hidden content.")
container <= html.P("The button will be automatically sized according to the visible content size. Make sure there is enough room for the hidden content to show.")
container <= html.P("The visible/hidden content can be strings or DOMElements.")
container <= ui.Button(visible='Next',
                       hidden=ui.Icon(Class="right arrow"),
                       Class="animated")
container <= ui.Button(visible=ui.Icon(Class="cart"),
                       hidden="Shop",
                       Class="vertical animated")
container <= ui.Button(visible="Sign-up for a Pro account",
                       hidden="$12.99 a month",
                       Class="fade animated")
""",
"""
container <= html.H2("Icons")
container <= html.P("A button can have only an icon, or an icon and a label")
container <= ui.Button(ui.Icon(Class="cloud"), Class="icon")
container <= ui.Button(ui.Icon(Class="pause") + "Pause",
                       Class="labeled icon")
container <= ui.Button(ui.Icon(Class="right arrow") + "Next",
                       Class="labeled icon")
""",
"""
container <= html.H2("Groups")
container <= html.P("Buttons can exist together as a group")
buttons = ui.Button('One') + ui.Button('Two') + ui.Button('Three')
container <= ui.ButtonGroup(buttons)
""",
"""
container <= html.H2("Multiple Icons")
container <= html.P("Button groups can show groups of icons")
group1 = ui.Button(ui.Icon(Class='align left')) + ui.Button(ui.Icon(Class='align center')) + ui.Button(ui.Icon(Class='align right')) + ui.Button(ui.Icon(Class='align justify'))
group2 = ui.Button(ui.Icon(Class='bold')) + ui.Button(ui.Icon(Class='underline')) + ui.Button(ui.Icon(Class='text width'))
container <= ui.ButtonGroup(group1) + html.BR() + html.BR()
container <= ui.ButtonGroup(group2)
""",
"""
container <= html.H2("Conditionals")
container <= html.P("Button groups can be separated by conditionals")
buttons = ui.Button('Cancel') + html.DIV(Class='or') + ui.Button('Save', Class="positive")
container <= ui.ButtonGroup(buttons)
""",
"""
container <= html.H2("Social Formatting")
container <= html.P("Buttons can take their formatting from social websites.")
for name in ('facebook', 'twitter', 'google plus', 'vk'):
    container <= ui.Button(ui.Icon(Class=name) + name, Class=name)
container <= html.BR() + html.BR()
for name in ('linkedin', 'instagram', 'youtube'):
    container <= ui.Button(ui.Icon(Class=name) + name, Class=name)
""",
"""
container <= html.H2("Attached Buttons")
container <= html.P("A button can be attached to the top or bottom of other content.")
container <= ui.Button('Top', Class='attached top')
container <= ui.Button('Middle', Class='attached')
container <= ui.Button('Bottom', Class='attached bottom')
container <= html.P("A button can be attached to the left or right of other content.")
container <= ui.Button('Left', Class='left attached')
container <= ui.Button('Right', Class='right attached')
""",
"""
container <= html.H2("ButtonGroups Affect Formatting")
container <= html.P("Groups can be formatted to appear vertically")
group1 = ui.ButtonGroup(Class='vertical')
group1 <= ui.Button("Top") + ui.Button("Middle") + ui.Button("Bottom")
container <= group1
container <= html.P("Groups can be formatted as icons. 'labeled icons' also works.")
group2 = ui.ButtonGroup(Class='icon')
group2 <= ui.Button(ui.Icon(Class='pause')) + ui.Button(ui.Icon(Class='play')) + ui.Button(ui.Icon(Class='shuffle'))
container <= group2
""",
"""
container <= html.H2("ButtonGroups Can Organize By Number")
container <= html.P("Enumeration can be with numbers.")
group1 = ui.ButtonGroup(Class="3 fluid")
group1 <= ui.Button("One") + ui.Button("Two") + ui.Button("Three")
container <= group1 + html.BR() + html.BR()
container <= html.P("Enumeration can also be with words.")
group2 = ui.ButtonGroup(Class="twelve fluid icon")
for name in ('tag', 'tags', 'tasks', 'terminal', 'text file',
             'text file outline', 'time', 'trash', 'url', 'user', 'users',
             'video'):
    group2 <= ui.Button(ui.Icon(Class=name))
container <= group2
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Variations")
container <= 'Variations on buttons are available:'
container <= html.UL(
    html.LI("Adding 'basic' to an buttons's classes removes formatting.") + \
    html.LI("Adding 'hover' to an buttons's classes adds a hover animation.") + \
    html.LI("Adding 'down' to an buttons's classes adds an animation when pressed.") + \
    html.LI("Adding 'active' to an buttons's classes indicates it is the user's current selection.") + \
    html.LI("Adding 'loading' to an buttons's classes shows a loading indicator.") + \
    html.LI("Adding 'primary'/'secondary' shows levels of emphasis.") + \
    html.LI("Adding 'mini'/'tiny'/'small'/'medium'/'large'/'big'/'huge'/'massive' changes size.") + \
    html.LI("Adding 'inverted' to an buttons's classes inverts colors.") + \
    html.LI("Colors are available: 'black'/'green'/'red'/'blue'/'purple'/'teal'/'orange'") + \
    html.LI("Adding 'toggle' to an buttons's classes makes it a toggle button.") + \
    html.LI("Add 'positive'/'negative' for feedback indicators.") + \
    html.LI("Add 'fluid' to make a button that fills it's container.") + \
    html.LI("Add 'circular' to make a circular button.")
)
""",
    ],
]

pages['Checkbox'] = [
    "A checkbox visually indicates the status of a user's selection",
    [
"""
container <= "TODO: Labels here should be ui.Label type"
container <= html.H2("Basic Checkbox")
container <= html.P("A standard checkbox")
container <= ui.Checkbox('I enjoy having fun')
""",
"""
container <= html.H2("Alternative Checkboxs")
container <= html.P("Variant checkboxes are also available: slider and toggle.")
container <= ui.Checkbox('Taking dog for a walk', Class='slider')
container <= html.BR() + html.BR()
container <= ui.Checkbox('Allow other to pet my dog', Class='toggle')
""",
"""
container <= html.H2("Radio Box")
container <= html.P("TODO: Implement this after forms are developed")
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Variations")
container <= html.P('Variations on buttons are available:')
container <= html.UL(
    html.LI("Size classes, like 'large'/'huge' can be added.")
)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Methods")
container <= html.P('Accordions present the following methods:')
container <= html.UL(
    html.LI("enable(): Changes to enabled state.") + \
    html.LI("disable(): Changes to disabled state.") + \
    html.LI("toggle(): Checkbox state is toggled.")
)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Settings")
container <= "TODO: settings have not yet been tested."
container <= html.UL(
    html.LI("required='auto': Indicates if a response is required. 'auto' indicates True for Radio Boxes") + \
    html.LI("context=False: Selector or jQuery object to use as a delegated event context.")
)
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Callbacks")
container <= html.P("Callbacks specify a function to occur after a specific behavior.")
container <= html.UL(
    html.LI("onChange: Callback after a checkbox is either disabled or enabled.") + \
    html.LI("onEnabled: Callback after a checkbox is enabled.") + \
    html.LI("onDisable: Callback after a checkbox is disabled.")
)
""",
    ]
]

pages['Comments'] = [
    "A comment view is used to display lists of user feedback to site content",
    [
"""
hide_code[0] = 'Hide'
container <= html.P("This will be implemented later as it's more involved.")
""",
    ],
]

pages['Dimmer'] = [
    "Dimmers hide distractions to focus user's attention on particular content",
    [
"""
hide_code[0] = 'Hide'
container <= html.P("This will be implemented after I get internet again.")
""",
    ],
]

pages['Divider'] = [
    "A divider visually segment's content into separate groups.",
    [
"""
container <= ui.Message("Grid rows don't used dividers. Instead add the 'divided' class to the grid", Classes="ignored warning")
container <= html.H2("Generic Divider")
container <= html.P("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec odio.")
container <= ui.Divider()
container <= html.P("Quisque volutpat mattis eros. Nullam malesuada erat ut turpis.")
""",
"""
container <= html.H2("Vertical Divider")
container <= html.P("Content can be vertically divided using a grid.")
container <= html.P("TODO: replace this when grid is done formally.")
segment = ui.Segment(Class='two column middle aligned relaxed basic grid')
segment <= html.DIV("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", Class='column')
segment <= ui.Divider(Class='vertical')
segment <= html.DIV("Quisque volutpat mattis eros. Nullam malesuada erat ut turpis.", Class='column')
container <= segment
""",
"""
container <= html.H2("Icon Divider")
container <= html.P("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec odio.")
container <= ui.Divider(ui.Icon(Class='circular heart'))
container <= html.P("Quisque volutpat mattis eros. Nullam malesuada erat ut turpis.")
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Variations")
container <= 'Variations on dividers are available:'
container <= html.UL(
    html.LI("Adding 'inverted' to an divider's classes inverts the colors.") + \
    html.LI("Adding 'fitted' removes padding before and after.") + \
    html.LI("Adding 'section' provides greater margins to divide sections of content.") + \
    html.LI("Adding 'clearing' can clear the contents above it.")
)
""",
    ],
]

pages['Dropdown'] = [
    "A dropdown is a revealable list of selections.",
    [
"""
hide_code[0] = 'Hide'
container <= html.P("This will be implemented after I get internet again.")
""",
    ],
]

pages['Feed'] = [
    "A feed presents user activity chronologically.",
    [
"""
hide_code[0] = 'Hide'
container <= html.P("This will be implemented after I get internet again.")
""",
    ],
]

pages['Form'] = [
    "A form is a collection of user input elements.",
    [
"""
hide_code[0] = 'Hide'
container <= html.P("Forms always include fields, and fields always contain form elements. Fields themselves may also include inputs, standard form fields, labels, selection dropdowns, textareas, checkboxes, and message blocks.")
container <= html.P("This will be implemented after the above list of objects are implemented.")
""",
    ],
]

pages['Grid'] = [
    "A grid is a structure used to harmonize negative space in a layout.",
    [
"""
hide_code[0] = 'Hide'
container <= html.P("This will be implemented after I get internet again.")
""",
    ],
]

pages['Header'] = [
    "Headers provide a short summary of content'.",
    [
"""
container <= html.H2("Generic Header")
container <= html.P("A standard header.")
container <= ui.Header("Account Settings")
""",
"""
container <= html.H2("Descriptive Headers")
container <= "TODO: implement a content class rather than use HTML"
container <= "TODO: implement headers instead of using html.H2"
container <= html.P("Headers may have sub headers containing further context.")
container <= ui.Header(ui.Icon(Class='settings') + html.DIV(Class='content',
    "Account Settings" + ui.Header(Class='sub',
        "Manage your account settings and set e-mail preferences."
    )
))
""",
"""
container <= html.H2("Icon Headers")
container <= html.P("Adding 'icon' to a headers classes emphasizes icons.")
container <= ui.Header(Class='icon',
    ui.Icon(Class='circular question') + ui.Header(Class='sub',
        "Have any questions? Contact us."
    )
)
""",
"""
container <= html.H2("Section on header size omitted")
container <= "TODO: consider doing this section when I can compare results."
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Variations")
container <= 'Variations on headers are available:'
container <= ui.List(items=[
    "Adding 'disabled' to a header's classes formats it as disabled.",
    "Adding 'attached' makes the header attached to nearby objects.",
    "'right floated' makes the header float to the right of content.",
    "'left floated' makes the header float to the right of content.",
    "'left aligned' makes the content aligned to the left.",
    "'right aligned' makes the content aligned to the right.",
    "'center aligned' makes the content aligned to the center.",
    "'justified' makes the content justified.",
    "'black'/'blue'/etc can be used to color the headers.",
    "'dividing' makes the header automatically divide itself from content below.",
    "'block' causes the header to create a block.",
    "'inverted' inverts the coloring of the header."
])
"""
    ],
]

pages['Icon'] = [
    "An icon represents a concept. For a complete gallery, see: " + \
    html.A("semantic-ui's website", href="//semantic-ui.com/elements/icon.html")
    [
"""
hide_code[0] = "Hide"
container <= html.H2("Variations")
container <= 'Variations on icons are available:'
container <= ui.List(items=[
    "Adding 'disabled' to an icon's classes formats it as disabled.",
    "Adding 'attached' makes the header attached to nearby objects.",
    "'right floated' makes the header float to the right of content.",
    "'left floated' makes the header float to the right of content.",
    "'left aligned' makes the content aligned to the left.",
    "'right aligned' makes the content aligned to the right.",
    "'center aligned' makes the content aligned to the center.",
    "'justified' makes the content justified.",
    "'black'/'blue'/etc can be used to color the headers.",
    "'dividing' makes the header automatically divide itself from content below.",
    "'block' causes the header to create a block.",
    "'inverted' inverts the coloring of the header."
])
"""
    ],
]

pages['Image'] = [
    "An image is a graphic representation.",
    [
"""
container <= ui.Message("Images will, by default, take up the same size as the original image. Specifying an image size will force an image to only take up a specific size.",
                        Class='ignored info')
container <= "TODO: This will be completed with images are downloaded for testing."
""",
    ],
]

pages['Label'] = [
    "Labels give descriptions to pieces of content.",
    [
"""
container <= html.H2("Generic Label")
container <= html.P("A basic label.")
container <= ui.Label(ui.Icon(Class='mail') + '23')
""",
"""
container <= html.H2("Detail Label")
container <= html.P("A label can contain a detail.")
container <= ui.Label("Dogs" + html.DIV('214', Class='detail'))
""",
"""
container <= html.H2("Label's with inclusions")
container <= html.P("A label can contain arbitrary text, DOMNodes, and ui objects.")
container <= ui.Label("Witty" + ui.Icon(Class='delete'))
container <= ui.Label("Inbox" + html.A(
                                       ui.Icon(Class='mail') + '23',
                                       Class='detail'))
container <= "TODO: images need to be added to the website. To be completed after image section is done."
container <= html.("If the label contains an image, add 'image' to it's class.")
""",
    ],
]

pages['Message'] = [
    "Messages alert a user to information.",
    [
"""
container <= html.H2("Generic Message")
container <= ui.Message(
    ui.Header("Welcome Back") + html.P("It's good to see you again.")
)
""",
"""
container <= html.H2("Messages with Inclusions")
container <= html.P("Arbitrary DOMElements and ui Elements can be included, but sometimes a class should be added to the message.")
container <= ui.Message(
    ui.Header("Welcome Back") + ui.List(items=[
        "It's good to see you again", "Did you know it's been a while?"
    ])
)
container <= ui.Message(Class='icon',
    ui.Icon(Class='inbox') + html.DIV(
        Class='content',
        ui.Header("Have you heard about our mailing list?") + html.P("Get invitations in your e-mail every day. Sign up now!")
    )
)
""",
"""
container <= html.H2("Dismissable Block")
closable = ui.Message(ui.Icon(Class='close') + ui.Header("Welcome Back!") + \
    html.P("Dismiss this by clicking it.")
)
closable.bind('click', lambda event: closable.fadeOut())
container <= closable
container <= ui.Message(Class='warning',
    html.P("Dismissable blocks do not automatically close. See the code below for an example implementation.")
)
container <= "TODO: verify that all .fadeOut() options are implemented."
""",
"""
hide_code[0] = "Hide"
container <= html.H2("Variations")
container <= 'Variations on messages are available:'
container <= ui.List(items=[
    "Adding 'hidden' to classes hides the message.",
    "Adding 'small'/'large'/'big'/'huge'/'massive' changes size.",
    "Adding 'link' formats the icon as a link during hover etc.",
    "Adding 'horizontally flipped' flips the icon horizontally.",
    "Adding 'vertically flipped' flips the icon vertically.",
    "Adding 'horizontally flipped' flips the icon horizontally.",
    "Adding 'clockwise rotated' rotates the icon clockwise.",
    "Adding 'counterclockwise rotated' rotates the icon counterclockwise.",
    "Adding 'circular' makes the icon circular.",
    "Adding 'inverted' inverts the icon's colors.",
    "Adding 'square' makes the icon square.",
    "Colors are available: 'black'/'blue'/'red'/'green'/'purple'/'teal'",
])
"""
    ],
]

pages['Template'] = [
    "This is the subtitle",
    [
"""
container <= html.H2("Template with code")
container <= html.P("This is an example of code")
""",
"""
hide_code[0] = 'Hide'
container <= html.H2("Template without code")
container <= html.P("The code for this section will be hidden")
""",
    ],
]
