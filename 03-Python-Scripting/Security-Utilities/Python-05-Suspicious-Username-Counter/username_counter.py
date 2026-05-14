user_counts = {}

with open("sample_log.txt", "r") as file:
    for line in file:
        if "Failed login for user" in line:
            user_part = line.strip().split("Failed login for user ")[1]
            username = user_part.split(" from ")[0]

            if username in user_counts:
                user_counts[username] += 1
            else:
                user_counts[username] = 1

sorted_users = sorted(user_counts.items(), key=lambda item: item[1], reverse=True)

print("Suspicious Username Summary")
print("--------------------------------------------------")

for user, count in sorted_users:
    print(f"{user}: {count} failed login attempt(s)")

print(f"\nTotal unique usernames targeted: {len(user_counts)}")