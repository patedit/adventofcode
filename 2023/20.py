from advent import Advent
from collections import deque
from math import prod, lcm

advent = Advent(2023, 20, use_file=False)

class Module:
    def __init__(self, name, outputs=[]):
        self._outputs = list(outputs)
        self._name = name

    # def process(self, pulse, from_module):
    #     pass

    def state(self):
        pass

    def add_input(self):
        pass

    def reset_state(self):
        pass

    def outputs(self):
        return self._outputs
    
    def name(self):
        return self._name

class FlipFlop(Module):
    def __init__(self, name, outputs=[]):
        super().__init__(name, outputs)
        self._state = False

    def process(self, pulse, from_module):
        if pulse is False:
            self._state = (not self._state) if not pulse else self._state
            return self._state
        return None

    def state(self):
        return self._state
    
    def reset_state(self):
        self._state = False
    
class Conjuction(Module):
    def __init__(self, name, outputs=[]):
        super().__init__(name, outputs)
        self._state = {}

    def process(self, pulse, from_module):
        self._state[from_module] = pulse
        return not all(self._state.values())

    def add_input(self, name):
        self._state[name] = False

    def state(self):
        return self._state
    
    def reset_state(self):
        for k in self._state.keys():
            self._state[k] = False
    
class Broadcaster(Module):
    def process(self, pulse, from_module):
        return pulse

    def state(self):
        return 0

modules = {}
for line in advent.lines:
    module, outputs = line.split(" -> ")
    outputs = outputs.split(", ")
    if module[0] == '%':
        module = FlipFlop(module[1:], outputs)
    elif module[0] == '&':
        module = Conjuction(module[1:], outputs)
    elif module == 'broadcaster':
        module = Broadcaster(module, outputs)
    
    modules[module.name()] = module

for module in modules.values():
    for output in module.outputs():
        if output not in modules: continue
        if isinstance(modules[output], Conjuction):
            modules[output].add_input(module.name())

# Part 1
pulses_sent = {True: 0, False: 0}
for _ in range(1000):
    q = deque([(False, 'broadcaster', None)])
    while q:
        pulse, mod_name, from_mode_name = q.popleft()
        pulses_sent[pulse] += 1
        if mod_name not in modules: continue
        orig_state = modules[mod_name].state()
        nv = modules[mod_name].process(pulse, from_mode_name)

        if nv is not None:
            for output in modules[mod_name].outputs():
                q.append((nv, output, mod_name))

print(prod(pulses_sent.values()))


# Part 2
[m.reset_state() for n, m in modules.items()]
pulses = 0
inputs = dict(modules['cs'].state()) # Asked for 'rx', which is connected to cs

for button_press in range(1, 10000):
    q = deque([(False, 'broadcaster', None)])
    while q:
        pulse, mod_name, from_mode_name = q.popleft()
        if mod_name not in modules: continue
        if mod_name in inputs.keys() and pulse is False and inputs[mod_name] is False:
            inputs[mod_name] = button_press
        orig_state = modules[mod_name].state()
        nv = modules[mod_name].process(pulse, from_mode_name)

        if nv is not None:
            for output in modules[mod_name].outputs():
                q.append((nv, output, mod_name))

print(lcm(*inputs.values()))
