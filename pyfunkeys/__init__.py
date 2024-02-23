import keyboard
import pyautogui

__version__ = '0.0.1'

pyautogui.PAUSE = 0.0

DOWN = 1
UP = 0

key_maps = {}

fn_keys = []

def add_key_map(key, map):
    key_maps[key] = map

def add_fn_key(key):
    fn_keys.append(key)

def fn(keypos):
    if keypos is DOWN:
        map_all_keys()
    else:
        keyboard.unhook_all()
        map_fn_keys()

def map_all_keys():
    for key, val in key_maps.items():
        map_key(key, DOWN, pyautogui.keyDown, val)
        map_key(key, UP, pyautogui.keyUp, val)

def map_fn_keys():
    for key in fn_keys:
        map_key(key, DOWN, fn)
        map_key(key, UP, fn)

def map_key(key, keypos, func, arg=None):
    arg = keypos if arg is None else arg
    if keypos is DOWN:
        keyboard.on_press_key(key, lambda e: func(arg), suppress=True)
    else:
        keyboard.on_release_key(key, lambda e: func(arg), suppress=True)
