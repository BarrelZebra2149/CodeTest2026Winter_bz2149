total = int(input())
value_collection = []

for i in range(total):
    value_collection.append("".join(input().split()))

for sorted_sentence in value_collection:
    count=dict()
    most_common_letters=[]
    previous_largest_count=0
    for letter in sorted_sentence:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    if (len(count)>1) and (count[0][1] == count[1][1]):
        print("?")
    else:
        print(count[0][0])