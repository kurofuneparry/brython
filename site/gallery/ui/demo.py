# -*- coding: utf-8 -*-
from browser import html, alert

# Bulk objects for making the demo site
latin1 = "Mauris mauris ante, blandit et, ultrices a, suscipit eget, quam. Integer ut neque. Vivamus nisi metus, molestie vel, gravida in, condimentum sit amet, nunc. Nam a nibh. Donec suscipit eros. Nam mi. Proin viverra leo ut odio. Curabitur malesuada. Vestibulum a velit eu ante scelerisque vulputate."
latin2 = "Sed non urna. Donec et ante. Phasellus eu ligula. Vestibulum sit amet purus. Vivamus hendrerit, dolor at aliquet laoreet, mauris turpis porttitor velit, faucibus interdum tellus libero ac justo. Vivamus non quam. In suscipit faucibus urna."
latin3 = "Nam enim risus, molestie et, porta ac, aliquam ac, risus. Quisque lobortis. Phasellus pellentesque purus in massa. Aenean in pede. Phasellus ac libero ac tellus pellentesque semper. Sed ac felis. Sed commodo, magna quis lacinia ornare, quam ante aliquam nisi, eu iaculis leo purus venenatis dui."
latin4 = "Cras dictum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aenean lacinia mauris vel est."
latin5 = "Suspendisse eu nisl. Nullam ut libero. Integer dignissim consequat lectus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."

dialog = "This is the default dialog which is useful for displaying information. The dialog window can be moved, resized and closed with the 'x' icon."

ul = html.UL()
ul <= html.LI("List item 1") + html.LI("List item 2") + html.LI("List item 3")

delphi_menu = html.LI('Delphi')
delphi_sub = html.UL()
delphi_sub <= html.LI('Ada', Class='ui-state-disabled') + \
               html.LI('Saarland') + html.LI('Salzburg an der schönen Donau')
delphi_menu <= delphi_sub

menu1 = html.LI('Aberdeen', Class='ui-state-disabled') + \
                html.LI('Ada') + html.LI('Adamsville') + \
                html.LI('Addyston') + delphi_menu.clone() + \
                html.LI('Saarland') + html.LI('Salzburg') + \
                delphi_menu.clone() + delphi_menu + html.LI('Perch') + \
                html.LI('Amesville', Class='ui-state-disabled')

speeds = ['Slower', 'Slow', 'Medium', 'Fast', 'Faster']

languages = ["ActionScript", "AppleScript", "Asp", "BASIC", "C", "C++",
           "Clojure", "COBOL", "ColdFusion", "Erlang", "Fortran", "Groovy",
           "Haskell", "Java", "JavaScript", "Lisp", "Perl", "PHP", "Python",
           "Ruby", "Scala", "Scheme"]

worked = lambda x: alert("It worked!")

# Demo objects gathered to be used
demo = {
    'Accordion' : { # Headers and Contents for Accordion provided
        'headers' : ["Section %s" % x for x in range(1,5)], # Headers
        'contents' : (
            html.P(latin1),
            html.P(latin2),
            html.P(latin3) + ul,
            html.P(latin4) + html.P(latin5)
        ),
    },
    'Autocomplete' : {'source' : languages},
    'Button' : {'label':'Test', 'click' : worked},
    'Datepicker' : {},
    'Dialog' : {'content' : html.P(dialog), 'title' : 'Basic Dialog'},
    'Menu' : {'content' : menu1, 'style' : {'width' : '150px'}},
    'Progressbar' : {'value' : 37},
    'Selectmenu' : {'content' : speeds, 'selected' : 2, 'width' : 200},
    'Slider' : {},
    'Spinner' : {},
    'Tabs' : { # Headers and Contents for Accordion provided
        'headers' : ["Section %s" % x for x in range(1,5)], # Headers
        'contents' : (
            html.P(latin1),
            html.P(latin2),
            html.P(latin3) + ul,
            html.P(latin4) + html.P(latin5)
        ),
    },
    'Tooltip' : {},
}

# Code to be evaluated to make the demo site
code = {
    'Accordion' : "a = ui.Accordion(**demo['Accordion'])\ncontainer <= a\na.refresh()",
    'Autocomplete' : "container <= ui.Autocomplete(**demo['Autocomplete'])",
    'Button' : "container <= ui.Button(**demo['Button'])",
    'Datepicker' : "container <= ui.Datepicker(**demo['Datepicker'])",
    'Dialog' : "d = ui.Dialog(**demo['Dialog'])",
    'Menu' : "container <= ui.Menu(**demo['Menu'])",
    'Progressbar' : "container <= ui.Progressbar(**demo['Progressbar'])",
    'Selectmenu' : "s = ui.Selectmenu(**demo['Selectmenu'])\ncontainer <= s\ns.initialize()",
    'Slider' : "container <= ui.Slider(**demo['Slider'])",
    'Spinner' : "container <= ui.Spinner(**demo['Spinner'])",
    'Tabs' : "container <= ui.Tabs(**demo['Tabs'])",
    'Tabsold' : "t = ui.Tabs(**demo['Tabs'])\ncontainer <= t\nt.refresh()",
    'Tooltip' : "container <= ui.Tooltip(**demo['Tooltip'])",
}
