# Notes

## Main controls used

- DHCP snooping was enabled
- DHCP snooping was configured for VLAN 10
- The DHCP-server facing port was marked as trusted
- The client facing port remained untrusted
- Dynamic ARP Inspection was enabled for VLAN 10
- The infrastructure facing port was marked as trusted for ARP inspection

## Main lesson

Dynamic ARP Inspection depends on trust boundaries and works naturally alongside DHCP snooping.

## Why this matters

ARP is a simple protocol, however lacks security as it does not verify whether ARP information is truthful. DAI reduces this risk by validating behavior against trusted information.

## Important platform note

Packet Tracer supported the main DAI baseline commands in this lab, but not every optional interface-level feature.