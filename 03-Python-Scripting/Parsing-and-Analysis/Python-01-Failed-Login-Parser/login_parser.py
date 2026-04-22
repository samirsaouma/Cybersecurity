count = 0

with open("sample_log.txt", "r") as file:
    for line in file:
        if "Failed login" in line:
            print(line.strip())
            count += 1

print(f"\nTotal failed login attempts: {count}")

