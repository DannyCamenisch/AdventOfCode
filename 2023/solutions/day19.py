#!/usr/bin/env python3

import copy
from math import prod

from utils import advent

advent.setup(2023, 19)
fin = advent.get_input()

r, p = fin.read().split("\n\n")

r = r.strip().split("\n")
p = p.strip().split("\n")

rules = {}
for rule in r:
    name, rule = rule.removesuffix("}").split("{")
    rules[name] = rule

parts = [
    [int(component.split("=")[1]) for component in part.removesuffix("}").split(",")]
    for part in p
]

lut = "xmas"


def apply_rules(rule_name, part):
    if rule_name == "A":
        return True
    elif rule_name == "R":
        return False

    rule = rules[rule_name]
    stmts = rule.split(",")

    next_rule = stmts[-1]
    for stmt in stmts[:-1]:
        condition, destination = stmt.split(":")
        if "<" in condition:
            condition = condition.split("<")
            if part[lut.index(condition[0])] < int(condition[1]):
                return apply_rules(destination, part)
        elif ">" in condition:
            condition = condition.split(">")
            if part[lut.index(condition[0])] > int(condition[1]):
                return apply_rules(destination, part)

    return apply_rules(next_rule, part)


def apply_range(part, idx, op, value):
    p = copy.deepcopy(part)

    if op == "<":
        if part[idx][0] > value:
            p[idx] = []
            return p, part
        elif part[idx][1] < value:
            part[idx] = []
            return p, part
        else:
            p[idx] = [p[idx][0], value - 1]
            part[idx] = [value, part[idx][1]]
            return p, part
    if op == ">":
        if part[idx][1] < value:
            p[idx] = []
            return p, part
        elif part[idx][0] > value:
            part[idx] = []
            return p, part
        else:
            p[idx] = [value + 1, p[idx][1]]
            part[idx] = [part[idx][0], value]
            return p, part

    return p, part


def apply_rules_ranges(rule_name, part):
    if rule_name == "A":
        return prod(p[1] - p[0] + 1 for p in part)
    elif rule_name == "R":
        return 0
    elif any(len(p) == 0 for p in part):
        return 0

    result = 0

    rule = rules[rule_name]
    stmts = rule.split(",")

    next_rule = stmts[-1]
    for stmt in stmts[:-1]:
        condition, destination = stmt.split(":")
        if "<" in condition:
            condition = condition.split("<")
            idx = lut.index(condition[0])
            p, part = apply_range(part, idx, "<", int(condition[1]))
            result += apply_rules_ranges(destination, p)
        elif ">" in condition:
            condition = condition.split(">")
            idx = lut.index(condition[0])
            p, part = apply_range(part, idx, ">", int(condition[1]))
            result += apply_rules_ranges(destination, p)

    return result + apply_rules_ranges(next_rule, part)


accepted = []
for part in parts:
    if apply_rules("in", part):
        accepted.append(part)

# Part 1
result_1 = sum(sum(a) for a in accepted)
advent.submit_answer(1, result_1)

# Part 2
result_2 = apply_rules_ranges("in", [[1, 4000], [1, 4000], [1, 4000], [1, 4000]])
advent.submit_answer(2, result_2)
