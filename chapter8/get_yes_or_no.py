def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == "Y" or answer == "N":
            valid_input = True
        else:
            print("Please enter Y or N")
    return answer
response = get_yes_or_no("Do you like drama? Y) yes or N) no:")
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')