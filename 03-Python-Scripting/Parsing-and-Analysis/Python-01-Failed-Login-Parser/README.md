# Python-01 Failed Login Parser

## Objective

For my initial Python project, I built a simple Python script that reads a log file and extracts failed login events.

The goal was to practice basic file handling, conditional logic, and security-relevant scripting due to my current Sec+ studies.

## What I Built

I created:

- A sample log file with mixed event types
- A Python script that scans the file line by line
- Logic that filters only lines containing failed login activity
- A final counter showing how many failed login attempts were found

## Why This Matters

Log parsing is a practical security task.

Even in a very simple form, it helps show how Python can be used to:

- Search through event data
- Filter relevant entries
- Reduce noise
- Highlight suspicious activity

This is a beginner project, but it connects directly to security operations and investigation workflows.

## Files

- `sample_log.txt` — sample input log data
- `login_parser.py` — Python parser script
- `sample_output.txt` — output produced by the script
- `notes.md` — short notes on what the script is doing

## Verification

The script was run against the sample log file and correctly extracted all failed login entries.

Expected output is included in `sample_output.txt`.

## Main Takeaways

This project reinforced a few basic but important ideas:

- Python can read files line by line very simply
- `if` conditions are enough to build a useful first filter
- Even a small script can support a security use case
- Scripting is simpler when the goal is clear and narrow

## Summary

This was my first Python security-oriented scripting project.

It was kept simple, but shows how Python can be used to process log data and extract failed login events in a clear and repeatable way.