
secret_word = "pass"
pass_word = ""
while pass_word != secret_word:
    pass_word = input("enter your password")
    if pass_word != secret_word:
        print("Wrong password, enter again")


