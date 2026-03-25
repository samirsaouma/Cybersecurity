# Troubleshooting

## Issue Encountered

On first try, both PC's DHCP failed on subnet 1 and subnet 3.

## Diagnosis

Layer 1 verified via connectivity.

Layer 2 verified via switch communication.

Layer 3 verified via assigning static address and pinging from faulty PC. 

DHCP pool showed available addresses.

## Root Cause

Incorrect use of ip dhcp excluded-address command.

I excluded address ranges instead of single gateway addresses.

This removed usable hosts from the pools.

## Fix

Removed incorrect exclusions by using no ip dhcp excluded-address x... and added only gateway exclusions.

## Lesson

Configuration commands must be precise. Misunderstanding command behavior can invalidate entire services.
