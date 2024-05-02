# Banker's Algorithm
def main():
    # pro = input("Enter the number of processes: ")
    # res = input("Enter the number of resources: ")

    pro, res = 5, 3

    file = open('stats.txt', 'r')
    file_contents = file.read()

    arr = [[0 for _ in range(res*3)] for _ in range(pro)]

    row = 0
    for line in file_contents.split('\n'):
        array  = line.split(' ')
        for i in range(len(array)):
            arr[row][i] = int(array[i])
        row += 1
        # print(array)
    print(arr)

if __name__ == "__main__":
    main()