# Design Decisions

## 1. Topology style

The network was designed as a small enterprise branch with:

- A router triangle for redundancy
- A switching core with two access switches
- Centralized internal server services
- Separate wireless and wired user groups
- One simulated internet edge

This design and structure was chosen because it is large enough to justify dynamic routing and segmentation; while still small enough to be explainable in a portfolio setting.

## 2. Routing model

OSPF was selected as the internal routing protocol because:

- The project includes multiple routers
- Alternate router paths exist
- It scales better than full static routing, for future expansion
- It was already the routing protocol I had used most heavily in labs

A static default route was added on R1-CORE toward R3-EDGE for internet exit due to Packet Tracer limitations with OSPF default advertisement.

## 3. Segmentation model

The network was segmented into:

- Guest wireless
- Staff wireless
- Management wired
- Servers
- Infrastructure

This kept the design realistic, without over-complicating the ACL's with excessive departmental VLANs such as HR or Finance.

The focus was maintained on designing clear policy enforcement rather than expanding VLAN count.


## 4. Wireless model

A two AP model was implemented:

- One AP for guests
- One AP for staff

This choice was driven by Packet Tracer limitations while also keeping the project cleaner.

Guest wireless was left open.
Staff wireless was protected with WPA2-PSK.

## 5. Core and access roles

SW1-CORE was used as the aggregation point for:

- Router uplink
- Servers
- Trunk links to access switches

SW2-ACCESS served wireless infrastructure.

SW3-ACCESS served wired management clients.

This gave the topology a more realistic enterprise layout.

## 6. Security model

Security was enforced in two layers:

### Layer 2
- PortFast on edge ports
- BPDU Guard on edge ports

### Layer 3
- ACL-based segmentation

Policies were intentionally simple and realistic:

- Guest isolated from internal networks
- Staff allowed to reach application resources but blocked from management
- Management fully trusted internally

## 7. Addressing model

The internal address space 172.20.0.0/24 was subnetted using VLSM to reflect deliberate sizing.

This decision is important because it shows realistic subnet planning.

## 8. Service centralization

DHCP-SRV and APP-SRV were placed in the server VLAN and connected to the core switch.

This reflects the design principle that shared services should be centrally placed, rather than attached to edge switches.


## 9. Edge internet model

The internet side is simulated by a single external server above R3-EDGE.

This is not a true ISP path, but was implemented to demonstrate:

- Edge boundary definition
- NAT/PAT logic
- Inside/outside interface roles
- Client access to external destinations


## 10. What makes this my first flagship

This project combines:

- Switching
- Routing
- Wireless
- Services
- Segmentation
- Security
- Verification

Into a single coherent design.

This integration makes it a flagship project rather than just a larger configuration exercise.