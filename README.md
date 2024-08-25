# pyfunkeys
## A wrapper for creating custom function layers in python
> [!NOTE]
> Key name syntaxes are from [keyboard](https://github.com/boppreh/keyboard) and [pyautogui](https://github.com/asweigart/pyautogui)

You can edit `./pyfunkeys/maps.cfg` to change key bindings.

Example config for vim style arrow/movement keys:
```
caps lock, menu
h -> left
j -> down
k -> up
l -> right
```

The first line of the config is used to define the key(s) used switch layers

Use a `,` to separate key names if binding more than one

`
caps lock
 ` 
or 
`
caps lock, menu
`

The remaining lines are used to define your key-map pairs, separated by a `->`

`h -> left`
