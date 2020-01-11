import matplotlib.pyplot as plt

def main(int):
    vals = []
    counts = []

    for i in range(1,int):
        count = 0
        vals.append(i)

        while i != 1:
            if i%2 == 0:
                i = i/2
            else:
                i = 3*i + 1

            count +=1
        counts.append(count)

    plt.bar(vals, counts)
    plt.show()

if __name__ == '__main__':
    main()
