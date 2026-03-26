# OSPF Dynamic Routing Lab

## Objective

To convert the previously working static routing network lab, into a dynamic routing lab using OSPF.

Manual routing entires were removed to allow routers to automatically learn remote networks.

## Technologies Used

- OSPF 
- Cisco IOS CLI
- Dynamic routing protocols
- Network verification commands
- Routing table analysis

## Network Design

The topology consists of three routers, the same as the previous lab, connected using /30 transit networks and four LAN networks using VLSM subnetting.

Previously static routes were used. The static routes were removed and replaced with OSPF.

## Topology & Simulation 

![Topology](images/07topology.png)

## OSPF Configuration Overview

OSPF was enabled on all routers using process ID 1.

All networks were placed in area 0.

Routers advertised:

- Transit networks  
- LAN networks  

Routers then formed the neighbor relationships and exchanged routing information automatically.

## OSPF Neighbor & Routing Table Verification

![OSPF Neighbors](images/07tables.png)


Routes marked with "O" indicate that the routes were learned dynamically through OSPF.

## Key Differences from Static Routing

Static routing required manual route entry.

OSPF automatically distributes routing information.

This reduces manual configuration labor; especially at scale. Also reduces complexity, and improves scalability of networks.

## Troubleshooting Process

Steps performed:

- Removed static routes
- Verified interface connectivity
- Enabled OSPF on all routers
- Verified neighbor relationships
- Verified routing tables
- Tested end to end connectivity using ping.

## Lessons Learned

- Dynamic routing removes the need for manual route management.
- OSPF uses neighbor relationships to exchange routing information.
- Must understand wildcard masks, as they must match the subnet mask correctly.
- OSPF requires interfaces to be in the same area to form adjacency.
- Routing tables update automatically when OSPF is configured correctly.
- Dynamic routing protocols scale better than static routing.
- Network design remains important even when routing is automated.

## Skills Practiced

- Dynamic routing configuration
- OSPF fundamentals
- Routing protocol verification
- Network protocol comparison
- Infrastructure troubleshooting
