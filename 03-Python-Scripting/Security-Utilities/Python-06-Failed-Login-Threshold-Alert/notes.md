# Notes

## What the script does

- Opens the sample log file
- Reads the file line by line
- Identifies failed login events
- Extracts the source IP address
- Counts failed logins per IP address
- Compares each count against the alert threshold
- Prints an alert when an IP reaches or exceeds the threshold

## New idea in this project

This project introduces threshold based alerting. Security monitoring often depends on thresholds, and alerts to better pinpoint potential security concerns.

Repeated failed logins from the same IP address can indicate brute force, password guessing, or other security vulnerabilities.