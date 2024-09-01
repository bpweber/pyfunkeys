# pyfunkeys
## A wrapper for [keyboard](https://github.com/boppreh/keyboard) to easily create custom function layers in python
> [!NOTE]
> Available key names can be found [here](https://github.com/boppreh/keyboard/blob/master/keyboard/_canonical_names.py)

> [!IMPORTANT]
> Please exit using a `KeyboardInterrupt` to allow for keys to be properly unhooked.

Key bindings can be changed by editing `./pyfunkeys/maps.cfg`

Below is an example config for adding vim style movement keys to the function layer:
```
caps lock, menu
h -> left
j -> down
k -> up
l -> right
w -> ctrl+right
b -> ctrl+left
windows : none
```

The first line of the config defines the key(s) used switch layers. Use a `,` to separate key names if binding more than one:

`caps lock` or `caps lock, menu`

The remaining lines are used to define your key-map pairs, separated by a `->`:

`h -> left`

Base layer keys can be remapped using the `:` separator. The line below will disable the Windows key on the base layer, but still allow for it to be used on the function layer:

`windows : none`

Function layer keys can also be mapped to hotkeys containing more than one key by using a `+` on the right side of the `->`. The lines below will remap `w` and `b` on the function layer to move forward and backward by one word in the current text:

`w -> ctrl+right` and `b -> ctrl+left`
