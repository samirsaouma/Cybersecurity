# Notes

## Main controls used

- VLAN 999 was used as a blackhole VLAN for unused ports
- Unused ports were shut down to reduce attack surface
- Port security was enabled on active access ports
- Sticky MAC learning was used so the switch could learn and bind the connected device
- PortFast was enabled on host-facing ports
- BPDU Guard was enabled to protect edge ports from unexpected switch behavior

## Main lesson

A switch can be made noticeably more secure with a few simple hardening decisions.

## Important distinction

These protections belong on end-host interfaces, not on switch uplinks or trunk links.