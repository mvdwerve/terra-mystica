import numpy as np
from sys import argv

if __name__ == "__main__":
    # the amount
    n = len(argv[1:])

    # original
    labels = ['Auren', 'Witches', 'Alchemists', 'Darklings', 'Halflings', 'Cultists', 'Engineers',
              'Dwarves', 'Mermaids', 'Swarmlings', 'Chaos Magicians', 'Giants', 'Fakirs', 'Nomads']
    bonus = ['+Priest', '+3 Power | + Worker', '+6c', '+3 Power | +1 Ship', 'Spade Action | + 2c', 'Cult Action | + 4c',
             'Dwelling VP | + 2c', 'Trading Post VP | + Worker', 'Sanctuary / Stronghold VP | +2 Workers']
    round = ['Trading Post VP -> Air Spade', 'Dwelling VP -> Water Priest', 'Trading Post VP -> Water Spade', 'Key VP -> Earth Spade',
             'Sanct/Strong VP -> Air Worker', 'Spade VP -> Earth Coins', 'Dewlling VP -> Fire Power', 'Sanct/Strong VP -> Fire Worker']

    # the cards and sides to choose from
    cards = range(0, 7)
    side = range(0, 2)

    # choose everything
    choices = np.random.choice(cards, n, replace=False)
    sides = np.random.choice(side, n)
    start = np.random.choice(n, 1)[0]
    bonuses = np.random.choice(bonus, n + 3, replace=False)
    rounds = np.random.choice(round, 6, replace=False)

    boem = choices * 2 + sides
    chosen = [labels[i] for i in boem]

    print('===== Generated Results =====')

    for i, v in enumerate(argv[1:]):
        print('%s: %s' % (v, chosen[i]))

    print('\nInitial Starting Player is %s' % argv[start + 1])

    print('\nBonuses (%d / %d)' % (len(bonuses), len(bonus)))
    for v in bonuses:
        print(' - %s' % v)

    print('\nRounds (%d / %d)' % (len(rounds), len(round)))
    for i, v in enumerate(rounds):
        print('%d - %s' % (i + 1, v))
