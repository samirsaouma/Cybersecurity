# Python-04 Failed Login Summary Report

## Objective

In this project, I built a Python script that reads a log file and generates a simple summary report for failed login activity.

The goal was to combine earlier Python projects into one script that is more useful.

## What I Built

I created:

- A sample log file containing mixed events
- A Python script that identified the failed login entries
- Logic that counts the total number of failed logins
- Logic that extracts usernames and counts the repeated attempts per user
- Logic that extracts the source IP addresses
- A printed report that summarizes the findings

## Why This Matters

Security analysis depends on turning raw logs into something easily digestible and coherent.

This kind of reporting helps answer questions:

- How many failed login events occurred?
- Which usernames were targeted most frequently?
- Which source IP addresses appeared in the activity?

This project is still beginner level.

## Files

- `sample_log.txt` — sample input log data
- `summary_report.py` — Python script that builds the failed login summary
- `sample_output.txt` — output from the script
- `notes.md` — short notes on the script logic

## Verification

The script was run against the sample log file and generated the summary report showing total failed events, username counts, and source IP addresses.

Output is included in `sample_output.txt`.

## Main Takeaways

This project reinforced a few important ideas:

- Python can combine several simple parsing tasks into one report
- Dictionaries are useful for counting repeated usernames
- Lists are useful for storing repeated extracted values
- Structured output is more useful than raw event dumping
- Small scripts could produce meaningful summaries for security related data

## Summary

This is my fourth Python security oriented scripting project.

It combined filtering, extraction, counting, and reporting into a simple failed login summary utility.