import pyfunkeys
import time

if __name__ == '__main__':
    pyfunkeys.on_init()
    try:
        while True:
            time.sleep(1e6)
    except KeyboardInterrupt:
        pyfunkeys.on_exit()

