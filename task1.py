def check_rhythm(poem):
    lines = poem.split()
    syllables = []
    
    for line in lines:
        words = line.split('-')
        count = 0
        for word in words:
            count += sum(1 for char in word if char.lower() in 'aeiou')
        syllables.append(count)
    
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"
    
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
