from random import randint, randrange, random

time = 0

event_number = 0


def add_event(title, text, probability, opens, vulnerability, function=None, one_use=True):
    global d
    global event_number
    event_number += 1
    d[title] = {'n': event_number, 'title': title, 'text': text, 'probability': probability, 'opens': opens,
                'vulnerability': vulnerability, 'function': function, 'one_use': one_use}


def balance_delta_time():
    global delta_time, d
    max_prob = max([d[i]['probability'] for i in active])
    while True:  # fix later
        if max_prob * delta_time > .1:
            delta_time //= 10
        elif max_prob * delta_time < .0001:
            delta_time *= 10
        else:
            return None


def event(index):
    global last_update, active, delta_time
    print(f'{transform(time)} (+{transform(time - last_update)}): {d[active[index]]["text"]}')
    last_update = time
    for new in d[active[index]]['opens']:
        active.append(new)

    f = d[active[index]]['function']

    if d[active[index]]['one_use']:
        done.append(active[index])
        del active[index]

    if f is not None:
        f()

    balance_delta_time()


def GAI():
    if not randrange(100):
        active.append('GAI bad')
    else:
        active.append('GAI good')


done = []
active = ['replecators', 'supernove_explosion']


def destruction(limit):
    global gameOver
    if limit == 1:
        gameOver = True
    global active, done
    for i in range(len(done) - 1, -1, -1):
        if d[done[i]]['vulnerability'] >= limit:
            del done[i]
    for i in range(len(active) - 1, -1, -1):
        if d[active[i]]['vulnerability'] >= limit:
            del active[i]

    for i in done:
        for j in d[i]['opens']:
            if j not in done:
                active.append(j)
    balance_delta_time()


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
add_event('multi-cell',
          'Single-celled organisms unite into increasingly complex colonies. First multicellular organism appeared on the planet',
          10 ** -9, ['smart', 'geotermal'], 3)
add_event('smart', 'Some animal species on the planet are experiencing rapid brain growth. The first tools appear',
          10 ** -8, ['agricultural society'], 4)
add_event('agricultural society',
          'The hunting-gathering lifestyle is being replaced by a sedentary one. Humans start to growing plants and anumals',
          10 ** -6, ['industrial society'], 4)
add_event('industrial society', 'The advent of new technologies allows fewer and fewer people to be involved in food '
                                'production. The first automation systems are being developed',
          10 ** -4, ['post-industrial society'], 5)
add_event('post-industrial society', 'Much of production has been automated, which is why a significant portion of '
                                     'jobs are moving into the service sector',
          3 * 10 ** -3, ['advanced computing', 'Genetic Engineering', 'nuclear energy'], 5)

add_event('advanced computing', 'advanced computing', 10 ** -2, ['super computers'], 6)
add_event('super computers', 'super computers', 10 ** -2, ['AI', 'grey goo'], 6)

add_event('grey goo', 'grey goo apocalypses', 10 ** -3, [], 6, function=lambda: destruction(1))

add_event('AI', 'Self-evolving AI is superior to humans in many tasks, but creating GAI is still impossible',
          2 * 10 ** -2, ['GAI'], 7)
add_event('GAI', 'GAI was created', 10 ** -2, [], 7, function=GAI)
add_event('GAI bad', 'GAI destroys humanity and all life on the planet', 10 ** -2, [], 5, function=lambda: destruction(1))
add_event('GAI good', 'GAI helps civilization achieve incredible levels of efficiency. Production levels are '
                      'experiencing super-exponential growth', 10 ** -2, ['1'], 5)
add_event('1', 'Civilization becomes a civilization of the first type on the Kardashev scale. All available resources '
               'of the planet are used.', 2 * 10 ** -2, [], 5)

add_event('Genetic Engineering', 'Genetic Engineering', 10 ** -2, ['genetic apocalypses'], 6)
add_event('genetic apocalypses', 'genetic apocalypses', 10 ** -3, [], 6, function=lambda: destruction(1))

add_event('nuclear energy', 'nuclear energy', 10 ** -2, ['nuclear apocalypses'], 6)
add_event('nuclear apocalypses', 'nuclear apocalypses', 10 ** -3, [], 5, function=lambda: destruction(4))

add_event('supernove_explosion', 'A supernova explosion destroys all complex life on the planet ', 2 * 10 ** -12, [], 0,
          function=lambda: destruction(3))
add_event('geotermal', 'sudden rise in geothermal activity causes mass extinction', 5 * 10 ** -9, [], 4, one_use=False,
          function=lambda: destruction(4))

delta_time = 10 ** 7

last_update = 0

star_lifetime = randrange(5 * 10 ** 9, 20 * 10 ** 9)

gameOver = False

while time < star_lifetime and not gameOver:
    time += delta_time
    if len(active) < 2:
        print(len(active), active, delta_time)
        break
    for i in range(len(active) - 1, -1, -1):
        if random() < (d[active[i]]['probability'] * delta_time):
            event(i)
            break
