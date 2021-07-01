import json
import sys

from LibRadar import LibRadar

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("LibRadar only takes 1 arguments.")
        print("Usage:")
        print("    $ python libradar.py example.apk")
        exit(1)
    apk_path = sys.argv[1]
    lrd = LibRadar(apk_path)
    res = lrd.compare()
    print(json.dumps(res, indent=4, sort_keys=True))