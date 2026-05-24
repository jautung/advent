from itertools import permutations

import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '7_dat.txt'
mapper = {}

def main():
    data = [int(i) for i in readlines(FILENAME)[0].split(',')]
    phases = list(range(5))
    highestSoFar = None
    for phaseSettingSequence in permutations(phases):
        phaseSettingSequence = list(phaseSettingSequence)
        candidate = runWithPhaseSettingSequence(phaseSettingSequence, data)
        # print(candidate, phaseSettingSequence)
        if highestSoFar is None or candidate > highestSoFar[0]:
            highestSoFar = candidate, phaseSettingSequence
    print(highestSoFar)

def runWithPhaseSettingSequence(phaseSettingSequence, data):
    INPUT = 0
    # phaseSettingSequence = [4,3,2,1,0]
    for idx, phaseSetting in enumerate(phaseSettingSequence):
        # print(f"passing INPUT {INPUT} to idx {idx}")
        newInput = runProgram([phaseSetting, INPUT], data)
        # print(f"- got OUTPUT {newInput}")
        INPUT = newInput
    return INPUT

def runProgram(INPUT, data):
    input_pos = 0
    curr_pos = 0
    while True:
        # print(f".... stepping {curr_pos}")
        curr_opcode = data[curr_pos]
        parm_modes = curr_opcode//100
        parm_mode_1 = parm_modes%10
        parm_mode_2 = (parm_modes%100) // 10
        parm_mode_3 = (parm_modes%1000) // 100
        curr_opcode = curr_opcode%100
        # print(curr_opcode, parm_mode_1, parm_mode_2, parm_mode_3)
        if curr_opcode == 1:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            data[out] = real_inp1 + real_inp2
            curr_pos += 4
        elif curr_opcode == 2:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            data[out] = real_inp1 * real_inp2
            curr_pos += 4
        elif curr_opcode == 3:
            inp = data[curr_pos+1]
            assert(parm_mode_1 == 0)
            # print('input will be stored in position', inp)
            assert(input_pos < len(INPUT))
            # print(f"  > getting input of {INPUT[input_pos]}")
            data[inp] = INPUT[input_pos]
            input_pos += 1
            curr_pos += 2
        elif curr_opcode == 4:
            out = data[curr_pos+1]
            # print('a', out, data[out])
            if parm_mode_1 == 0:
                real_out = data[out]
            elif parm_mode_1 == 1:
                real_out = out
            # print('output is', real_out)
            # print(f"  > emitting output of {real_out}")
            return real_out
            # assert(real_out == 0)
            curr_pos += 2
        elif curr_opcode == 5:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            if real_inp1 != 0:
                curr_pos = real_inp2
            else:
                curr_pos += 3
        elif curr_opcode == 6:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            if real_inp1 == 0:
                curr_pos = real_inp2
            else:
                curr_pos += 3
        elif curr_opcode == 7:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            if real_inp1 < real_inp2:
                data[out] = 1
            else:
                data[out] = 0
            curr_pos += 4
        elif curr_opcode == 8:
            inp1 = data[curr_pos+1]
            inp2 = data[curr_pos+2]
            out = data[curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            if real_inp1 == real_inp2:
                data[out] = 1
            else:
                data[out] = 0
            curr_pos += 4
        elif curr_opcode == 99:
            # print(data[0])
            return None
        else:
            assert(False)

def main2():
    data = [int(i) for i in readlines(FILENAME)[0].split(',')]

    phases = list(range(5, 10))
    highestSoFar = None
    for phaseSettingSequence in permutations(phases):
        phaseSettingSequence = list(phaseSettingSequence)
        candidate = runWithPhaseSettingSequence2(phaseSettingSequence, data)
        # print(candidate, phaseSettingSequence)
        if highestSoFar is None or candidate > highestSoFar[0]:
            highestSoFar = candidate, phaseSettingSequence
    print(highestSoFar)


def runWithPhaseSettingSequence2(phaseSettingSequence, data):
    amplifiers = []
    for pIdx, phaseSetting in enumerate(phaseSettingSequence):
        amplifier = Amplifier(data=data, phase=phaseSetting, gid=pIdx)
        amplifiers.append(amplifier)
    
    RUNNING_PASSOVER_SIGNALS = 0
    waiting_amplifier_index = 0
    latest_outputs = [None for _ in range(5)]
    while True:
        # print(f"passing signal {RUNNING_PASSOVER_SIGNALS} to index {waiting_amplifier_index}")
        waiting_amplifier = amplifiers[waiting_amplifier_index]
        result = waiting_amplifier.runProgramUntilInput(inpVal=RUNNING_PASSOVER_SIGNALS)
        if result == "HALT":
            # print(" - halted while waiting for input!")
            break
        elif result == "INPUT_USED":
            result_out = waiting_amplifier.runProgramUntilOutput()
            # print(" - waiting for output")
            if result_out == "HALT":
                # print(" - halted while waiting for output!")
                break
            elif result_out == "OUTPUT":
                # print(f" - output: {waiting_amplifier.latest_out}")
                RUNNING_PASSOVER_SIGNALS = waiting_amplifier.latest_out
                latest_outputs[waiting_amplifier_index] = waiting_amplifier.latest_out
            waiting_amplifier_index = (waiting_amplifier_index + 1) % 5
            continue
    return latest_outputs[-1]


class Amplifier:
    def __init__(self, data, phase, gid):
        self.data = copy.deepcopy(data)
        self.curr_pos = 0
        self.phase = phase
        self.gid = gid
        self.latest_out = None

        initialResult = self.runProgramUntilInput(inpVal=phase)
        assert initialResult == "INPUT_USED"

    def runProgramUntilInput(self, inpVal):
        # print(f"   - {self.gid}: running program until input {inpVal}")
        while True:
            result = self.runStep(maybeInput=inpVal)
            if result == "HALT":
                return "HALT"
            elif result == "INPUT_USED":
                return "INPUT_USED"

    def runProgramUntilOutput(self):
        while True:
            result = self.runStep(maybeInput=None)
            if result == "HALT":
                return "HALT"
            elif result == "OUTPUT":
                return "OUTPUT"

    # returns None for any normal instruction
    # returns outputted value for output instruction
    # maybeInput ONLY used for input instruction
    # returns "HALT" literally when halting
    def runStep(self, maybeInput):
        # print(f"       x {self.gid}: stepping {self.curr_pos}")
        curr_opcode = self.data[self.curr_pos]
        parm_modes = curr_opcode//100
        parm_mode_1 = parm_modes%10
        parm_mode_2 = (parm_modes%100) // 10
        parm_mode_3 = (parm_modes%1000) // 100
        curr_opcode = curr_opcode%100
        # print(curr_opcode, parm_mode_1, parm_mode_2, parm_mode_3)
        if curr_opcode == 1:
            inp1 = self.data[self.curr_pos+1]
            inp2 = self.data[self.curr_pos+2]
            out = self.data[self.curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = self.data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = self.data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            self.data[out] = real_inp1 + real_inp2
            self.curr_pos += 4
            return "CONTINUE"
        elif curr_opcode == 2:
            inp1 = self.data[self.curr_pos+1]
            inp2 = self.data[self.curr_pos+2]
            out = self.data[self.curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = self.data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = self.data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            self.data[out] = real_inp1 * real_inp2
            self.curr_pos += 4
            return "CONTINUE"
        elif curr_opcode == 3:
            inp = self.data[self.curr_pos+1]
            assert(parm_mode_1 == 0)
            # print('input will be stored in position', inp)
            # assert(input_pos < len(INPUT))
            assert maybeInput is not None
            # print(f"  > {self.gid}: getting input of {maybeInput}")
            self.data[inp] = maybeInput
            self.curr_pos += 2
            return "INPUT_USED"
        elif curr_opcode == 4:
            out = self.data[self.curr_pos+1]
            # print('a', out, data[out])
            if parm_mode_1 == 0:
                real_out = self.data[out]
            elif parm_mode_1 == 1:
                real_out = out
            # print('output is', real_out)
            # print(f"  > {self.gid}: emitting output of {real_out}")
            self.latest_out = real_out
            self.curr_pos += 2
            return "OUTPUT"
        elif curr_opcode == 5:
            inp1 = self.data[self.curr_pos+1]
            inp2 = self.data[self.curr_pos+2]
            if parm_mode_1 == 0:
                real_inp1 = self.data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = self.data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            if real_inp1 != 0:
                self.curr_pos = real_inp2
            else:
                self.curr_pos += 3
            return "CONTINUE"
        elif curr_opcode == 6:
            inp1 = self.data[self.curr_pos+1]
            inp2 = self.data[self.curr_pos+2]
            if parm_mode_1 == 0:
                real_inp1 = self.data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = self.data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            if real_inp1 == 0:
                self.curr_pos = real_inp2
            else:
                self.curr_pos += 3
            return "CONTINUE"
        elif curr_opcode == 7:
            inp1 = self.data[self.curr_pos+1]
            inp2 = self.data[self.curr_pos+2]
            out = self.data[self.curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = self.data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = self.data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            if real_inp1 < real_inp2:
                self.data[out] = 1
            else:
                self.data[out] = 0
            self.curr_pos += 4
            return "CONTINUE"
        elif curr_opcode == 8:
            inp1 = self.data[self.curr_pos+1]
            inp2 = self.data[self.curr_pos+2]
            out = self.data[self.curr_pos+3]
            if parm_mode_1 == 0:
                real_inp1 = self.data[inp1]
            elif parm_mode_1 == 1:
                real_inp1 = inp1
            if parm_mode_2 == 0:
                real_inp2 = self.data[inp2]
            elif parm_mode_2 == 1:
                real_inp2 = inp2
            assert(parm_mode_3 == 0)
            if real_inp1 == real_inp2:
                self.data[out] = 1
            else:
                self.data[out] = 0
            self.curr_pos += 4
            return "CONTINUE"
        elif curr_opcode == 99:
            # print(data[0])
            return "HALT"
        else:
            assert(False)

# def main3():
#     data = [int(i) for i in readlines(FILENAME)[0].split(',')]

#     amplifiers = []
#     phaseSettingSequence = [4,3,2,1,0]
#     for pIdx, phaseSetting in enumerate(phaseSettingSequence):
#         amplifier = Amplifier(data=data, phase=phaseSetting, gid=pIdx)
#         amplifiers.append(amplifier)
    
#     RUNNING_PASSOVER_SIGNALS = 0
#     waiting_amplifier_index = 0
#     latest_outputs = [None for _ in range(5)]
#     while True:
#         print(f"passing signal {RUNNING_PASSOVER_SIGNALS} to index {waiting_amplifier_index}")
#         waiting_amplifier = amplifiers[waiting_amplifier_index]
#         result = waiting_amplifier.runProgramUntilInput(RUNNING_PASSOVER_SIGNALS)
#         if result == "HALT":
#             print(" - halted while waiting for input!")
#             break
#         elif result == "INPUT_USED":
#             result_out = waiting_amplifier.runProgramUntilOutput()
#             print(" - waiting for output")
#             if result_out == "HALT":
#                 print(" - halted while waiting for output!")
#                 break
#             elif result_out == "OUTPUT":
#                 print(f" - output: {waiting_amplifier.latest_out}")
#                 RUNNING_PASSOVER_SIGNALS = waiting_amplifier.latest_out
#                 latest_outputs[waiting_amplifier_index] = waiting_amplifier.latest_out
#             waiting_amplifier_index = (waiting_amplifier_index + 1) % 5
#             if waiting_amplifier_index == 0:
#                 break
#             continue
#     print(latest_outputs)

if __name__ == '__main__':
    main()
    main2()
    # runWithPhaseSettingSequence([4,3,2,1,0], [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
    # print()
    # main3()
