
def totalScore(lists, level):
    if lists == 'garbage':
        return 0
    else:
        new_level = level + 1
        return new_level + sum([totalScore(l, new_level) for l in lists])

f = open("9")
s = f.read()
ignore_next = False
is_garbage = False
s2 = ""
noncanceledgarbage = 0
for c in s:
    if ignore_next:
        ignore_next = False
    elif is_garbage:
        if c == '>':
            is_garbage = False
            s2 += "'garbage'"
        elif c == '!':
            ignore_next = True
        else:
            noncanceledgarbage += 1
    elif c == '>':
        assert False
    elif c == '!':
        ignore_next = True
    elif c == '<':
        is_garbage = True
    else:
        s2 += c

print s2

print noncanceledgarbage

lists = eval(s2.replace('{', '[').replace('}', ']'))

print totalScore(lists, 0)