with open('03.3_7th_.txt', 'r', encoding='utf-8') as file:
    src = file.read()
print(f"Длина строки: {len(src)}")
list_words = src.split(' ')
list_words2 = []
count = 0
for i in list_words:
    word = i.split('\n')
    list_words2.append(word)
for i in list_words2:
    count += len(i)
print(f"Слов: {count}")

content_without_points = src.replace('.', '!')
with open('03.3_7th_content2.txt', 'w', encoding='utf-8') as file:
    file.write(content_without_points)