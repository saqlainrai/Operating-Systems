
class tuple:
    def __init__(self, name, priority, arrival_time, burst_time):
        self.name = name
        self.priority = priority
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.wait_time = 0

def main():
    file1 = open('psaInput.txt', 'r')
    file2 = open('psaOutput.txt', 'w')
    file_contents = file1.read()
    
    allTuples = []
    for line in file_contents.split('\n'):
        name, p, at, bt = line.split(' ')
        t = tuple(name, int(p), int(at), int(bt))
        allTuples.append(t)

    allTuples.sort(key=lambda x: x.arrival_time)
    allTuples.sort(key=lambda x: x.priority)

    # calculating all time values for each process
    for i in range(len(allTuples)):
        if i == 0:
            allTuples[i].completion_time = allTuples[i].burst_time + allTuples[i].arrival_time
        else:
            if allTuples[i-1].completion_time < allTuples[i].arrival_time:
                allTuples[i].completion_time = allTuples[i].arrival_time + allTuples[i].burst_time
            else:
                allTuples[i].completion_time = allTuples[i - 1].completion_time + allTuples[i].burst_time
        allTuples[i].turnaround_time = allTuples[i].completion_time - allTuples[i].arrival_time
        allTuples[i].wait_time = allTuples[i].turnaround_time - allTuples[i].burst_time

    allTuples.sort(key=lambda x: x.name)

    # writing result in output file
    file2.write("Name AT BT CT TAT WT\n")
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in allTuples:
        file2.write(i.name + ' ' + str(i.arrival_time) + ' ' + str(i.burst_time) + ' ' + str(i.completion_time) + ' ' + str(i.turnaround_time) + ' ' + str(i.wait_time) + '\n')
        total_waiting_time += i.wait_time
        total_turnaround_time += i.turnaround_time

    file1.close()
    file2.close()

    average_waiting_time = total_waiting_time / len(allTuples)
    average_turnaround_time = total_turnaround_time / len(allTuples)

    print("Done writing the output to fcfsOutput.txt and calculating time...")
    print("Average Waiting Time: ", average_waiting_time)
    print("Average Turnaround Time", average_turnaround_time)

if __name__ == "__main__":
    main()