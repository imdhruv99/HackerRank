def reverse_words_order_and_swap_cases(sentence):

    word = []
    reversed_list = []
    word = sentence.split()
    reversed_list = word[::-1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence.swapcase()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()