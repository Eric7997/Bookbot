def main():
    print_report()

def get_book_text():
    import sys
    with open(sys.argv[1]) as contents:
        return contents.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_letters(words):
    letter_list = []
    for word in words:
        for letter in word:
            if letter.isalpha():    
                letter_list.append(letter)
    return letter_list

def count_letters(letter_list):
    letter_count = {}
    for letter in letter_list:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] +=1
        else:
            letter_count[letter.lower()] =1
    return dict(sorted(letter_count.items(), key = lambda item: item[1],reverse = True))

def print_report():
    text = get_book_text()
    num_words = count_words(text)
    words = text.split()
    letter_list = get_letters(words)
    letter_count = count_letters(letter_list)
    print (f"============ BOOKBOT ============ \nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count ---------")
    for key, value in letter_count.items():
        print(f"{key}: {value}")
    print("============= END =============")

main()
   
