# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.10.3 (main, Jul 25 2022, 17:09:16) [Clang 13.0.0 (clang-1300.0.27.3)]
# Embedded file name: /boot/LBBridge/lbcamera.py
# Compiled at: 2021-09-13 10:26:38
# Size of source mod 2**32: 238 bytes
from LBBridge import log
from LBBridge import config

log.init_logger("lbcamera")
from LBBridge import camera


def main():
    cfg = config.Config()
    serv = camera.CameraServer(cfg)
    serv.run()


if __name__ == "__main__":
    main()
