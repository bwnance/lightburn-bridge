# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.10.3 (main, Jul 25 2022, 17:09:16) [Clang 13.0.0 (clang-1300.0.27.3)]
# Embedded file name: /boot/LBBridge/lbpistatus.py
# Compiled at: 2021-09-13 10:26:38
# Size of source mod 2**32: 177 bytes
from LBBridge import log

log.init_logger("lbpistatus")
from LBBridge import pi_state


def main():
    ps = pi_state.PiState()
    ps.run()


if __name__ == "__main__":
    main()
