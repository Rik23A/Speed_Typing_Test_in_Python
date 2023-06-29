from time import time

print('press enter to start typing or break a new line')
print('press enter twice to finish typing')
print('please enter text for typing test')
input('---------text input----------')

# record time stamp when user starts typing
start = time()
text = []
while True:
    line = input()
    if not line:
        break
    text.append(line)

# record time stamp when user finish typing
end = time()



print('---------------- checking of typing speed on comment -----------------')

elapsed_time = (end-start)/60
chars_count = sum(len(item) for item in text)
words_count = chars_count / 5

wpm = round(words_count/elapsed_time)

print(f'your average words per minute (WPM) is {wpm}')
if wpm < 30:
    print('you have to learn proper technique of typing...')
elif wpm < 40:
    print('you are below average do more practicing...')
elif wpm < 50:
    print('you are an average typist...')
elif wpm < 60:
    print('you are above average typist...')
else:
    print('Great!! you are a professional typist...')