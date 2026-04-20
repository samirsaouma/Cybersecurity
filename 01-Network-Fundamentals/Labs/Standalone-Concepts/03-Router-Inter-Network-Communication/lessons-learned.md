## Technical Lessons

- Learned how routers connect separate networks.

- Learned that devices must send traffic to the default gateway for remote communication.

- Observed ARP resolution occurring before ICMP communication. (Reason for first ping failure)

- Observed MAC address resolution behavior in routing scenarios.

Observed Sequence:  
1. PC checks if destination is in local subnet
2. PC determines destination is remote
3. PC sends ARP request for router MAC address
4. Router responds with MAC address
5. ICMP traffic begins after MAC resolution

## Troubleshooting Lessons

- Removing default gateway prevents remote communication. Pings time out.

- Learnt booting routers may require ROMMON recovery.

- Testing failures helps confirm understanding.

## Security Lessons

- Routers control traffic between networks.

- Network segmentation can reduce attacker movement.

- Understanding packet flow helps understand network attacks.

