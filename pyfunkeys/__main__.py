import pyfunkeys
import time

if __name__ == '__main__':
    pyfunkeys.load_keys_from_config()
    pyfunkeys.map_fn_keys()
    while True:
        time.sleep(1e6)
