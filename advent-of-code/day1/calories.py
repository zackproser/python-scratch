CALORIES_LEADER = 0

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
            if current_elf_calories > CALORIES_LEADER:
                CALORIES_LEADER = current_elf_calories
            # Reset the local calorie counter
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

print(f"Calories leader: {CALORIES_LEADER}")
