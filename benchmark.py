from process_generator import generateProcess


k = 250  ## total number of processes on the system


# ----------------------------------------------------------------------------
#    loadProcesses - helper function that loads newly generated processes into a list
#
#
#    @returns - temp : list         -list of newly generated processes
# ----------------------------------------------------------------------------


def loadProcesses():
    temp = []
    count = k
    while count > 0:
        temp.append(generateProcess())
        count = count - 1
    return temp


# ----------------------------------------------------------------------------
#    benchmarkAlgorthm - measures turnaround and wait times for custom priority scheduling algorthm in nanoseconds.
#                    print average value to the screen when complete
#
#
#    @returns - scheduler : Scheduler         -Scheduler to simulate scheduling method
# ----------------------------------------------------------------------------


def benchmarkAlgorithm(scheduler):
    count = k

    turnaroundTimeSum = 0
    waitTimeSum = 0

    while count > 0:
        endedProcess = scheduler.detachProcess()
        if endedProcess == None:
            break

        turnaroundTime = endedProcess.completion_time - endedProcess.arrival_time
        waitTime = turnaroundTime - endedProcess.burst_time

        turnaroundTimeSum = turnaroundTimeSum + turnaroundTime
        waitTimeSum = waitTimeSum + waitTime

        count = count - 1

    print("----------------------Benchmarking Algorithm-----------------------------\n")
    print("Average turnaround: %f nanoseconds\n" % ((turnaroundTimeSum / k) * 1e9))


# ----------------------------------------------------------------------------
#    sortProcesses - variation of QuickSort thats sorts processes by burst time. Used
#                    to sort processes before being scheduled
#
#
#    @returns - scheduler : Scheduler         -Scheduler to simulate scheduling method
# ----------------------------------------------------------------------------


def sortProcesses(processes, first, last):
    if len(processes) == 1:
        return processes
    if first < last:

        i = first - 1
        pivot = processes[last].burst_time

        for j in range(first, last):
            if processes[j].burst_time <= pivot:

                i = i + 1
                processes[i], processes[j] = processes[j], processes[i]

        processes[i + 1], processes[last] = (
            processes[last],
            processes[i + 1],
        )

        pi = i + 1

        sortProcesses(processes, first, pi - 1)
        sortProcesses(processes, pi + 1, last)
