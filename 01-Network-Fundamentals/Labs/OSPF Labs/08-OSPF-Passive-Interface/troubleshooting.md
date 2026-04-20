## OSPF Behavior Testing

I performed additional testing to observe the impact of different passive interfaces.

Test 1:

LAN interfaces set passive.

Result:

Routing continued to function.

PC0 ping PC1 successful.

Reason:

OSPF still advertises connected networks even when LAN interfaces are passive.

Test 2:

Transit interface set passive.

Result:

Routing completely failed.

PC0 dropped ping; "desination unreachable".

Reason:

Routers could no longer form OSPF adjacency.

Without adjacency, routers cannot exchange any routing information.

## Key Learning Insight

Passive interfaces should only be used on LAN interfaces.

Transit interfaces must remain active for routing to function.

This demonstrated the importance of OSPF neighbor relationships for route exchange, and how misconfigurations can block traffic. 

# Troubleshooting Notes

## Issue Encountered

Routers formed OSPF adjacency but could not reach remote LAN networks. No passive interfaces were installed at this point.

## Root Cause

OSPF network statement did not match LAN interface IP.

OSPF only enables interfaces that match the network command.

## Diagnosis Process

Checked:

show ip ospf neighbor

Confirmed adjacency.

Checked:

show ip route

No OSPF routes present.

Checked:

show ip ospf interface

LAN interface missing.

## Fix

Corrected OSPF network statements.

Cleared OSPF process.

Routing tables updated.

## Key Lesson

OSPF network statements control interface participation.

Routing failures often occur due to incorrect interface matching.