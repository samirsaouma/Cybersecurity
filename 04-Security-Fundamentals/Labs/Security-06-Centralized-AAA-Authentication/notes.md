# Notes

## Main controls used

- AAA was enabled with `aaa new-model` on router
- RADIUS was configured as the primary login authentication method
- Local authentication was configured as a fallback
- AAA server was configured with the router as a RADIUS client
- A shared RADIUS secret was configured on both sides
- An administrative user was created on the AAA server
- VTY lines were configured for AAA authentication
- SSH was used for remote management access

## Main lesson

Centralized authentication creates a central platform for identity management, improving scalability from authenticating individual network devices.

The router is able to forward login authentication to a dedicated AAA server.

## Authentication flow

1. Admin PC attempts to initiate an SSH session to the router.
2. Router receives the login attempt.
3. Router sends a RADIUS access request to the AAA server.
4. AAA server checks the username and password.
5. AAA server sends an access accept response.
6. Router allows the SSH session.