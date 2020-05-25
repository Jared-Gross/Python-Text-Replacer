# the tutorial was on hut but it van
wordsToReplaceOld = []
wordsToReplaceNew = []
content = []
file_to_edit = 'textTest.txt'
with open('textToReplace.txt') as f:
    for i in  f.readlines():
        if i != '\n':
            wordList = i.split('=')
            wordsToReplaceOld.append(wordList[0])
            wordsToReplaceNew.append(wordList[1].replace('\n',''))
with open(file_to_edit, 'r') as f: content = f.readlines()
with open(file_to_edit, 'w+') as f:
    for line, word in enumerate(content):
        for index, wordToReplace in enumerate(wordsToReplaceOld):
            if word.__contains__(wordToReplace):   word = word.replace(wordToReplace,wordsToReplaceNew[index]); continue
            else: continue
        f.write(word)
