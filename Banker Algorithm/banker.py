# Banker's Algorithm
def main():
    # pro = input("Enter the number of processes: ")
    # res = input("Enter the number of resources: ")

    pro, res = 5, 3

    file1 = open('input.txt', 'r')
    file2 = open('output.txt', 'w')
    file_contents = file1.read()

    arr = [[0 for _ in range(res*3)] for _ in range(pro)]

    row = 0
    for line in file_contents.split('\n'):
        array  = line.split(' ')
        for i in range(len(array)):
            arr[row][i] = int(array[i])
        row += 1

    # print(arr)

    for i in arr:
        for j in range(res):
            i[(res*2)+j] = i[res+j] - i[j]
    
    for i in arr:
        file2.write(str(i) + '\n')


if __name__ == "__main__":
    main()