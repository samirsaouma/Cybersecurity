## Troubleshooting Process & Resolution
# Initial Problem

All end devices across multiple different VLANs were unable to ping their default gateway. When testing from the router, the router itself was unable to ping hosts on directly connected networks. Packet simulation showed that packets were not progressing past the router, or from the end hosts, and ARP resolution was failing.

# Observed Symptoms
1) PCs could not reach default gateway
2) Router could not reach hosts 
3) Simulation mode showed packets stopping before Layer 2 forwarding
4) No ARP table entries created for affected hosts
5) Tested ACL removal, did not resolve the issue
6) Trunk links appeared operational

# Troubleshooting Methodology

The following troubleshooting approach was used following observed symptoms:

**Step 1 – Verify trunk infrastructure (First Prediction)**

1) Checked trunk allowed VLAN lists - Confirmed
2) Verified trunk operational state - Confirmed
3) Verified VLAN configuration across all switches - Confirmed

Result: Trunk configurations functioning correctly.

**Step 2 – Verify Layer 3 configuration**

1) Verified router subinterfaces - Confirmed
2) Verified IP addressing and default gateways - Confirmed
3) Verified encapsulation dot1Q configuration - Confirmed

Result: No routing issues identified.


**Step 3 – Investigate Layer 2 forwarding failure**

Checks performed:

1) VLAN database verification - Confirmed
2) Interface configuration verification - Issue.
3) Root Cause Identified

Although VLANs existed on the switches, the end host facing interfaces were not assigned to the VLANs. 

**Resolution Applied**

Access ports were properly the missing configuration:

interface Fa0/x
 switchport access vlan x


# Key Lessons Learned

**Technical lessons:**

VLAN creation alone does not place interfaces into the VLAN.
IP Addressing does not place end hosts into a VLAN


**Operational lessons:**

1) Always verify VLAN membership & Interface configuration to VLAN using show vlan brief.
2) Packet simulation is valuable for identifying where communication fails.
3) Troubleshooting Skills Practiced
4) Fault Isolation
5) ARP behavior analysis
6) VLAN membership verification