import pyfunkeys
import time

pyfunkeys.add_fn_key('caps lock')
pyfunkeys.add_fn_key('menu')
pyfunkeys.add_key_map('pause', 'playpause')
pyfunkeys.add_key_map('page up', 'volumeup')
pyfunkeys.add_key_map('page down', 'volumedown')

pyfunkeys.map_fn_keys()

while True:
    time.sleep(1e6)
