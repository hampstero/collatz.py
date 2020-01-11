from math import *
import matplotlib
import collatz_plot

def main():

    while True:

        num = input("\nEnter a natural number. Press Enter to exit. Input plot to show iteration lengths in range (0,1000)\n")
        if num == 'plot':
            collatz_plot.main()
            continue
        if num == '':
            return
        try:
            num = eval(num)
            if int(num) == False or num < 0:
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