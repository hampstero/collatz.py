from math import *
import matplotlib
import collatz_plot

def main():

    while True:

        num = input("\nEnter a natural number. Press Enter to exit. Input plot to show iteration lengths in any desired range\n")
        if num == 'plot':
            rng = input("\nChoose the range\n")
            if isinstance(eval(rng), int) == False:
                print("Improper input")
                continue
            collatz_plot.main(eval(rng))
            continue
        if num == '':
            return
        try:
            num = eval(num)
            if isinstance(num, int) == False or num < 0:
                print("Improper input")
                continue
        except NameError:
            print("Improper input")
            continue

        count = 0
        while True:

            if num == 1:
                print(f"\nIterations required to reach loop {count}\n")
                break

            if num%2==0:
                num = num/2
            else:
                num = 3*num + 1

            print(num)

            count += 1
if __name__ == '__main__':
    main()