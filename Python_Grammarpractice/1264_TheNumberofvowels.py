while True :
    Sentence = input()

    if Sentence == "#" :
       break

    count = 0

    for char in Sentence.lower() :
        if char in "aeiou" :
           count += 1

    print(count)
