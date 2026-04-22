# Lessons Learned

- Linux permissions are a direct access control mechanism
- `644`, `600`, and `700` each serve different purposes; allowing or disallowing access, viewing, or manipulation of file content depending on user.
- Execute permission should only be added when it is actually needed
- A script is still just a file until it has execute permission and is run correctly
- File permissions are one of the clearest practical examples of least privilege in Linux