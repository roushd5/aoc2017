def main():

    test_input = open('input2-1', 'r').read()

    lines = test_input.split('\n')
    
    difference = 0

    for line in lines:
        if line != '':
            numbers = line.split()
            minimum = 99999999
            maximum = 0
            for number in numbers:
                number = int(number)
                if number > maximum:
                    maximum = number
                if number < minimum:
                    minimum = number
            difference = difference + (maximum - minimum)
            print difference




if __name__ == '__main__':
    main()
