import sys
import subprocess
from subprocess import *

XKB_PRINT = "setxkbmap -print | grep xkb_symbols | awk -F\"+\" '{print $2}'"

XKB_SET_PT = "setxkbmap pt"
XKB_SET_GB = "setxkbmap gb"

try:
   layout = check_output( XKB_PRINT, stderr=subprocess.STDOUT, shell=True ).strip()
except CalledProcessError as e:
   sys.exit( -1 )

switchCommand = XKB_SET_PT if layout == "gb" else XKB_SET_GB

try:
   call( switchCommand, shell=True )
except CalledProcessError as e:
   sys.exit( -2 )
