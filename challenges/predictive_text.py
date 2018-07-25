
# Given a sample of words you've typed in the past, trainingText, and an initial word, firstWord, return an array of length howManyWords, representing the words you'd get by always selecting the top suggestion.

# How can you tell which word will be the top suggestion? It's the word that appears after the last one most frequently in trainingText. If there's more than one word that follows the current one most frequently, choose the one that follows it most early on in the text.

# If it was the last word of the text, or if it's an unfamiliar word, our predictive text algorithm should suggest the word that appears most frequently overall in the text. If there's no unique most frequent word, choose the one that appears earliest in the text.

# Example

# For trainingText = "some very repetitive text, very very repetitive text", firstWord = "very", and howManyWords = 10, the output should be predictiveText(trainingText, firstWord, howManyWords) = ["very", "repetitive", "text", "very", "repetitive", "text", "very", "repetitive", "text", "very"].
import string
def predictiveText(trainingText, firstWord, howManyWords):
    # Never Finished!!!
    word_count = dict()
    trainingText = [word.strip(string.punctuation) for word in trainingText.split()] 
    for word in trainingText:
        word_count[word] = word_count.get(word,0) + 1
    ordered_words = sorted(word_count.keys(),key = word_count.get)
    if word_count[ordered_words[-2]] == word_count[ordered_words[-1]]:
        i = trainingText.index(ordered_words[-1])
        j = trainingText.index(ordered_words[-2])
        if i > j:
            ordered_words[-1],ordered_words[-2] = ordered_words[-2],ordered_words[-1]

    result_text = list()
    result_text.append(firstWord)
   
    k = 1
    print(word_count)
    print(ordered_words)
    while len(result_text) < howManyWords:
        if firstWord not in ordered_words:
            result_text.append(ordered_words[-1])
        if word_count[ordered_words[1]] == word_count[ordered_words[-1]]:
            result_text.append(ordered_words[-1])
        else:
       
            result_text.append(ordered_words[k])
            if k ==  len(ordered_words) - 1:
                k = 1
            else:
                k += 1

    return result_text
# We'd like to construct a diverse array of numbers. At each step, we'll be given two choices for the next number we can add, and we'd like to select the number that appears least frequently in our array so far. If both numbers appear with equal frequency, we'll choose the smaller one.

# Our choices will be given in the form of an array, choices, consisting of 2-element arrays of integers.

# Example

# For choices = [[1, 2], [3, 4], [1, 2]], the output should be leastAppearance(choices) = [1, 3, 2].

# Initially, our array is empty, so given the choice between 1 and 2, we'll pick 1 since it's smaller.

# On the next step, our array looks like [1], which doesn't contain 3 or 4, so we'll pick 3 (again, because it's smaller than 4).

# On the final step, our array looks like [1, 3], so we'll pick 2 since the array already contains a 1.

# Input / Output

# [execution time limit] 4 seconds (py3)

# [input] array.array.integer choices

# An array containing sorted 2-element arrays of integers. Each 2-element array represents the two choices for the next number to add to our array of results.

# Guaranteed constraints
# 0 ≤ choices.length ≤ 105
# choices[i].length = 2
# choices[i][0] ≤ choices[i][1]
# 1 ≤ choices[i][j] ≤ 100

# [output] array.integer

# An array of numbers where each number appears as infrequently as possible up to the index at which it was selected.
def leastAppearance(choices):
   #
    numbers_count = dict()
    result_list = list()
    for pair in choices:
        if len(numbers_count) == 0:
            numbers_count[pair[0]] = 1
            result_list.append(pair[0])
        else:
            if pair[0] not in numbers_count.keys() and pair[1] not in numbers_count.keys():
                numbers_count[pair[0]] = 1
                result_list.append(pair[0])
            elif pair[0] in numbers_count.keys() and pair[1] not in numbers_count.keys():
                numbers_count[pair[1]] =  1
                result_list.append(pair[1])
            elif pair[1] in numbers_count.keys() and pair[0] not in numbers_count.keys():
               numbers_count[pair[0]] =  1
               result_list.append(pair[0])
            else:
                # both already in the dict
                if numbers_count[pair[0]] <= numbers_count[pair[1]]:
                    numbers_count[pair[0]] = numbers_count[pair[0]] + 1
                    result_list.append(pair[0])
                else:
                    numbers_count[pair[1]] = numbers_count[pair[1]] + 1
                    result_list.append(pair[1])
        
    
    return result_list

def main():
    # trainingText = "some very repetitive text, very very repetitive text"
    # trainingText = "only three words"
    # firstWord = "words"
    # howManyWords  = 7
    # print(predictiveText(trainingText, firstWord, howManyWords))
    choices = [[1, 2], [3, 4], [1, 2]]
    print(leastAppearance(choices))
if __name__ == '__main__':
    main()