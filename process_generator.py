from scheduler import Process
import datetime
import random


# ----------------------------------------------------------------------------
#    generateProcess - generates a new process with a randomly generated
#                      process ID, burst time and memory footprint
#
#
#    @returns - new Process object : Process
# ----------------------------------------------------------------------------


def generateProcess():
    burstTime = generateBurstTimeCycles()

    ##exeution_time is equal burst_time for new processes
    ##arrival_time and completion_time default to -1
    return Process(generatePID(), burstTime, burstTime, generateMemFootprint(), -1, -1)


# ----------------------------------------------------------------------------
#    generatePID - generates a process ID based on the number of second since
#                  midnight times a random number between 1-100
#
#
#    @returns - new Process ID : int
# ----------------------------------------------------------------------------


def generatePID():
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time())
    seconds = (now - midnight).seconds
    return seconds * random.randint(1, 100)


# ----------------------------------------------------------------------------
#    generateBurstTimeCycles - generates burst cpu cycle between 10 X 10^6 and 10 X 10^12
#
#
#
#    @returns - randomly generated burst time : int
# ----------------------------------------------------------------------------


def generateBurstTimeCycles():
    return int(random.random() * pow(10, random.randint(6, 12)))


# ----------------------------------------------------------------------------
#    generateMemFootprint - generate required memory bewteen 1MB and 16GB(16,384MB)
#
#
#
#    @returns - randomly generated memory footprint in MB : int
# ----------------------------------------------------------------------------


def generateMemFootprint():
    return random.randint(1, 16384)
