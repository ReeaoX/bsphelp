#!/data/data/com.termux/files/usr/bin/python3
from rich import print as rprint, box as rbox
from rich.console import Console as rterm
from rich.table import Table as rtable
from decouple import config as pydefine
from dotenv import load_dotenv as dotload, find_dotenv as dotfind
import cli_box as cbox

"""Load the '.env'-formatted config through 'dotenv'."""
dotload(dotfind("dotenv-config.env"))

"""System variable through 'decouple'."""
PRINT_BOX_TYPE = pydefine("PRINT_BOX_TYPE", default="rounded")

"""Python variable."""
HELP_NON_TABLE_MESSAGE = """bsphelp ver. 0.0.1.
Powered by Python.

bspwn"""

"""Function the 'bprint' execute-able class."""
def bprint(pyinput):
    if PRINT_BOX_TYPE == "rounded":
       rprint(cbox.rounded(pyinput))
    elif PRINT_BOX_TYPE == "square":
       rprint(cbox.square(pyinput))
    elif PRINT_BOX_TYPE == "ascii":
       rprint(cbox.ascii(pyinput))
    else:
       exit(rprint("[red]Your env-powered box type is unknown.[/red]"), end="\r\n") # this would outputed, if you're didn't correct your env-powered box print.

"""Write the non-table message with the box. And next into the table message."""
bprint(HELP_NON_TABLE_MESSAGE)

"""Define 'pytable' variable through the 'rich'."""
pytable = rtable(box=rbox.ROUNDED) # you're able to configure this 'box' variable.

"""Create the column through the 'pytable'."""
pytable.add_column("Name.", justify="right", style="yellow")
pytable.add_column("Description.", justify="middle", style="blue")
pytable.add_column("Executable.", justify="middle", style="magenta")
pytable.add_column("Configurable.", justify="middle", style="yellow")
pytable.add_column("Require.", justify="left", style="magenta")

"""Create the row inside the column. But through the 'pytable'."""
pytable.add_row("bspwmrc", "The shebang-based configuration file, that let you execute while running 'bspwm'.", "Partially yes ('bspwm' needed).", "Yes.", "Yes.")
pytable.add_row("sxhkdrc", "The sxhkd-powered configuration file, that let you partially execute while running 'bspwm'.", "Partially yes.", "Yes.", "Partially no.")
pytable.add_row("picom", "The X11-based blur-able compositor, that let you round itself.", "Yes.", "Yes.", "No.")
# pytable.add_row("compton (forked into Picom.)", "The X11-based blur-able compositor. Where Picom forked from.", "Occuredly yes.", "Yes.", "No.") | disabled to focus in Termux needs.
# pytable.add_row("Unagi", "The unmaintained compositor.", "Partially yes.", "Yes.", "No.") | disabled to focus in Termux needs.
# pytable.add_row("dcompmgr (forked into Compton, where Picom forked from.)", "The xcompmgr-based active-able compositor, that determine 'x' from 'xcompmgr' name.", "Occuredly yes.", "Yes (without file config), along it's forked-from '.", "No.") | disabled to focus in Termux needs.
pytable.add_row("polybar", "The BSPWM replacement of i3status. But inside the status bar program workaround.", "Yes, partially needed 'POLYBAR_DISPLAY' variable.", "Yes.", "Partially no (with desktop), partially pre-true (without desktop).")
# pytable.add_row("lemonbar", "The lightweight replacement of i3status. But recursively based on XCB.", "Yes, partially needed 'LEMONBAR_DISPLAY' variable.", "Yes.", "Partially no (with desktop), Pre-true (without desktop).") | disabled for the reason Termux developers hate lemon.
# pytable.add_row("bspwmbar", "odknt's lightweight replacement of i3status. But required nerd font.", "Yes.", "Yes.", "Yes/no.") | disabled to focus in Termux needs.
pytable.add_row("eww/eyw", "The ElKowar\'s standalone widget written in the sister programming of Cargo \'Rust\'. But able to execute as the status bar.", "Partially yes, partially needed 'EWW_DISPLAY' variable.", "Yes.", "No (as the widget), Pre-true (as the status bar).")
# pytable.add_row("ags", "Aylur's Astal-based performace-able (in opening/closing of window) widget. But secondary based on TypeScript (at least they written in Golang (and Nix(?)/same programming)).", "Partially yes.", "Yes, same as EWW.", "No (as the widget), Pre-true (as the status bar). Same as EWW.") | disabled to focus in Termux needs, at least TypeScript is available in Termux through NPM.

"""Define 'rcon' variable united from 'rich'."""
rcon = rterm()

"""Write the table message through 'rich'."""
rcon.print(pytable)
