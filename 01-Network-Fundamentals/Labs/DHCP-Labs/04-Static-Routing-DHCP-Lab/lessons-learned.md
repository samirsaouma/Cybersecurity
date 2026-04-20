# Lessons Learned

## Building networks one step at a time is important

I attempted to configure multiple networks at once which made troubleshooting difficult when I ran into difficulties. In my rebuild I learn to verify at each step.

## Physical connections must exist before routing works

I attempted to configured static routes before connecting the routers physically, causing routing failures because the routers must be physically connected before routes can function.

## ARP can cause unexpected connectivity issues

During earlier troubleshooting I was unable to ping router from a faulty PC, even with a static IP Address. After checking layer 1 was configured correctly, as well as gateway, I cleared ARP table. This fixed connectivity issues even when configurations appeared correct. I used the command arp -d. 

## DHCP troubleshooting requires isolating variables

When DHCP failed previously I learned to verify:

- Interface status  
- Subnet matching  
- Pool configuration  
- Available addresses  
- PC DHCP state

Commands I used for this:
- show ip interface brief
- show ip dhcp pool

## Troubleshooting approach learned

I learned to troubleshoot in layers:

Layer 1:
Check cables

Layer 2:
Check switch connectivity

Layer 3:
Check IP addressing

Routing:
Check routing tables


## Skills improved

Basic router configuration  
DHCP setup  
Static routing  
Subnet design  
Packet flow analysis  
Structured troubleshooting
Troubleshooting commands
