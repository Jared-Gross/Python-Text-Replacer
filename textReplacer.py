# the tutorial was on hut but it van
wordsToReplaceOld = []
wordsToReplaceNew = []
content = []
with open('textToReplace.txt') as f:
    content = f.readlines()
    for i in content:
        if i != '\n':
            wordList = i.split('=')
            wordsToReplaceOld.append(wordList[0])
            wordsToReplaceNew.append(wordList[1].replace('\n',''))
with open('textTest.txt', 'r') as f: content = f.readlines()
with open('textTest.txt', 'w+') as f:
    for line, word in enumerate(content):
        for index, wordToReplace in enumerate(wordsToReplaceOld):
            if word.__contains__(wordToReplace):   word = word.replace(wordToReplace,wordsToReplaceNew[index]); continue
            else: continue
        f.write(word)