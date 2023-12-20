#!/usr/bin/env python3

from collections import deque
from copy import deepcopy
from itertools import count
from math import lcm

from utils import advent

advent.setup(2023, 20)
fin = advent.get_input()

graph = {}
flops = {}
conjs = {}

for line in fin.read().splitlines():
    s, ds = line.split("->")
    s = s.strip()
    ds = list(map(str.strip, ds.split(",")))

    if s[0] == "%":
        s = s[1:]
        flops[s] = False
    elif s[0] == "&":
        s = s[1:]
        conjs[s] = {}

    graph[s] = ds

for s, ds in graph.items():
    for d in filter(conjs.__contains__, ds):
        conjs[d][s] = False


def propagate_pulse(graph, flops, conjs, sender, receiver, pulse):
    if receiver in flops:
        if pulse:
            return
        flops[receiver] = not flops[receiver]
        next_pulse = flops[receiver]
    elif receiver in conjs:
        conjs[receiver][sender] = pulse
        next_pulse = not all(conjs[receiver].values())
    elif receiver in graph:
        next_pulse = pulse
    else:
        return

    for new_receiver in graph[receiver]:
        yield receiver, new_receiver, next_pulse


def run(graph, flops, conjs):
    q = deque([("button", "broadcaster", False)])

    low = 0
    high = 0
    while q:
        sender, receiver, pulse = q.popleft()
        low += not pulse
        high += pulse
        q.extend(propagate_pulse(graph, flops, conjs, sender, receiver, pulse))

    return low, high


def find_cycles(graph, flops, conjs):
    useful = set()
    for rx_source, dests in graph.items():
        if dests == ["rx"]:
            assert rx_source in conjs
            break

    for source, dests in graph.items():
        if rx_source in dests:
            assert source in conjs
            useful.add(source)

    for iteration in count(1):
        q = deque([("button", "broadcaster", False)])
        while q:
            sender, receiver, pulse = q.popleft()
            if not pulse:
                if receiver in useful:
                    yield iteration
                    useful.discard(receiver)
                    if not useful:
                        return
            q.extend(propagate_pulse(graph, flops, conjs, sender, receiver, pulse))


orig_flops = deepcopy(flops)
orig_conjs = deepcopy(conjs)

lows = 0
highs = 0
for _ in range(1000):
    low, high = run(graph, flops, conjs)
    lows += low
    highs += high

# Part 1
result_1 = lows * highs
advent.submit_answer(1, result_1)

# Part 2
result_2 = lcm(*find_cycles(graph, orig_flops, orig_conjs))
advent.submit_answer(2, result_2)
