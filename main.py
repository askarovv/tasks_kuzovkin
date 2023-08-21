import math
from random import randint

def randrange_float(start, stop, step):
    return randint(0, int((stop - start) / step)) * step + start

# Задача №14063
def sine_to_cosine():
    global radians, angle

    def myround(angle):
        if angle / 180 % 10 > 5:
            answer = round(angle / 180)
        else:
            answer = angle // 180 + 0.5
        return answer

    sin = 0.0
    cos = 0.0

    while sin == 0.0 or cos == 0.0:
        angle = randint(0, 360)
        radians = round(angle * math.pi / 180)
        sin = round(math.sin(radians), 1)
        cos = round(math.cos(radians), 1)
        print(angle, radians, sin, cos)

    random_interval_1 = myround(angle)
    random_interval_2 = myround(angle) + 0.5
    if random_interval_1 > random_interval_2:
        random_interval_1, random_interval_2 = random_interval_2, random_interval_1
    angle_1 = random_interval_1 * 180
    angle_2 = random_interval_2 * 180
    radians_1 = randint(radians-2, radians-1)
    radians_2 = randint(radians+1, radians+2)
    angle_3 = randint(angle-30, angle-1)
    angle_4 = randint(angle+1, angle+30)

    print(f"Вычислить sin, если cos = {cos} и a принадлежит [{random_interval_1}pi; {random_interval_2}pi]")
    print(f"Вычислить sin, если cos = {cos} и a принадлежит [{angle_1}^0; {angle_2}^0]")
    print(f"Вычислить sin, если cos = {cos} и a принадлежит [{radians_1}; {radians_2}]")
    print(f"Вычислить sin, если cos = {cos} и a принадлежит [{angle_3}^0; {angle_4}^0]")
    print(f"Ответ: {sin}")


sine_to_cosine()
