## Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    
    infile = open(filename, 'r')

    # read file
    story = infile.read()

    # close file
    infile.close()

    # print story
    # print(story)
    return story

# function “count_words”. It uses “read_file_content” to read the text contained in “story.txt”. It should return a dictionary whose keys are unique words, and their values the count of those words in the text e.g {“as”:10, “would”:5}.
def count_words():
    # read file
    story = read_file_content("story.txt")

    # split story into words
    words = story.split()

    # create dictionary
    word_count = {}

    # count words
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # print word_count
    print(word_count)
    return word_count


    
# #split the text into DICTIONary of words with their occurence
    

#     return {"as": 10, "would": 20}

#  print content of story.txt file

read_file_content('story.txt')
count_words()