_, max_val = map(int, input().split())
num = sorted(map(int, input().split()),reverse=True)

temp_val=0
offset1=0
best_combo=0
theo_max=False

for card1 in num:
    offset1+=1
    temp_val=card1
    offset2=offset1
    for card2 in num[offset1:]:
        offset2+=1
        temp_val = card1+card2
        for card3 in num[offset2:]:
            if ((temp_val+card3)==max_val):
                print(max_val)
                theo_max=True
                break
            if ((temp_val+card3) < max_val) and ((temp_val+card3) > best_combo):
                best_combo=temp_val+card3
        if theo_max:
            break
    if theo_max:
        break
if not theo_max:
    print(best_combo)
