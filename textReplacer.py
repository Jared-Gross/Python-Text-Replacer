def replaceText(txtFile, wordList):
    # This list contains all of the words you want to replace
    wordsToReplaceOld = []
    # This list contains all of the new words
    wordsToReplaceNew = []
    # This list contains the whole file you want to replace text with
    content = []
    # This is the file you want to edit
    file_to_edit = txtFile
    # We need the text that we want to replace and to replace with what
    with open(wordList) as f:
        '''
        We need to loop over all the lines, as each line has 2 words
        one being the word we want to replace and
        one being what it should be replaced with.
        '''
        for i in  f.readlines():
            '''
            We don't want empty lines of text.
            If a line is empty, we ignore it.
            '''
            if i != '\n':
                '''
                We split each line into a list using the "="
                as it's the seperator. This list contains 2 words.
                one being the word to replace
                the other being the new word
                '''
                wordList = i.split('=')
                # old word
                wordsToReplaceOld.append(wordList[0])
                # new word
                '''
                It's very imortant to replace '\n' because 
                if the word would be in the middle of a sentence, 
                it would make a new line after the word, which is a no no.
                '''
                wordsToReplaceNew.append(wordList[1].replace('\n',''))
    # Here we get all the lines of the text you want to replace.
    with open(file_to_edit, 'r') as f: content = f.readlines()
    # Here we actually replace the text.
    with open(file_to_edit, 'w+') as f:
        # we loop over all of the lines in the text you want to replace
        for line, word in enumerate(content):
            # we need to loop over every word that we want to replace
            for index, wordToReplace in enumerate(wordsToReplaceOld):
                '''
                If the word contains wordToReplace, 
                we simple take the whole line of text, 
                and replace that word with the new one.
                then we continue.
                Then the loop contiues to check if their are
                more words that are in the line
                '''
                if word.__contains__(wordToReplace): word = word.replace(wordToReplace,wordsToReplaceNew[index]); continue
                # if word doesn't contained wordToReplace, we simply continute the for loop.
                else: continue
            # write the newly modified word into the file!
            f.write(word)
# Calls the function that begins the text replace process 
if __name__ == '__main__': replaceText('textTest.txt', 'textToReplace.txt')
