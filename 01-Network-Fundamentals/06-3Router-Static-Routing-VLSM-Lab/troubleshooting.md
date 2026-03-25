# Troubleshooting Notes

## Issue Encountered

First inital packet loss occurred when attempting end to end connectivity between LAN networks.

## Symptoms

- End routers could not reach the remote LAN networks
- ICMP packets dropped
- Routing tables incomplete

## Diagnostic Steps

Step 1:
Verified interface status:

show ip interface brief

All interfaces were up.

Step 2:
Verified routing tables:

show ip route

Discovered missing static routes.

Step 3:
Tested router connectivity:

Ping tests performed between routers to isolate the problem.

Step 4:
Verified next hop addresses.

Incorrect next hop routes caused traffic to drop.

## Root Cause

Missing or incorrect static routes prevents routers from knowing remote networks, or returning the packet.

## Resolution

Added correct static routes pointing to proper next hop router interfaces.

## Verification

After corrections:

- Router routing tables updated correctly
- All LAN networks reachable
- ICMP successful

## Key Troubleshooting Takeaways

Verify in order:

Physical connectivity  
Interface status  
Routing tables  
Hop by hop connectivity  

Troubleshoot by layers.
