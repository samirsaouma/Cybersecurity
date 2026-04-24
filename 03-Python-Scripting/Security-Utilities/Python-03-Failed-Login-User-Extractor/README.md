# Python-03 Failed Login User Extractor

## Objective

In this project, I built a Python script that reads a log file and extracts usernames from failed login events.

The goal was to practice moving from simple filtering toward easily understood and digestible information from security related log data.

## What I Built

I created:

- A sample log file containing mixed event types
- A Python script that scans the file line by line
- Logic that identifies failed login entries
- String splitting logic that extracts only the username information from each matching line
- A final summary showing all extracted usernames and the total count

## Why This Matters

Security log analysis often depends on isolating specific pieces of information.

This kind of parsing helps answer questions like:

- Which usernames are being targeted?
- Are the same accounts being attacked repeatedly?
- What information in the log is most relevant?

This project is simple, but it is a practical next step in log parsing.

## Files

- `sample_log.txt` — sample input log data
- `user_extractor.py` — Python script that extracts usernames from failed login entries
- `sample_output.txt` — expected script output
- `notes.md` — short notes on the parsing logic

## Verification

The script was run against the sample log file and correctly extracted the usernames from failed login entries.

Expected output is included in `sample_output.txt`.

## Main Takeaways

This project reinforced important ideas:

- Python can split strings into smaller useful pieces
- Logs often contain different information of events inside one line
- Extracting specific information is often more useful than printing the whole event
- Simple parsing logic can support basic security analysis

## Summary

This is my third Python security oriented scripting project.

It built on earlier projects by moving from full line filtering and IP counting to a focused username breakdown from failed login events.