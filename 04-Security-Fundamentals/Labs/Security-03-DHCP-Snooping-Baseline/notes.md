# Notes

## Main controls used

- DHCP snooping was enabled
- DHCP snooping was configured for VLAN 10
- The legitimate DHCP server facing port was configured as trusted
- Client and rogue DHCP server facing ports remained untrusted
- Rate limiting (10) was applied on untrusted ports

## Main lesson

A switch can enforce which connected device is allowed to behave like infrastructure.

## Why this matters

Rogue DHCP behavior can disrupt client networking/activity or redirect traffic through incorrect gateway and DNS settings.

DHCP snooping helps stop that by configuring trust boundaries at the switch.