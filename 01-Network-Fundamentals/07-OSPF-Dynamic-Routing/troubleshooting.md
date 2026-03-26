# Troubleshooting Notes

## Goal

Replace static routing with OSPF dynamic routing.

## Steps Taken

Removed static routes from all routers.

Enabled OSPF process using CLI.

Configured connected networks.

## Verification Steps

Checked neighbor formation:

show ip ospf neighbor

Checked routing tables:

show ip route

Verified connectivity using ping tests.

## Observations

Routing tables automatically populated with remote networks.

Routes displayed with "O" indicating OSPF.

## Key Takeaway

Dynamic routing simplifies network management greatly compared to static routing.

Routers automatically exchange network information instead of requiring manual configuration.
