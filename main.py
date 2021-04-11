import logo
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
go_again = "true"
while not go_again.lower() == "no":
    print(logo.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    if direction == "encode":
        list_of_name = []
        i = 0
        fark = 0
        while i < len(text):
            for n in text:
                if n in alphabet:
                    if alphabet.index(n) + shift >= len(alphabet):
                        fark = len(alphabet) - alphabet.index(n)
                        list_of_name.append(alphabet[shift - fark])
                    else:
                        list_of_name.append(
                            alphabet[(alphabet.index(n) + shift)])
                else:
                    list_of_name.append(n)
                i += 1

        list_of_name_str = ""

        for n in list_of_name:
            list_of_name_str = list_of_name_str + n
        print(f"The cipher result is:{list_of_name_str} the key is {shift}")

    elif direction == "decode":
        list_of_name = []
        i = 0

        while i < len(text):
            for n in text:
                if n in alphabet:
                    list_of_name.append(alphabet[(alphabet.index(n) - shift)])
                else:
                    list_of_name.append(n)
                i += 1

        list_of_name_str = ""

        for n in list_of_name:
            list_of_name_str = list_of_name_str + n
        print(f"The cipher result is:{list_of_name_str} the key is {shift}")

    go_again = input(
        "Go again to'yes' or u don't need to try one more time type 'no'..\n")
    if go_again == "no":
        print("GoodBye")
    elif go_again == "yes":
        print()
    else:
        print("Wrong choice u banned the cipher generator! BYEE")
        go_again = "no"