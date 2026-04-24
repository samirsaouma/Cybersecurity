failed_count = 0
user_counts = {}
ip_list = []

with open("sample_log.txt", "r") as file:
    for line in file:
        if "Failed login for user" in line:
            failed_count += 1

            user_part = line.strip().split("Failed login for user ")[1]
            username = user_part.split(" from ")[0]
            ip_address = user_part.split(" from ")[1]

            if username in user_counts:
                user_counts[username] += 1
            else:
                user_counts[username] = 1

            ip_list.append(ip_address)

print("Failed Login Summary Report")
print("---------------------------")
print(f"Total failed login events: {failed_count}\n")

print("User counts:")
for user, count in user_counts.items():
    print(f"- {user}: {count}")

print("\nSource IP addresses:")
for ip in ip_list:
    print(f"- {ip}")