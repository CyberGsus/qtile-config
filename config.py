"""
Qtile Config File
http://www.qtile.org/

Antonio Sarosi
https://www.youtube.com/channel/UCzTi9I3zApECTkukkMOpEEA/featured

Cyber Gsus
https://github.com/CyberGsus
"""

# Qtile Conf
from libqtile import layout
from libqtile.command import lazy

from libqtile.config import Click
from libqtile.config import Drag

# Custom Conf
from custom.bindings import mod
from custom.groups import init_groups
from custom.screens import init_screens
from custom.startup import keys
from custom.theme import colors
from custom.widgets import defaults  # Add-ons

# Basic Config

widget_defaults = defaults
extension_defaults = widget_defaults.copy()

# Workspaces

groups = init_groups(keys)

# Layouts

layout_config = dict(
    border_focus=colors["primary"][0],
    border_normal=colors["secondary"][0],
    border_width=1,
    margin=4,
)

layouts = [
    layout.Max(),
    layout.Bsp(fair=False, **layout_config),
    layout.Floating(**layout_config),
]

# Screens

screens = init_screens()

# Drag floating layouts

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size(),
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
    ],
    border_focus=colors["secondary"][0],
)
auto_fullscreen = True
focus_on_window_activation = "smart"


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's lightlist.
wmname = "LG3D"
