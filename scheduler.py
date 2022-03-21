from dataclasses import dataclass


# -----------------------------------/\/\/\---------------------------------------
#
#    Process - dataclass stucture representing a running process on the system
#
#
#    @fields:   PID : int               - the process's ID
#
#               burst_time : int        - require number of cpu cycles a process
#                                         needs execute before completing.
#
#               execution_time : int    - remaining number of cycles to be executed.
#
#               memory_footprint : int  - required amount of memory needed to execute process.
#
#               arrival_time : int      - time process begins excuting for the first time
#                                         in cpu cycles.
#
#               completion_time : int   - time process stops excuting in cpu cycles.
#
# -----------------------------------\/\/\/-----------------------------------------


@dataclass
class Process:
    PID: int
    burst_time: int
    execution_time: int
    memory_footprint: int
    arrival_time: int
    completion_time: int


# -----------------------------------/\/\/\--------------------------------------
#
#    Processor - dataclass stucture representing one of the system's processors
#
#
#    @fields:   current_process : Process - Process currently occupying processor. It
#                                          defaults to "None"(null) when processor is vacant.
#
# -----------------------------------\/\/\/--------------------------------------


@dataclass
class Processor:
    current_process: Process


# ---------------------/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\----------------------
#
#    Scheduler - class responsible for coordinating between processors and processes
#
#
#    @fields:   clock : int                 - keeps track of the total number of cpu cycles that
#                                             have been executed by all processors.
#
#               process_inverval : int      - maximum number of cpu cycles a process can run before
#                                             surrendering it's processor. It defaults to zero, in
#                                             which case, process runs to completion.
#
#               process_queue : list        - queue of process waiting for a processor to become vacant.
#
#               Pa, Pb, ... Pf : Processor  - represents processors on the system. Six in total.
#
# ---------------------\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/----------------------


