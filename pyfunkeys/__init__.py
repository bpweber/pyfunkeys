import os
import keyboard
import pyautogui

__version__ = '0.0.1'

pyautogui.PAUSE = 0.0

DOWN = 1
UP = 0

fn_layer_maps = {}
base_layer_maps = {}
fn_keys = []

def load_keys_from_config():
    with open(os.path.dirname(__file__) + '/maps.cfg') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i == 0:
                add_fn_keys(line.split(','))
            elif '->' in line:
                add_layer_map(fn_layer_maps, line.split('->'))
            elif ':' in line:
                add_layer_map(base_layer_maps, line.split(':'))

def add_layer_map(layer, keys):
    layer[keys[0].strip()] = keys[1].strip()

def add_fn_keys(keys):
    for key in keys:
        fn_keys.append(key.strip())

def fn(keypos):
    if keypos is DOWN:
        keyboard.unhook_all()
        map_keys(fn_layer_maps)
        map_fn_keys()
    else:
        keyboard.unhook_all()
        map_keys(base_layer_maps)
        map_fn_keys()

def map_keys(keys=base_layer_maps):
    for key, val in keys.items():
        if '+' in val:
            map_key(key, DOWN, pyautogui.hotkey, val.split('+'))
        else: 
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

