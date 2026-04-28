# Notes

## Main controls used

- Local privileged administrative account was created
- Passwords encrypted
- SSH version 2 configured for remote access
- VTY lines restricted to SSH only
- `login local` applied to management lines
- Warning banner configured
- Login block policy enabled for repeated failed login attempts
- VTY session timeout applied with `exec-timeout 5 0`

## Main lesson

Administrative access should be treated as a protected security surface, not just a convenience feature.

## Why this matters

If login protections are not secured, attackers can repeatedly attempt access and use attack techniques such as dictionary attacks or brute force attacks. It's also important to limit long-lived sessions. Even simple hardening steps such as; lockout configurations, timeouts, banners, and SSH only access improves the security posture significantly.

## Important platform note

Packet Tracer does not support `login delay 3`. Only the accepted and verifiable controls were documented.