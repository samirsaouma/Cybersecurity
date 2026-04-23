ip_counts = {}

with open("sample_log.txt", "r") as file:
    for line in file:
        if "Failed login" in line:
            parts = line.strip().split(" from ")
            if len(parts) == 2:
                ip = parts[1]
                if ip in ip_counts:
                    ip_counts[ip] += 1
                else:
                    ip_counts[ip] = 1

print("Suspicious IP Summary:\n")

for ip, count in ip_counts.items():
    print(f"{ip}: {count} failed login attempt(s)")