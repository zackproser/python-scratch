CALORIES_LEADERBOARD = []
top_three_cal_counts = []
# 1. Open the input file for reading
# 2. Iterate through each line
# 3. For each line, add the current value to the local calorie counter
# 4. When a newline is encountered, that means we're inspecting the inventory of a new elf, so
# do a comparison and check if the current elf's calories is greater than the leader value
# If it is, that elf's calorie count becomes the new leader. Otherwise, continue on to inspect
# the next elf's inventory
with open("input.txt", "r") as f:
    lines = f.readlines()

    current_elf_calories = 0

    for line in lines:
        if line == "\n":
            # We're at the end of the input for our current elf, so add their tally to the leaderboard
            CALORIES_LEADERBOARD.append(current_elf_calories)
            # Reset the local calorie counter
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

# Sort the leaderboard from highest to lowest
CALORIES_LEADERBOARD.sort(reverse=True)
if len(CALORIES_LEADERBOARD) > 3:
    top_three_cal_counts = CALORIES_LEADERBOARD[:3]

final_total = sum(top_three_cal_counts)

print(f"Top three calorie counts: {final_total}")
