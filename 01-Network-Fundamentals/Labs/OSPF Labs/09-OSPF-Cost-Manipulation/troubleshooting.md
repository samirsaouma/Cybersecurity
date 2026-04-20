## Troubleshooting Observation

During testing, the LAN networks did not appear in the routing table.

Initial checks confirmed:

OSPF configuration correct
Network statements correct  
- confirmed using show run | section router ospf

OSPF neighbors formed
- confirmed using show ip ospf neighbor  

After further inspection, I discovered that the LAN interfaces were not fully validated as part of the topology design.

After LAN connectivity was verified and endpoints deployed, OSPF properly advertised the connected networks.

## Lesson Learned

Always verify:

Interface participation
Correct topology connections
OSPF interface matching

## Design Verification Lesson

This lab reinforced the importance of validating physical and logical topology before troubleshooting routing protocols.

This issue demonstrated that routing troubleshooting should begin with infrastructure validation rather than assuming protocol failure.

Key takeaway:

Always verify Layer 1, Layer 2, and Layer 3 before diagnosing routing behavior.