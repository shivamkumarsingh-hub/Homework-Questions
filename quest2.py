master_list = [101, 102, 103, 104, 105]

with open("attendance.txt") as file:
    present = [int(line.strip()) for line in file]

absent = [roll for roll in master_list if roll not in present]

print("Present students:", present)
print("Absent students:", absent)

with open("absent.txt", "w") as file:
    for roll in absent:
        file.write(f"{roll}\n")