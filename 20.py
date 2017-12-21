import numpy as np

def get_values(str, i):
    return [int(x) for x in str[i].strip()[3:-1].split(',')]


x = open("20").readlines()

particles = []

for line in x:
    pva = line.split(', ')
    p = get_values(pva, 0)
    v = get_values(pva, 1)
    a = get_values(pva, 2)
    particles.append({'p': p, 'v': v, 'a': a, 'i': len(particles)})

i = np.argmin([sum([abs(an) for an in particle['a']]) for particle in particles])
print i, particles[i]

# detected_collisions = [521, 520, 519, 517, 516, 515, 514, 513, 512, 510, 509, 508, 507, 506, 505, 504, 502, 500, 499, 498, 497, 495, 494, 493, 492, 491, 490, 489, 487, 486, 485, 484, 483, 481, 480, 479, 478, 477, 476, 475, 473, 471, 470, 469, 468, 467, 466, 465, 464, 462, 460, 458, 457, 456, 455, 454, 453, 452, 450, 449, 447, 445, 444, 443, 442, 441, 440, 438, 437, 436, 435, 433, 432, 430, 429, 427, 426, 425, 424, 423, 422, 421, 420, 419, 417, 416, 414, 413, 412, 411, 410, 409, 407, 406, 405, 404, 403, 402, 401, 399, 398, 396, 395, 394, 393, 392, 391, 389, 388, 386, 385, 384, 382, 380, 379, 378, 377, 375, 374, 372, 371, 370, 369, 368, 367, 366, 365, 364, 362, 361, 360, 359, 358, 357, 355, 354, 353, 352, 350, 349, 348, 346, 345, 344, 342, 341, 340, 339, 338, 337, 336, 334, 333, 332, 330, 329, 328, 327, 326, 325, 324, 323, 322, 320, 319, 318, 317, 316, 315, 313, 312, 311, 310, 309, 307, 305, 303, 302, 300, 299, 298, 297, 296, 295, 294, 293, 292, 290, 289, 288, 287, 286, 285, 284, 283, 282, 280, 279, 278, 277, 275, 273, 272, 271, 270, 269, 268, 266, 265, 264, 263, 262, 260, 259, 258, 257, 256, 254, 253, 252, 250, 249, 247, 246, 245, 244, 243, 242, 241, 240, 238, 236, 234, 233, 232, 230, 229, 228, 226, 225, 224, 223, 222, 221, 219, 218, 217, 216, 215, 214, 212, 211, 210, 209, 208, 207, 206, 205, 203, 201, 199, 198, 197, 196, 194, 193, 192, 191, 190, 189, 188, 186, 185, 184, 183, 182, 180, 179, 178, 176, 175, 174, 173, 172, 171, 170, 169, 168, 166, 164, 163, 162, 160, 159, 158, 156, 154, 153, 151, 150, 149, 148, 146, 144, 143, 142, 140, 139, 138, 137, 136, 135, 133, 132, 130, 129, 128, 127, 126, 125, 124, 122, 121, 120, 119, 118, 117, 116, 115, 113, 112, 111, 110, 109, 108, 106, 105, 104, 103, 102, 101, 100, 99, 97, 96, 95, 94, 92, 91, 90, 89, 88, 87, 86, 85, 83, 82, 81, 80, 79, 78, 77, 75, 74, 73, 71, 70, 69, 68, 67, 66, 65, 63, 61, 60, 59, 58, 57, 56, 55, 54, 52, 51, 50, 49, 47, 46, 44, 43, 42, 41, 40, 39, 38, 37, 36, 34, 33, 32, 31, 30, 29, 28, 27, 26, 24, 23, 22, 21, 20, 18, 17, 16, 14, 12, 11, 10, 9, 8, 7, 6, 4, 3, 2, 1, 0]
# for d in detected_collisions:
#     particles.pop(d)

t = 0

popped_i = []

while len(particles):
    for particle in particles:
        particle['v'] = [particle['v'][i] + particle['a'][i] for i in range(3)]
        particle['p'] = [particle['p'][i] + particle['v'][i] for i in range(3)]
    # collisions = set([])
    collisions = []
    for i, particle in enumerate(particles):
        for j, particle2 in enumerate(particles[i + 1:]):
            if particle['p'] == particle2['p']:
                # collisions.add(i)
                # collisions.add(i + j)
                collisions.append(i)
                collisions.append(i + 1 + j)
                # print i, i+1+j
                # print particle, particle2
    collisions = sorted(set(collisions))
    # print collisions
    # assert not len(collisions)
    p1 = len(particles)
    c1 = len(collisions)
    while len(collisions):
        popped = particles.pop(collisions.pop(0))
        popped_i.append(popped['i'])
        collisions = [c - 1 for c in collisions]
    assert len(particles) == p1 - c1
    t += 1
    print t, len(particles)

    # if len(particles) == 574:
    #     print sorted(popped_i, reverse=True)
    #     break

# 574 is too high
# 322 too low
# could maybe calc which pairs will never collide and see if any of the 574 could actually collide