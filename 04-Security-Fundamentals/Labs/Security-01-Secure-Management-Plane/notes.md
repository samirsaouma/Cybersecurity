# Notes

## Commands that mattered most

- `hostname` and `ip domain-name` were needed to generate RSA keys
- `crypto key generate rsa` created the key pair SSH depends on
- `username admin secret ...` created the local credentials
- `login local` made the VTY lines use the local user database
- `transport input ssh` blocked Telnet and allowed only SSH
- `access-class 10 in` restricted router management access

## Main lesson

SSH management is not one command. It is multiple configurations that all need to line up in order for SSH to function as intended.