# Python-05 Suspicious Username Counter

## Objective

For this project I created a Python script that prints a summary of failed login attempts, with a ranking of username appearance count. 

The goal is to move towards simple prioritization by frequency.

## What I Built

I created:

- A sample log file containing repeated failed login attempts against several usernames
- A Python script that scans the file line by line
- Logic that extracts usernames from failed login entries
- A dictionary based counter that tracks how often each username appears
- Sorting logic that places the most frequently targeted usernames first
- A final printed summary report

## Why This Matters

Security log analysis depend on prioritization. Prioritization helps understand the most critical ongoing issues.

This helps answer questions like:

- Which usernames are being targeted most often?
- Which accounts should be reviewed first?
- Is the activity concentrated on a few common accounts?

This project is still simple but introduces the idea of ranking suspicious activity.

## Files

- `sample_log.txt` — Sample input log data
- `username_counter.py` — Python script that counts and ranks targeted usernames
- `sample_output.txt` — Output from the script
- `notes.md` — Notes on the parsing and sorting logic

## Verification

The script was run against the sample log file and produced the sorted summary of targeted usernames based on failed login frequency.

Output is included in `sample_output.txt`.

## Main Takeaways

This project reinforced a few important ideas:

- Dictionaries are useful for counting repeated values
- Usernames can be extracted from structured log strings using simple splitting
- Sorting makes the output more useful and interpretable
- A small script can support basic prioritization

## Summary

This was my fifth Python scripting project.

It builds onto earlier projects by adding simple ranked reporting of log data.