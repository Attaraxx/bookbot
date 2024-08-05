def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(f"{count} words found in document\n\n")
    letters = count_chars(text)
    #print(f"{letters} letters found in text")
    report(letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    chars = {}
    for x in text:
        if x in chars:
            chars[x] = chars[x] + 1
        else:
            chars[x] = 1
    return chars

def report(text):
    chars = {}
    #buch = {}
    report = []
    for k in text:
        if k.isalpha():
            chars[k] = text[k]
    lk = zip(chars.keys(), chars.values())
    lk = list(lk)
    for l in lk:
        #buch[l[0]] = l[1]
        buch = {}
        buch["character"] = l[0]
        buch["counts"] = l[1]
        report.append(buch)
    report.sort(key=sort_on, reverse=True)
    #print(lk)
    for rep in report:
        print(f"The {rep["character"]} character was found {rep["counts"]} times")
    return None


def sort_on(dict):
    return dict["counts"]
 

main()
