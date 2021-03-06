from libqtile import widget
from libqtile.config import Key
from libqtile.command import lazy
from custom import functions

mod = "mod4"
alt = "mod1"


# redshift = RedShift([ 2400, 20000 ])

# Keyboard Layout
keyboard = widget.keyboardlayout.KeyboardLayout(
    configured_keyboards=["us", "es"], update_interval=0.3
)

keys = [
    # ------------ WINDOW CONFIGS ------------
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # Change window sizes (MonadTall)
    Key([mod, "shift"], "l", lazy.layout.grow()),
    Key([mod, "shift"], "h", lazy.layout.shrink()),
    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    # Kill window
    Key([mod], "w", lazy.window.kill()),
    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),
    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),
    # ------------ APPS CONFIG ------------
    # Menu
    # Key([mod], "m", lazy.spawn("rofi -show run")),
    # Window Nav
    # Key([mod, "shift"], "m", lazy.spawn("dmenu_run -p 'Run: '")),
    Key([mod, "shift"], "m", lazy.spawn("dmenu_run -p 'Run :'")),
    # Browser
    Key([mod], "b", lazy.spawn("qutebrowser")),
    # Discord
    Key([mod], "d", lazy.spawn("discord")),
    # File Manager
    Key([mod], "f", lazy.spawn("nautilus")),
    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),
    # Redshift
    # Key([mod], 'r', redshift.next),
    # Key([mod, "shift"], "r", redshift.reset),
    Key([mod], "r", lazy.spawn("redshift -PO 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),
    # ------------ HARDWARE CONFIG ------------
    # Volume
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),),
    Key([mod], "space", functions.next_keyboard_layout(keyboard))
    # Brightness
    # Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

# Special keybindings for different layouts
special_keys = dict(
    bsp=[
        Key([mod, alt], "j", lazy.layout.flip_down()),
        Key([mod, alt], "k", lazy.layout.flip_up()),
        Key([mod, alt], "h", lazy.layout.flip_left()),
        Key([mod, alt], "l", lazy.layout.flip_right()),
        Key([mod, "control"], "j", lazy.layout.grow_down()),
        Key([mod, "control"], "k", lazy.layout.grow_up()),
        Key([mod, "control"], "h", lazy.layout.grow_left()),
        Key([mod, "control"], "l", lazy.layout.grow_right()),
        Key([mod, "shift"], "n", lazy.layout.normalize()),
        Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    ],
)

for v in special_keys.values():
    keys.extend(v)


def get_keyboard():
    kbd = globals().get("keyboard", None)
    if kbd is None:
        raise ValueError("Keyboard not initialized")
    return kbd
