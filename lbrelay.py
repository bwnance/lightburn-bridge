# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.10.3 (main, Jul 25 2022, 17:09:16) [Clang 13.0.0 (clang-1300.0.27.3)]
# Embedded file name: /boot/LBBridge/lbrelay.py
# Compiled at: 2021-09-13 10:26:38
# Size of source mod 2**32: 1138 bytes
from LBBridge import log

log.init_logger("lbrelay")
from LBBridge import config
from LBBridge import network
from LBBridge import relay
from LBBridge.proc_status import RelayStatus, RelayDetails


def main():
    cfg = config.Config()
    nm = network.NM()
    rs = RelayStatus()
    rd = RelayDetails()
    log.info(cfg.to_dict())
    if cfg.device_type not in relay.RELAYS:
        cfg.device_type = "ruida"
    relay_cls = relay.RELAYS[cfg.device_type]
    relay_obj = relay_cls(cfg, rs)
    rs.info("Setting up ethernet...")
    rd.info("No relay loaded")
    if relay_obj.type == relay.RelayType.Ethernet:
        if not nm.EthConfigDirect(cfg.laser_ip, True):
            rs.error("Failure configuring direct ethernet")
            return
    else:
        nm.EthKillDirect()
    rs.info(f"Starting {cfg.device_type} relay")
    rd_msg = f"{cfg.device_type} {relay_obj.version[0]}.{relay_obj.version[1]}"
    rd.ok(rd_msg)
    relay_obj.run()
    rs.warn("Relay service closing...")


if __name__ == "__main__":
    main()
