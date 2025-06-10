results = []

while True :
    Sentence = input()

    if Sentence == "#" :
       break

    count = 0

    for char in Sentence.lower() :
        if char in "aeiou" :
           count += 1

    results.append(count)

for r in results :
    print(r)
