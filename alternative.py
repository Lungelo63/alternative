sentence = input("Enter a sentence to be alternated: ")                #Taking in the user input
new_sentence = ""                                                      #Creating an empty string for the loop
for word_index in range(len(sentence)):                                #initiating for loop 'word index' modulus 2. If remainder = 2...
    if word_index % 2 == 0:
        new_sentence = new_sentence + sentence[word_index].upper()     #change the even index letters to uppercase
    else:
        new_sentence = new_sentence + sentence[word_index].lower()     #Else change it to lowercase then print out
print(new_sentence)
