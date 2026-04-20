## Troubleshooting Notes – Inter-VLAN ACL Enforcement
# Issue encountered

ACL rules were configured to block VLAN 10 from accessing other VLANs, but initial ping were successful, showing the ACL was not functioning.

**Root causes identified**
1. ACL rule order mistake

The ACL contained a <permit ip any any> statement placed before several deny rules:

access-list 100 permit ip any any
access-list 100 deny ip 192.168.20.0 ...

ACL lists operate from top to down, with first match logic. Any traffic reaching the permit statement was allowed and therefore the subsequent deny rules were ignored.

**Resolution:**
Rebuilt ACL ensuring all deny statements appear before the final permit rule.

1. Testing methodology confusion

Initial validation attempts were uncertainty due to inconsistent testing results. ACL counters showed matches, confirming filtering was occurring.

**Verification method used:**

show access-lists

This confirmed that the deny rules were matching traffic.

Counters were reset for clean testing:

clear access-list counters

Traffic was then retested from VLAN host machines.

3. ACL placement considerations

ACLs were correctly applied inbound on router subinterfaces:

ip access-group 100 in

This ensured traffic entering from the source VLAN was filtered before routing decisions.

# Final resolution

ACL had to be rebuilt with proper structure:

deny rules first
permit ip any any last

Traffic testing from VLAN hosts confirmed correct segmentation behavior.

# Key lessons learned
- ACL processing is top-down, first match wins
- permit ip any any must always be last
- ACLs filter transit traffic, not router-generated traffic
- show access-lists counters are critical for validation
- Proper testing should always originate from endpoint devices