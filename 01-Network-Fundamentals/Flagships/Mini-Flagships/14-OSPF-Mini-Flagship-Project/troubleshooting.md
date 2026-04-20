# Troubleshooting Notes

## Issue 1 — OSPF formed neighbors but routes did not appear

Root cause:
OSPF network statement did not match the intended interface range.

Fix:
Corrected network statements and validated interface participation again.

## Issue 2 — Summary route remained while an internal subnet failed

Observation:
ABR continued advertising the summary because at least one component subnet still existed.

Lesson:
Summarization improves scale but can hide internal failures.

## Issue 3 — Cost change did not immediately change route

Fix:
Verified route table again after OSPF recalculated. In some test cases clearing the OSPF process was necessary.

## Issue 4 — Floating static route did not appear active

Root cause:
OSPF route still had lower administrative distance and remained preferred.

Fix:
Shutdown preferred OSPF path to force floating static activation.