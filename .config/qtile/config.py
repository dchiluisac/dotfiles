from typing import List  # noqa: F401

from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

#COLORS

colors = {
    'purple': '#cb39fd',
    'orange': '#FE8019',
    'blue': '#2eb0fb',
    'green': '#40e48e',
    'yellow': '#fdc33d',
    'black': '#220000',
    'red': '#fe7966',
    'greyBlack': '#333333',
    'grey': '#888888',
    'brown': '#C8C8A9',
    'redFull': '#FF0000'
}
fontSize = 20
separator = widget.TextBox(padding = 0, text = ' ', fontsize = fontSize + 44)
font = "SF Mono Bold" 
border = 1
border_focus = colors['greyBlack']
border_normal = colors['greyBlack']

keys = [
    # Switch between windows in current stack pane
    Key(["control"], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key(["control"], "i", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key(["control"], "j", lazy.layout.left(),
        desc="Move focus up in stack pane"),
    Key(["control"], "l", lazy.layout.right(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "i", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_left(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    #Key([mod], "space", lazy.layout.next(),
    #    desc="Switch window focus to other pane(s) of stack"),
    Key([mod], "space", lazy.spawn('/home/diego/myscripts/rof'),
        desc="Spawn Rof applications"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    #SHOW RANGER FILE MANAGER
    Key([mod], "m", lazy.spawn('alacritty -e sh -c "sleep 0.1 && ranger"'),
        desc="Show rager file manager"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    #mykeys
    Key(["mod1",], "space", lazy.spawn('/home/diego/myscripts/rof'),
        desc="Spawn Rof applications"),
    Key([mod,], "c", lazy.spawn('rofi -show calc'),
        desc="Spawn Rof calc"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn('/home/diego/myscripts/volumeUp'),
        desc="Raise volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn('/home/diego/myscripts/volumeDown'),
        desc="Lowe volume"),
    Key([], "XF86AudioMute", lazy.spawn('amixer sset Master,0 toggle'),
        desc="Mute"),
     Key([], 'XF86AudioStop',
        lazy.spawn(
            'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify '
            '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop')),
    Key([], 'XF86AudioNext',
        lazy.spawn(
            'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify '
            '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next')),
    Key([], 'XF86AudioPrev',
        lazy.spawn(
            'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify '
            '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous')),
    Key([], 'XF86MonBrightnessUp', lazy.spawn('/home/diego/myscripts/utils/subirBrillo.sh'),
            desc='brifhtness lower'),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('/home/diego/myscripts/utils/bajarBrillo.sh'),
            desc='brifhtness up'),
    Key([mod], 'F8', lazy.spawn('arandr'), 
            desc='Display')
]

groups = [
    Group("j", label="HOME", layout="monadtall"),
    Group("k", label="DEV", layout="monadtall"),
    Group("l", label="DB", layout="monadtall"),
    Group("i", label="CHAT", layout="monadtall"),
    Group("u", label="OTHERS", layout="monadtall"),
]

for i in groups:
    keys.extend([
        # mod + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=False),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    #layout.Max(),
    layout.MonadTall(
        margin = 10,
        border_focus = border_focus,
        border_normal = border_normal,
        border_width = border,
        ),
    layout.MonadWide(
        margin = 10,
        border_focus = border_focus,
        border_normal = border_normal,
        border_width = border
        ),
    #layout.Stack(
    #    num_stacks=2,
    #    margin = 10,
    #    border_focus = border_focus,
    #    border_normal = border_normal,
    #    border_width = border
    #),
    ## Try more layouts by unleashing below layouts.
     layout.Bsp(
        margin = 10,
        border_focus = border_focus,
        border_normal = border_normal,
        border_width = border
     ),
    # layout.Columns(
    #    margin = 10,
    #    border_focus = colors['purple'],
    #    border_normal = colors['black'],
    #    border_width = 0
    # ),
    #layout.Matrix(
    #    margin = 10,
    #    border_focus = colors['purple'],
    #    border_normal = colors['black'],
    #    border_width = 0
    #),
    # layout.RatioTile(
    #    margin = 10,
    #    border_focus = colors['purple'],
    #    border_normal = colors['black'],
    #    border_width = 0
    # ),
     layout.Tile(
        margin = 10,
        border_focus = border_focus,
        border_normal = border_normal,
        border_width = border
        ),
    # layout.TreeTab(
    #    margin = 10,
    #    border_focus = border_focus,
    #    border_normal = colors['black'],
    #    border_width = 0
    # ),
    # layout.VerticalTile(
    #    margin = 10,
    #    border_focus = colors['purple'],
    #    border_normal = colors['black'],
    #    border_width = 0
    # ),
    # layout.Zoomy(
    #    margin = 10,
    #    border_focus = colors['purple'],
    #    border_normal = colors['black'],
    #    border_width = 0
    # ),
]

widget_defaults = dict(
    font = font,
    fontsize = fontSize,
    padding = 0,
    margin = 0
)
extension_defaults = widget_defaults.copy()

#methods
def open_wifi_list_saved():
    qtile.cmd_spawn('alacritty -e /home/diego/myscripts/menu/index.js up')

def open_wifi_list():
    qtile.cmd_spawn('alacritty -e /home/diego/myscripts/menu/index.js c')

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    padding_x = 20,
                    borderwidth = 0,
                    #highlight_method = "text",
                    highlight_method = "block",
                    urgent_alert_method = "block",
                    active = colors['orange'],# deprecated
                    inactive = colors['grey'],
                    block_highlight_text_color = colors['greyBlack'],
                    this_current_screen_border= colors['green'],
                    this_screen_border = colors['green'], 

                    other_screen_border = colors['orange'],
                    other_current_screen_border = colors['orange'],

                    rounded = True,
                    disable_drag = True,
                    use_mouse_wheel = False
                    ),
                widget.Wallpaper( directory='~/Pictures/background/', label=''),
                widget.Spacer(),
                widget.Wlan(
                        foreground = colors['blue'],
                        mouse_callbacks = { 'Button1': open_wifi_list_saved, 'Button3': open_wifi_list }
                    ),
                
                widget.Prompt(),
                separator,
                widget.TextBox(padding = 0, text = 'Vol', foreground = colors['orange'], font = font),
                widget.TextBox(padding = 0, text = ' ', fontsize = fontSize - 1),
                widget.Volume(foreground = colors['orange']),
                separator, 
                widget.Battery(
                    format = '{char} {percent:2.0%}',
                    foreground = colors['yellow'],
                    low_foreground = colors['red'],
                    charge_char = "~",
                    discharge_char = "D",
                    empty_char = "L",
                    update_interval = 30,
                    ),
                separator,
                widget.Clock(
                    foreground = colors['green'],
                    format = '%a %I:%M %p', 
                    ),
                separator,
            ],
            30,
            opacity = 0.65,
        ),
    ),
    Screen(),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
margin = 10,
        border_focus = border_focus,
        border_normal = border_normal,
        border_width = border,
    default_float_rules = [
        Match(wm_type='utility'),
        Match(wm_type='notification'),
        Match(wm_type='toolbar'),
        Match(wm_type='splash'),
        Match(wm_type='dialog'),
        Match(wm_class='file_progress'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='Gpick'),
        Match(wm_class='androidemulator'),
    ],
)

main = None
auto_fullscreen = True
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "picom"
wmname = "LG3D"
