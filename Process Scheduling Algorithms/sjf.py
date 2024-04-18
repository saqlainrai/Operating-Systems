
class tuple:
    def __init__(self, name, burst_time, arrival_time):
        self.name = name
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.wait_time = 0
        self.temp_burst_time = burst_time

def findIndex(name, allTuples):
    for i in range(len(allTuples)):
        if allTuples[i].name == name:
            return i
    return -1

def main():
    sliceIterator = 0
    time = 0
    q = []
    file1 = open('sjfInput.txt', 'r')
    file2 = open('sjfOutput.txt', 'w')
    file_contents = file1.read()
    
    allTuples = []
    for line in file_contents.split('\n'):
        name, bt, at = line.split(' ')
        t = tuple(name, int(bt), int(at))
        allTuples.append(t)

    maxBurst, maxArrival = 0, 0
    for i in allTuples:
        maxBurst += i.burst_time
        maxArrival = max(maxArrival, i.arrival_time)
    time = maxBurst + maxArrival

    for i in range(time):
        for j in allTuples:
            if j.arrival_time == i:
                q.append(j)

        q.sort(key=lambda x: x.temp_burst_time)
        if len(q) != 0:
            if q[0].temp_burst_time > 0:
                q[0].temp_burst_time -= 1
            else:
                allTuples[findIndex(q[0].name, allTuples)].completion_time = i
                q.pop(0)

    for i in range(len(allTuples)):
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

    print("Done writing the output to sjfOutput.txt and calculating time...")
    print("Average Waiting Time: ", average_waiting_time)
    print("Average Turnaround Time", average_turnaround_time)

if __name__ == "__main__":
    main()