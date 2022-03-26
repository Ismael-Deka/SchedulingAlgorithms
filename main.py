from scheduler import Scheduler
from benchmark import (
    loadProcesses,
    sortProcesses,
    benchmarkAlgorithm,
)


def main():
    processes = []

    processes = loadProcesses()

    sortProcesses(processes, 0, len(processes) - 1)

    benchmarkAlgorithm(Scheduler(0, processes))


if __name__ == "__main__":
    main()
