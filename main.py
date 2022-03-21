from scheduler import Scheduler
import copy
from benchmark import (
    loadProcesses,
    sortProcesses,
    benchmarkFIFO,
    benchmarkRR,
    benchmarkSJR,
)


def main():
    fifo_Processes = []
    sjr_Processes = []
    rr_Processes = []

    fifo_Processes = loadProcesses()
    sjr_Processes = (
        copy.deepcopy(  ##Making sure each scheduling method uses the same data
            fifo_Processes
        )
    )
    rr_Processes = copy.deepcopy(fifo_Processes)
    sortProcesses(sjr_Processes, 0, len(sjr_Processes) - 1)

    benchmarkFIFO(Scheduler(0, fifo_Processes))
    benchmarkSJR(Scheduler(0, sjr_Processes))
    benchmarkRR(Scheduler(10e8, rr_Processes))


if __name__ == "__main__":
    main()
