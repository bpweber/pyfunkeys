# pyfunkeys
## A wrapper for creating custom function layers in python
> [!NOTE]
> Key names are from [keyboard](https://github.com/boppreh/keyboard/blob/master/keyboard/_canonical_names.py) and [pyautogui](https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py)

Key bindings can be changed by editing `./pyfunkeys/maps.cfg`.

Below is an example config for adding vim style movement keys to the function layer:
```
caps lock, menu
h -> left
j -> down
k -> up
l -> right
```

The first line of the config defines the key(s) used switch layers. Use a `,` to separate key names if binding more than one:

`caps lock` or `caps lock, menu`

The remaining lines are used to define your key-map pairs, separated by a `->`:

`h -> left`
