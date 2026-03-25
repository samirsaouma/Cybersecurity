# Subnet Calculations

Initial network:

192.168.10.0/24

Requirement:

4 networks, one for each deparment in a small enterprise.


Hosts available:

2^6 = 64

Usable:

62

New mask:

/26

Subnet block size:

256 - 192 = 64

Subnet increments:

0
64
128
192

Resulting networks:

192.168.10.0
192.168.10.64
192.168.10.128
192.168.10.192
