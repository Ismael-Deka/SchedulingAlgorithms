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
#    benchmarkFIFO - measures turnaround and wait times for First-In-First-Out(FIFO) scheduling in cpu cycles.
#                    print average value to the screen when complete
#
#
#    @returns - scheduler : Scheduler         -Scheduler to simulate scheduling method
# ----------------------------------------------------------------------------


def benchmarkFIFO(scheduler):
    count = k

    turnaroundTimeSum = 0
    waitTimeSum = 0

    while count > 0:
        endedProcess = scheduler.detactProcess()
        if endedProcess == None:
            break

        turnaroundTime = endedProcess.completion_time - endedProcess.arrival_time
        waitTime = turnaroundTime - endedProcess.burst_time

        endedProcess.clock_time = endedProcess.burst_time
        turnaroundTimeSum = turnaroundTimeSum + turnaroundTime
        waitTimeSum = waitTimeSum + waitTime

        count = count - 1

    print("----------------------Benchmarking FIFO-----------------------------\n")
    print(
        "Average turnaround: "
        + "{:.2e}".format(turnaroundTimeSum / k)
        + " (%d cycles)\n" % (turnaroundTimeSum / k)
    )
    print(
        "Average wait time: "
        + "{:.2e}".format(waitTimeSum / k)
        + " (%d cycles) \n\n" % (waitTimeSum / k)
    )


# ----------------------------------------------------------------------------
#    benchmarkSJR - measures turnaround and wait times for Shortest job first(SJR) scheduling in CPU cycles.
#                    print average value to the screen when complete
#
#
#    @returns - scheduler : Scheduler         -Scheduler to simulate scheduling method
# ----------------------------------------------------------------------------


def benchmarkSJR(scheduler):
    count = k

    turnaroundTimeSum = 0
    waitTimeSum = 0

    while count > 0:
        endedProcess = scheduler.detactProcess()
        if endedProcess == None:
            break

        turnaroundTime = endedProcess.completion_time - endedProcess.arrival_time
        waitTime = turnaroundTime - endedProcess.burst_time

        turnaroundTimeSum = turnaroundTimeSum + turnaroundTime
        waitTimeSum = waitTimeSum + waitTime

        count = count - 1

    print("----------------------Benchmarking SJR-----------------------------\n")
    print(
        "Average turnaround: "
        + "{:.2e}".format(turnaroundTimeSum / k)
        + " (%d cycles)\n" % (turnaroundTimeSum / k)
    )
    print(
        "Average wait time: "
        + "{:.2e}".format(waitTimeSum / k)
        + " (%d cycles)\n\n" % (waitTimeSum / k)
    )


# ----------------------------------------------------------------------------
#    benchmarkRR - measures turnaround and wait times for Round Robin(RR) scheduling in CPU cycles.
#                  prints average value to the screen when complete
#
#
#    @returns - scheduler : Scheduler         -Scheduler to simulate scheduling method
# ----------------------------------------------------------------------------


def benchmarkRR(scheduler):
    count = 0

    turnaroundTimeSum = 0
    waitTimeSum = 0

    while True:
        endedProcess = scheduler.detactProcess()
        if endedProcess == None:
            break
        turnaroundTime = endedProcess.completion_time - endedProcess.arrival_time
        waitTime = turnaroundTime - endedProcess.burst_time

        turnaroundTimeSum = turnaroundTimeSum + turnaroundTime
        waitTimeSum = waitTimeSum + waitTime

        count = count + 1

    print("----------------------Benchmarking RR-----------------------------\n")
    print(
        "Average turnaround: "
        + "{:.2e}".format(turnaroundTimeSum / count)
        + " (%d cycles)\n" % (turnaroundTimeSum / count)
    )
    print(
        "Average wait time: "
        + "{:.2e}".format(waitTimeSum / count)
        + " (%d cycles)\n\n" % (waitTimeSum / count)
    )


# ----------------------------------------------------------------------------
#    sortProcesses - variation of QuickSort thats sorts processes by burst time. Used
#                    to sort processes for SJR scheduling
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
