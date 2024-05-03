from random import randint, randrange, random

time = 0

event_number = 0


def add_event(title, text, probability, opens, one_use=True):
    global d
    global event_number
    event_number += 1
    d[title] = {'n': event_number, 'title': title, 'text': text, 'probability': probability, 'opens': opens, 'one_use': one_use}


def transform(x):
    if x > 10 ** 9:
        return f'{round(x / 10 ** 9, 1)}B'
    if x > 10 ** 6:
        return f'{round(x / 10 ** 6, 1)}M'
    if x > 1000:
        return f'{round(x / 1000, 1)}K'


d = {}
add_event('replecators', 'first self-replecating molecules appears on the planet', 10 ** -9, ['one-cell'])
add_event('one-cell', 'first single-celled organisms appeared on the planet', 10 ** -9, ['multi-cell'])
add_event('multi-cell', 'Single-celled organisms unite into increasingly complex colonies. First multicellular organism appeared on the planet', 10 ** -9, ['smart'])
add_event('smart', 'Some animal species on the planet are experiencing rapid brain growth. The first tools appear', 10 ** -8, ['agricultural society'])
add_event('agricultural society', 'The hunting-gathering lifestyle is being replaced by a sedentary one. Humans start to growing plants and anumals', 10 ** -6, [])
add_event('supernove_explosion', 'A supernova explosion destroys all life on the planet ', 10 ** -11, [])

active = ['replecators', 'supernove_explosion']

delta_time = 10 ** 7

last_update = 0

star_lifetime = randrange(5 * 10 ** 9, 20 ** 9)

while time < star_lifetime:
    time += delta_time
    for i in range(len(active) - 1, -1, -1):
        if random() < (d[active[i]]['probability'] * delta_time):
            print(f'{transform(time)} (+{transform(time - last_update)}): {d[active[i]]["text"]}')
            last_update = time
            for new in d[active[i]]['opens']:
                active.append(new)
                max_prob = max([d[i]['probability'] for i in d])
                if max_prob * delta_time > .1:
                    delta_time //= 10
                if max_prob * delta_time < .0001:
                    delta_time *= 10
            if d[active[i]]['one_use']:
                del active[i]
