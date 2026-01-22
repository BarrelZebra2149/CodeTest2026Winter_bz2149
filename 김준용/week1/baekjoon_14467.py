total_count = int(input())
total_cow_movement=0
cow_position_pairs=dict()

for i in range(total_count):
    cow, position = map(int, input().split())
    if str(cow) in cow_position_pairs:
        cow_position_pairs[str(cow)].append(position)
    else:
        cow_position_pairs[str(cow)]=[position]
 
for cow_designation, positions in cow_position_pairs.items():
    previous_value=positions[0]
    for value in positions:
        if value != previous_value:
            total_cow_movement+=1
        previous_value=value

print(total_cow_movement)