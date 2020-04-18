def is_palindrom(word):
    rword=word[::-1]
    if word==rword:
        print("plimdrom")
    else:
        print("not")

is_palindrom("hello")
is_palindrom("hah")
