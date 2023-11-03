import os
import socket
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile import layout, bar, widget, hook, qtile
from libqtile.command import lazy

def init_layout_theme():
    return {"margin":6,
            "border_width":1,
            "border_focus": "#05F9FF",
            "border_normal": "#f4c2c2"
            }


# COLORS FOR THE BAR

def bw_colors():
    return [
            ["#ffffff","#ffffff"], # White
            ["#000000","#000000"], # Black
            ["#999999","#999999"], # Grey 
            ["#5b5b5b","#5b5b5b"], # Dark grey
            ["#00000000","#00000000"], # Compositing
           ]  

colors = bw_colors()

# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 9,
                padding = 2,
                background=colors[2])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

                 widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        opacity = 0,
                        foreground = colors[4],
                        background = colors[4]
                        ),              
	              widget.Image(
                       filename = "~/.config/qtile/icons/arch-white.png",
                       iconsize = 9,
                       background = colors[4],
                       ),

              # widget.Spacer(),

               widget.GroupBox(

            background = colors[4],
            font='UbuntuMono Nerd Font',

                    fontsize = 17,
                    margin_y = 5,
                    margin_x = 3,
                    padding_y = 5,
                    padding_x = 4,
                    borderwidth = 1,

            active=colors[0],
            inactive=colors[3],
            rounded= True,
            highlight_method='line',
            highlight_color = colors[4],
            urgent_alert_method='block',
            urgent_border=colors[4],
            this_current_screen_border=colors[0],
            this_screen_border=colors[4],
            other_current_screen_border=colors[4],
            other_screen_border=colors[4],
            disable_drag=True


                   
                        ),


               widget.Spacer(),

               widget.Systray(
                       background=colors[4],
                       icon_size=20,
                       padding = 4
                      ),

               widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[4], # 3 is original
                       padding = 0,
                       scale = 0.7
                       ),


               widget.Clock(
                        foreground = colors[0],
                        background = colors[4], # 3 is original
                        fontsize = 14,
                        #format="%Y-%m-%d %H:%M"
                        format = "%d/%m  %H:%M"
                        ),


               widget.Battery(
                        background = colors[4], # 10 is original
                        foreground = colors[0],
                        fontsize = 14,
                        format = '{percent:2.0%}',
                        fmt = '{}'
                        ),

               #widget.BatteryIcon(),

                       

              ]
    return widgets_list




def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()

widgets_screen2 = init_widgets_screen2()

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=25, opacity=1.0, background= colors[4],margin=[5,1,1,1])),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=1.0, background= colors[4]))]

