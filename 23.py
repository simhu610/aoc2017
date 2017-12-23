
x = open("23").readlines()

I = []

for line in x:
    l = line.split()
    I.append({'instr': l[0], 'reg': l[1]})
    if len(l) == 3:
        I[-1]['val'] = l[2]

print I

regs = [{'p': 0}, {'p': 1}]
for reg in regs:
    reg['a'] = 0
    reg['b'] = 0
    reg['c'] = 0
    reg['d'] = 0
    reg['e'] = 0
    reg['f'] = 0
    reg['g'] = 0
    reg['h'] = 0
pointer = [0, 0]
q = [[], []]
result = [0, 0]

program = 1
locked = [False, False]

num_mul = [0, 0]

history = []

while all([0 <= p < len(I) for p in pointer]):
    # locked = [False, False]
    # for program in [1, 0]:
    for _ in range(1):
        i = I[pointer[program]]
        ii = i['instr']
        ir = i['reg']
        # if ir not in regs[program]:
        #     regs[program][ir] = 0
        assert ir in regs[program] or ii == "jnz", i
        if 'val' in i:
            if i['val'] in regs[program]:
                val = regs[program][i['val']]
            else:
                val = int(i['val'])

        if ii == "snd":
            assert 'val' not in i
            try:
                snd_val = int(ir)
            except:
                snd_val = regs[program][ir]
            print "snd", program, snd_val
            print q
            q[1 - program].append(snd_val)
            print q
            locked[1 - program] = False
            result[program] += 1
        elif ii == "set":
            regs[program][ir] = val
        elif ii == "add":
            regs[program][ir] += val
        elif ii == "sub":
            regs[program][ir] -= val
        elif ii == "mul":
            regs[program][ir] *= val
            num_mul[program] += 1
        elif ii == "mod":
            regs[program][ir] %= val
        elif ii == "rcv":
            assert 'val' not in i
            print "rcv", program, ir
            if len(q[program]):
                print q
                regs[program][ir] = q[program].pop(0)
                print q
            else:
                pointer[program] -= 1
                locked[program] = True
        elif ii == "jgz":
            cond_val = 1 if not ir in regs[program] else regs[program][ir]
            if cond_val > 0:
                pointer[program] += val - 1
        elif ii == "jnz":
            cond_val = 1 if not ir in regs[program] else regs[program][ir]
            if cond_val != 0:
                pointer[program] += val - 1
        else:
            print "unexpected instruction", ir
            assert False

        pointer[program] += 1

        if locked[program]:
            assert I[pointer[program]]['instr'] == 'rcv'

    if all(locked):
        print "deadlock"
        break
    elif locked[0]:
        program = 1
    elif locked[1]:
        program = 0

    import copy
    history.append(copy.deepcopy(regs[program]))

print result
# 130 too low
# 261 too low

print "num_mul", num_mul

print "pointer", pointer, "len(I)", len(I)

# import matplotlib.pyplot as plt
# for reg in regs[program]:
#     plt.clf()
#     plt.plot([h[reg] for h in history])
#     plt.title(reg)
#     plt.show()
