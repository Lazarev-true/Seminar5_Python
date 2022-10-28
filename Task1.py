# Напишите программу, удаляющую из текста все слова, содержащие "абв"

f = open('Task1.txt', 'r', encoding = 'utf-8')

text = f.read()
s = text

f.close()

if text.find('.') != -1:
    text = text.replace('!', ' !')
if text.find('?') != -1:
    text = text.replace('?', ' ?')

def del_words(text):
    myText = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(myText)

myText = del_words(text)

my_text = myText.replace(' .', '.')
myText = myText.replace(' ?', '?')

print()
print(s)
print()
print(myText)
        
