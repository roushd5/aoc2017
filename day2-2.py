def main():

    test_input = open('input2-1', 'r').read()

    lines = test_input.split('\n')
    
    checksum = 0

    for line in lines:
        if line != '':
            numbers = line.split()
            minimum = 99999999
            maximum = 0
            for number in numbers:
                number = int(number)
                for second_number in numbers:
                    second_number = int(second_number)
                    quotient, remainder = divmod(number, second_number)
                    if remainder == 0 and quotient > 1:
                        print quotient
                        checksum = checksum + quotient

            print checksum




if __name__ == '__main__':
    main()
