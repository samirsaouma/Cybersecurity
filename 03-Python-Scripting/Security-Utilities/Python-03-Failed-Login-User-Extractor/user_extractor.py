failed_users = []

with open("sample_log.txt", "r") as file:
    for line in file:
        if "Failed login for user" in line:
            parts = line.strip().split("Failed login for user ")
            if len(parts) == 2:
                user_part = parts[1].split(" from ")[0]
                failed_users.append(user_part)

print("Failed Login User Summary:\n")

for user in failed_users:
    print(user)

print(f"\nTotal failed login usernames found: {len(failed_users)}")