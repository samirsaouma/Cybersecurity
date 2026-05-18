alert_threshold = 3
ip_counts = {}

with open("sample_log.txt", "r") as file:
    for line in file:
        if "Failed login for user" in line:
            ip_address = line.strip().split(" from ")[1]

            if ip_address in ip_counts:
                ip_counts[ip_address] += 1
            else:
                ip_counts[ip_address] = 1

print("Failed Login Threshold Alert Report")
print("-----------------------------------")
print(f"Alert threshold: {alert_threshold} failed login attempts\n")

for ip, count in ip_counts.items():
    if count >= alert_threshold:
        print(f"ALERT: {ip} reached {count} failed login attempts")
    else:
        print(f"OK: {ip} had {count} failed login attempt(s)")