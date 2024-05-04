from random import randint, randrange, random

time = 0

event_number = 0


def add_event(title, text, probability, opens, vulnerability, function=None, one_use=True):
    global d
    global event_number
    event_number += 1
    d[title] = {'n': event_number, 'title': title, 'text': text, 'probability': probability, 'opens': opens,
                'vulnerability': vulnerability, 'one_use': one_use}
    if function is not None:
        function()


def GAI():
    pass


def transform(x):
    if x > 10 ** 9:
        return f'{round(x / 10 ** 9, 1)}B'
    if x > 10 ** 6:
        return f'{round(x / 10 ** 6, 1)}M'
    if x > 1000:
        return f'{round(x / 1000, 1)}K'
    return str(x)


d = {}
add_event('replecators', 'first self-replecating molecules appears on the planet', 10 ** -9, ['one-cell'], 1)
add_event('one-cell', 'first single-celled organisms appeared on the planet', 10 ** -9, ['multi-cell'], 2)
add_event('multi-cell', 'Single-celled organisms unite into increasingly complex colonies. First multicellular organism appeared on the planet', 10 ** -9, ['smart'], 3)
add_event('smart', 'Some animal species on the planet are experiencing rapid brain growth. The first tools appear', 10 ** -8, ['agricultural society'], 4)
add_event('agricultural society', 'The hunting-gathering lifestyle is being replaced by a sedentary one. Humans start to growing plants and anumals', 10 ** -6, ['industrial society'], 4)
add_event('industrial society', 'The advent of new technologies allows fewer and fewer people to be involved in food production. The first automation systems are being developed', 10 ** -4, ['post-industrial society'], 5)
add_event('post-industrial society', 'Much of production has been automated, which is why a significant portion of jobs are moving into the service sector', 3 * 10 ** -3, ['advanced computing', 'Genetic Engineering', 'nuclear energy'], 5)

add_event('advanced computing', 'advanced computing', 10 ** -2, ['super computers'], 6)
add_event('super computers', 'super computers', 2 * 10 ** -2, ['AI'], 6)
add_event('AI', 'Self-evolving AI is superior to humans in many tasks, but creating GAI is still impossible', 2 * 10 ** -2, ['GAI'], 7)
add_event('GAI', 'GAI was created', 2 * 10 ** -2, [], 3, function=GAI)

add_event('Genetic Engineering', 'Genetic Engineering', 10 ** -2, [], 6)
add_event('nuclear energy', 'nuclear energy', 10 ** -2, [], 6)

add_event('supernove_explosion', 'A supernova explosion destroys all life on the planet ', 10 ** -11, [], None)

done = []
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
                done.append(active[i])
                del active[i]
