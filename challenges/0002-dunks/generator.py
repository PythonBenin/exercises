from itertools import product
from random import sample, shuffle
from collections import Counter


def pairwise(iterable):
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b

# NBA 75th anniversary team. Fun fact, there are 76 players.
all_players = [
    'Kareem_Abdul_Jabbar',
    'Ray_Allen',
    'Giannis_Antetokounmpo',
    'Carmelo_Anthony',
    'Nate_Archibald',
    'Paul_Arizin',
    'Charles_Barkley',
    'Rick_Barry',
    'Elgin_Baylor',
    'Dave_Bing',
    'Larry_Bird',
    'Kobe_Bryant',
    'Wilt_Chamberlain',
    'Bob_Cousy',
    'Dave_Cowens',
    'Billy_Cunningham',
    'Stephen_Curry',
    'Anthony_Davis',
    'Dave_DeBusschere',
    'Clyde_Drexler',
    'Tim_Duncan',
    'Kevin_Durant',
    'Julius_Erving',
    'Patrick_Ewing',
    'Walt_Frazier',
    'Kevin_Garnett',
    'George_Gervin',
    'Hal_Greer',
    'James_Harden',
    'John_Havlicek',
    'Elvin_Hayes',
    'Allen_Iverson',
    'LeBron_James',
    'Magic_Johnson',
    'Sam_Jones',
    'Michael_Jordan',
    'Jason_Kidd',
    'Kawhi_Leonard',
    'Damian_Lillard',
    'Jerry_Lucas',
    'Karl_Malone',
    'Moses_Malone',
    'Pete_Maravich',
    'Bob_McAdoo',
    'Kevin_McHale',
    'George_Mikan',
    'Reggie_Miller',
    'Earl_Monroe',
    'Steve_Nash',
    'Dirk_Nowitzki',
    'Hakeem_Olajuwon',
    'Shaquille_O_Neal',
    'Robert_Parish',
    'Chris_Paul',
    'Gary_Payton',
    'Bob_Pettit',
    'Paul_Pierce',
    'Scottie_Pippen',
    'Willis_Reed',
    'Oscar_Robertson',
    'David_Robinson',
    'Dennis_Rodman',
    'Bill_Russell',
    'Dolph_Schayes',
    'Bill_Sharman',
    'John_Stockton',
    'Isiah_Thomas',
    'Nate_Thurmond',
    'Wes_Unsel',
    'Dwyane_Wade',
    'Bill_Walton',
    'Jerry_West',
    'Russell_Westbrook',
    'Lenny_Wilkens',
    'Dominique_Wilkins',
    'James_Worthy',
]


def players_in_clips(clips):
    players = set()

    for clip in clips:
        players.update(p for p in clip.split())
    
    return [u for u in players]


def all_possible_clips(players):
    clips = []

    for u, v in filter(lambda t: t[0] != t[1], product(players, repeat=2)):
        clips.append(f'{u} {v}')
    shuffle(clips)

    return clips


def generate_cycle(players, cycle_length):
    assert len(players) >= cycle_length

    clips = []
    selected_players = sample(players, cycle_length)

    for u, v in pairwise(selected_players):
        clips.append(f'{u} {v}')
    clips.append(f'{selected_players[-1]} {selected_players[0]}')

    return clips


def testcase_without_cycle(players, clip_count):
    assert len(players) > clip_count

    clips = []

    for u, v in pairwise(sample(players, clip_count + 1)):
        clips.append(f'{u} {v}')

    return clips


def testcase_with_several_cycles():
    cycle_lengths = [50, 50, 49, 36, 36, 32, 31, 27, 25, 16, 10, 9, 8, 7, 5, 3, 2, 2, 2]
    clip_set = set()
    selected_players = all_players[:60]
    remaining_players = all_players[60:]

    for n in cycle_lengths:
        cycle = generate_cycle(selected_players, n)
        clip_set.update(cycle)

    clip_list = [clip for clip in clip_set]

    # We add clips that won't be in a cycle
    clip_list.extend(clip for clip in testcase_without_cycle(remaining_players, 10))

    shuffle(clip_list)

    return clip_list


print('3')
testcases = [
    testcase_with_several_cycles(),
    testcase_without_cycle(all_players, 50),
    all_possible_clips(sample(all_players, 30))
]
for t in testcases:
    print(len(t))
    print(*t, sep='\n')
