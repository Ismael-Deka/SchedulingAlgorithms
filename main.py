import copy
from scheduler import Scheduler
from QuestionTwoAlgorithm.scheduler import QuestionTwoScheduler
from QuestionTwoAlgorithm.benchmark import (
    loadProcesses,
    sortProcesses,
    benchmarkQuestionTwoAlgorithm,
)
from benchmark import (
    loadProcesses,
    sortProcesses,
    benchmarkQuestionThreeAlgorithm,
)


def main():
    processesOne = []

    processesOne = loadProcesses()

    processesTwo = copy.deepcopy(processesOne)

    sortProcesses(processesOne, 0, len(processesOne) - 1)
    sortProcesses(processesTwo, 0, len(processesTwo) - 1)

    benchmarkQuestionTwoAlgorithm(QuestionTwoScheduler(0, processesOne))

    benchmarkQuestionThreeAlgorithm(Scheduler(0, processesTwo))


if __name__ == "__main__":
    main()
