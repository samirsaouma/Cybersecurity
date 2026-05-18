# Python-06 Failed Login Threshold Alert

## Objective

For this Python project I created a script that reads failed login events from a log file, then the script counts each failed attempt by source IP address, and generates an alert when an IP reaches the defined threshold.

This moves the Python projects from basic reporting into simple detection.

## What I Built

I created:

- A sample log file containing failed login events from multiple IP addresses
- A Python script that scans the file line by line
- Logic that extracts the source IP addresses from each failed login attempt
- A dictionary counter that tracks failed attempts per IP
- A threshold that identifies IPs with repeated failed login activity
- A simple alert report

## Why This Matters

Security monitoring requires deciding which events deserve attention.

A threshold based script helps answer questions like:

- Which IP addresses are failing repeatedly?
- Which sources may require investigation?
- When does normal network activity/noise become suspicious?
- How can repeated activity be turned into a basic alert?

This project introduces a core idea used in detection and monitoring: repeated behavior can become more important than a single event.

## Files

- `sample_log.txt` — Sample log data
- `threshold_alert.py` — Python script
- `sample_output.txt` — Output from the script
- `notes.md` — Short notes

## Verification

The script was run against the sample log file and correctly identified the IP addresses that reached or exceeded the configured threshold.

Output is included in `sample_output.txt`.

## Main Takeaways

This project reinforced important concepts:

- Dictionaries are useful for tracking repeated activity
- Threshold logic is beneficial for generating basic alerts
- Detection depends on repeated patterns, not an isolated event
- Alerting should be based on clear criteria