#Bilal Sayed 10/20/17
def main():
    #open file
    txtfile = open('text.txt', 'r')
    #readfile
    file_contents = txtfile.read()
    #create a string for the word counter by replacing the \n characters with spaces
    file_contents_stripped = file_contents.replace('\n', ' ')
    #create a string for the sentence counter string by stripping the extra \n at the end of the original string
    file_contents_for_sentences = file_contents.rstrip()
    #split the sentence counter string into sentences using the split method and using the .\n to split it into sentences
    file_contents_split = file_contents_for_sentences.split('.\n')
    #calls the function that counts the sentences
    sentences = sentence_counter(file_contents_split)
    #calls teh function that counts the words
    words = word_counter(file_contents_stripped, ' ')
    #calls teh funtion that calculates teh average
    result = avg(sentences, words)
    #calls the fucntion that displays the result
    display(sentences, words, result)
    #closes teh file
    txtfile.close()

#calculates the sentences by counting the number of strings in 'a'
def sentence_counter(a):
    sentences = 0
    for ch in a:
            sentences += 1
    return sentences
#calculats words by searching for the spaces after them.
def word_counter(a,b):
    words = 0
    for ch in a:
        if ch == b:
            words += 1
    return words
#calculates the average           
def avg(a,b):
    result = 0
    result = b / a
    return result
#displays the result
def display(a, b, c):
    print('The total number of sentences is', a, 'sentences.')
    print('The total number of words is', b, 'words.')
    print('The average number of words per sentences is', c, 'words per sentence')
main()
