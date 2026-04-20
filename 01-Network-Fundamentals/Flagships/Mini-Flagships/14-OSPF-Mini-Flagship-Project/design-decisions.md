# Design Decisions

## Why structured /30 transit addressing was used

Transit links were named using router to pair notation (for example 10.0.12.0/30, link between router1 and router2 = 12) to make topology relationships immediately visible from the IP plan.

## Why Areas 10 and 20 were chosen

Separate non backbone areas were used to demonstrate ABR behavior and route summarization.

## Why LAN networks were chosen as consecutive /24 blocks

Consecutive blocks allow clean summarization:
- 192.168.10.0/24 + 192.168.11.0/24 -> 192.168.10.0/23
- 192.168.20.0/24 + 192.168.21.0/24 -> 192.168.20.0/23

## Why passive interfaces were used

LAN segments do not contain routers and therefore do not need OSPF hello traffic. Passive interfaces reduce unnecessary protocol behavior and improves security.

## Why floating static routes were added

Floating static routes were used to demonstrate controlled backup routing if OSPF paths were to fail.