class Scheduler:

    # ----------------------------------------------------------------------------
    #    Default Constructor (__init__)
    #
    #    @params:   self                     - In Python, "self" represents the class instance. It is
    #                                          required when referencing non-static fields or functions
    #                                          within a class. Not requred when calling function outside
    #                                          the class. Won't be included in any other docs.
    #
    #                                          e.g. "def __init__(self)" of class "Foo" would be instantiated
    #                                               as "Foo()" instead of "Foo(self)"
    #
    #
    #               process_inveral : int    - new process inverval. defaults to zero.
    #
    #               processes : list         - list of processes to load into available
    #                                          processors and process queue
    #
    # ----------------------------------------------------------------------------

    def __init__(self, process_interval=0, processes=[]):
        self.clock = 0
        self.process_queue = []
        self.Pa = Processor(None)
        self.Pb = Processor(None)
        self.Pc = Processor(None)
        self.Pd = Processor(None)
        self.Pe = Processor(None)
        self.Pf = Processor(None)
        self.process_interval = process_interval
        self.loadProcesses(processes)

    # ----------------------------------------------------------------------------
    #    loadProcesses - function that loads unexecuted processes into processors/process queue
    #
    #
    #    @fields:       processes : list        - list of processes to load into available
    #                                             processors and process queue.
    #
    # ----------------------------------------------------------------------------

    def loadProcesses(self, processes):
        for process in processes:
            self.attachProcess(process)

    # ----------------------------------------------------------------------------
    #    getNextProcessorToDetach - function that finds the next processor to be detached
    #
    #
    #    @returns:     processorToDetach : Processor    - the processor that occupied by the process
    #                                                     with the shortest remaining execution
    #                                                     time. Returns "None" if all processors
    #                                                     are vacant.
    #
    # ----------------------------------------------------------------------------

    def getNextProcessorToDetach(self):
        processorToDetach = None
        shortestRuntime = (
            10e12 + 1
        )  ##Defaults to value larger than maximum possible burst time(10*10^12)

        if self.Pa.current_process != None:
            if self.Pa.current_process.execution_time < shortestRuntime:
                shortestRuntime = self.Pa.current_process.execution_time
                processorToDetach = self.Pa

        if self.Pb.current_process != None:
            if self.Pb.current_process.execution_time < shortestRuntime:
                shortestRuntime = self.Pb.current_process.execution_time
                processorToDetach = self.Pb

        if self.Pc.current_process != None:
            if self.Pc.current_process.execution_time < shortestRuntime:

                shortestRuntime = self.Pc.current_process.execution_time
                processorToDetach = self.Pc

        if self.Pd.current_process != None:
            if self.Pd.current_process.execution_time < shortestRuntime:

                shortestRuntime = self.Pd.current_process.execution_time
                processorToDetach = self.Pd

        if self.Pe.current_process != None:
            if self.Pe.current_process.execution_time < shortestRuntime:
                shortestRuntime = self.Pe.current_process.execution_time
                processorToDetach = self.Pe

        if self.Pf.current_process != None:
            if self.Pf.current_process.execution_time < shortestRuntime:
                shortestRuntime = self.Pf.current_process.execution_time
                processorToDetach = self.Pf

        return processorToDetach

    # ----------------------------------------------------------------------------
    #    getProcessBurstTime - helper function that returns the burst time of a process
    #
    #
    #    @params:      process : Process         - an active process on the system
    #
    #    @returns:     burst_time : int          - burst time of given process. returns
    #                                              (10e12 + 1) which is the maximum possible
    #                                              burst time (10*10^12) plus one.
    #
    # ----------------------------------------------------------------------------

    def getProcessBurstTime(self, process):
        if process != None:
            return process.burst_time
        else:
            return 10e12 + 1

    # ----------------------------------------------------------------------------
    #    updateClock - function that updates the clock and exeuction time of all active processes
    #                  before a process detachs from a processor. if there isn't a process_interval,
    #                  the clock is increamented by the ending processes remaining exeuction time.
    #                  Otherwise, it's incremented by the process interval.
    #
    #
    #    @params:      process : Process         - process that's going to be detached
    #
    # ----------------------------------------------------------------------------
    def updateClock(self, process):
        if self.process_interval == 0:
            self.clock = self.clock + process.execution_time
            if self.Pa.current_process != None:
                self.updateProcessExecutionTimes(self.Pa, process)
            if self.Pb.current_process != None:
                self.updateProcessExecutionTimes(self.Pb, process)
            if self.Pc.current_process != None:
                self.updateProcessExecutionTimes(self.Pc, process)
            if self.Pd.current_process != None:
                self.updateProcessExecutionTimes(self.Pd, process)
            if self.Pe.current_process != None:
                self.updateProcessExecutionTimes(self.Pe, process)
            if self.Pf.current_process != None:
                self.updateProcessExecutionTimes(self.Pf, process)
        else:
            self.clock = self.clock + self.process_interval

    # ----------------------------------------------------------------------------
    #    updateProcessExecutionTimes - Helper function to update execution times of all other active processes.
    #                                  Processes running concerrently with the ending process need to
    #                                  have their excution times reduced by the amount of time
    #                                  the ending process had run for.
    #
    #                                  e.g. Process A had run for 100 cycles, so Processes B to F need to
    #                                       have their remaining execution time reduced by 100 because they were
    #                                       running at the same time as Process A
    #
    #
    #    @params:                     processor : Processor     - processor of process that will be detacted
    #
    #                                 process : Process         - process that's going to be detached
    #
    # ----------------------------------------------------------------------------

    def updateProcessExecutionTimes(self, processor, process):

        if processor.current_process.execution_time > process.execution_time:
            processor.current_process.execution_time = (
                processor.current_process.execution_time - process.execution_time
            )
        else:
            processor.current_process.execution_time = 0

    # ----------------------------------------------------------------------------
    #    detactProcess - function that will detact a process from one of the processors on the system.
    #                    Once detacted, the next process in the process queue is attached to the next availible processor.
    #                    If there is a process interval greater than zero and the burst time is greater than the interval,
    #                    than the ending process is pushed back to the end of the process queue.
    #
    #
    #    @returns:      endingProcess : Process         - process that's going to be detached. Returns "None"
    #                                                     if all processors are vacant
    #
    # ----------------------------------------------------------------------------

    def detactProcess(self):
        processor = self.getNextProcessorToDetach()
        if processor == None:
            return None
        self.updateClock(processor.current_process)

        endingProcess = processor.current_process

        endingProcess.completion_time = self.clock

        processor.current_process = None

        if self.process_queue:
            self.attachProcess(self.process_queue.pop(0))

        if self.process_interval == 0 or endingProcess.burst_time == 0:
            return endingProcess
        else:
            if self.process_interval <= endingProcess.burst_time:
                endingProcess.burst_time = (
                    endingProcess.burst_time - self.process_interval
                )
            else:
                endingProcess.burst_time = 0
            self.process_queue.append(endingProcess)
            return endingProcess

    # ----------------------------------------------------------------------------
    #    attachProcess - function that will attact a process to the next availible processor. If all
    #                    processors are occupied, the process is pushed to the back of the process queue
    #
    #
    #    @returns:      newProcess : Process         - process attempting to execute.
    #
    # ----------------------------------------------------------------------------

    def attachProcess(self, newProcess):

        if self.Pa.current_process == None:
            if newProcess.arrival_time == -1:
                newProcess.arrival_time = self.clock
            self.Pa.current_process = newProcess

        elif self.Pb.current_process == None:
            if newProcess.arrival_time == -1:
                newProcess.arrival_time = self.clock
            self.Pb.current_process = newProcess

        elif self.Pc.current_process == None:

            if newProcess.arrival_time == -1:
                newProcess.arrival_time = self.clock
            self.Pc.current_process = newProcess

        elif self.Pd.current_process == None:
            if newProcess.arrival_time == -1:
                newProcess.arrival_time = self.clock
            self.Pd.current_process = newProcess

        elif self.Pe.current_process == None:
            if newProcess.arrival_time == -1:
                newProcess.arrival_time = self.clock
            self.Pe.current_process = newProcess

        elif self.Pf.current_process == None:
            if newProcess.arrival_time == -1:
                newProcess.arrival_time = self.clock

            self.Pf.current_process = newProcess
        else:
            self.process_queue.append(newProcess)
