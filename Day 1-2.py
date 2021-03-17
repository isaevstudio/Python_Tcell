names = []
phone_numbers = []
num = 1


def phonebook():
    while True:
        name = input("May I know your full name, please? ")
        if name == "":
            printing()
            exit()
        phone_number = int(input("May I have your phone number? "))
        names.append(name)
        phone_numbers.append(phone_number)
num += 1

def printing():
    print_phonebook()
    searchfor()


def print_phonebook():
    for i in range(num):
        print("Full Name: {}\t\t\t Contact Number: {}".format(names[i], phone_numbers[i]))


def searchfor():
    while True:
        search_term = input("Enter search term: ")
        print("Search results: ")
        if search_term == "exit":
            break
        if search_term in names:
           index = names.index(search_term)
           phone_number = phone_numbers[index]
           print("Number is: {}".format(phone_number))
        else:
            print("Such person doesn't exist in our phone-book")
        print("Type \"exit\" to end the program")

def main():
    phonebook()
    # print_phonebook()
    # searchfor()
main()

