import csv

ccfile = open("cc.csv", "r")
ccreader = csv.reader(ccfile)

newline = '\n'
runcode = "YES"

print(newline+'Welcome to Currency Converter')

while runcode == "YES":

    print(newline+'You can select one of the options mentioned below:-'+newline)
    print('1. You can convert value of any National/ Digital/ Crypto Currency')
    print('2. You can view the value of Currencies in runcode tabular form'+newline)
    input4 = input('Enter the number corresponding to the required option: ')
    print()

    if input4 == '1':

        input1 = input(
            'Enter Currency Code/ Name/ Country you want to convert from: ')
        input2 = input(
            'Enter Currency Code/ Name/ Country you want to change to: ')
        print()
        input3 = float(input('Enter amount required to convert: '))
        print()

        for ccline in ccreader:

            if ccline[0] == input1.upper():
                value1 = ccline[3]
                currency1 = ccline[0]

            elif ccline[1] == input1.upper():
                value1 = ccline[3]
                currency1 = ccline[0]

            elif ccline[2] == input1.upper():
                value1 = ccline[3]
                currency1 = ccline[0]

            elif ccline[0] == input2.upper():
                value2 = ccline[3]
                currency2 = ccline[0]

            elif ccline[1] == input2.upper():
                value2 = ccline[3]
                currency2 = ccline[0]

            elif ccline[2] == input2.upper():
                value2 = ccline[3]
                currency2 = ccline[0]

        value4 = input3 * float(value2) / float(value1)
        print('The value of', input3, currency1,
              'is equal to', value4, currency2, newline)

        ccfile.seek(0)

    elif input4 == '2':

        print('List of all currencies and their value per USD'+newline)

        for ccline in ccreader:
            space = '  '
            ccline[0] = space + ccline[0]
            ccline[1] = space + ccline[1]
            ccline[2] = space + ccline[2]
            ccline[3] = space + ccline[3]

            while len(ccline[0]) < 10:
                ccline[0] = ccline[0] + " "

            while len(ccline[1]) < 28:
                ccline[1] = ccline[1] + " "

            while len(ccline[2]) < 29:
                ccline[2] = ccline[2] + " "

            while len(ccline[3]) < 13:
                ccline[3] = ccline[3] + " "

            print(ccline)

        ccfile.seek(0)
        print()

    else:
        print('Invalid number entered'+newline)

    input5 = input("Do you want to convert or view more currencies? ").upper()
    runcode = input5

print(newline+'Thank you for using Currency Converter')
