# Python-02 Suspicious IP Counter

## Objective

In this project, I built a Python script that reads a log file, extracts source IP addresses from failed login events, and counts how many times each IP appears.

The goal was to move beyond simple filtering and begin turning raw log data into a more useful summary.

## What I Built

I created:

- A sample log file containing repeated failed login attempts from different IP addresses
- A Python script that scans the file line by line
- Logic that extracts the IP address from each failed login entry
- A dictionary based counter that tracks how often each IP appears
- A final printed summary of suspicious IP activity

## Why This Matters

This is useful because security work often involves more than just spotting one event.

It is also important to:
- Identify patterns
- Count repeated activity
- Reduce noisy raw logs into something more readable
- Highlight which sources appear most often

This project is simple, but it is a more realistic next step.

## Files

- `sample_log.txt` — sample input log data
- `ip_counter.py` — Python script that extracts and counts suspicious IPs
- `sample_output.txt` — expected output from the script
- `notes.md` — short notes on the script logic

## Verification

The script was run against the sample log file and correctly counted repeated failed login attempts by source IP.

Expected output is included in `sample_output.txt`.

## Main Takeaways

This project reinforced a few important ideas:

- Python can split strings into useful parts
- Dictionaries are useful for counting repeated values
- Simple scripting can turn raw logs into clearer summaries
- Even a beginner script can support basic security analysis

## Summary

This was my second Python security oriented scripting project.

It built on the first parser by moving from simple event filtering to basic activity summarization, which is a more useful step toward real log analysis.