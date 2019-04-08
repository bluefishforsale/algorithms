#!env python2
from pprint import pprint
from random import shuffle as r_shuffle
from random import randint
import sys
import dis

MAX = 2**64

PRIMES = [
    179424691, 179425033, 179425601, 179426083, 179424697, 179425063, 179425619, 179426089,
    179424719, 179425069, 179425637, 179426111, 179424731, 179425097, 179425657, 179426123,
    179424743, 179425133, 179425661, 179426129, 179424779, 179425153, 179425693, 179426141,
    179424787, 179425171, 179425699, 179426167, 179424793, 179425177, 179425709, 179426173,
    179424797, 179425237, 179425711, 179426183, 179424799, 179425261, 179425777, 179426231,
    179424821, 179425319, 179425811, 179426239, 179424871, 179425331, 179425817, 179426263,
    179424887, 179425357, 179425819, 179426321, 179424893, 179425373, 179425823, 179426323,
    179424899, 179425399, 179425849, 179426333, 179424907, 179425403, 179425859, 179426339,
    179424911, 179425423, 179425867, 179426341, 179424929, 179425447, 179425879, 179426353,
    179424937, 179425453, 179425889, 179426363, 179424941, 179425457, 179425907, 179426369,
    179424977, 179425517, 179425943, 179426407, 179424989, 179425529, 179425993, 179426447,
    179425003, 179425537, 179426003, 179426453, 179425019, 179425559, 179426029, 179426491,
    179425027, 179425579, 179426081, 179426549 ]

def yes_no(answer):
    yes = set(['yes','y', 'ye'])
    no = set(['no','n', ''])

    while True:
        choice = raw_input(answer).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
           print "Please respond with 'yes' or 'no'\n"

def listsum(numList):
    C = 500                              # max list len  we try and recurse down
    if len(numList) == 1:
        return numList[0]
    else:
        if len(numList) > C:                      # we have to recurse in chunks
            subSum = 0
            parts = len(numList) / C                 # how many times we iterate
            for x in range(0, len(numList), C):
                subSum = subSum + listsum(numList[x:x+C])      # iterate and add
            return subSum
        else:
            return numList[0] + listsum(numList[1:])

def listcount(numList):
    c = {}
    if len(numList) == 1:
        return numList[0]
    else:
        for i in numList:
            c[i] = numList.count(i)
        return c


def str2ord(word):
    string_as_ords = [ ord(x) for x in word ]
    return string_as_ords

def ord2str(ordlist):
    ords_as_string = "".join( [ chr(x) for x in ordlist ] )
    return ords_as_string

def shuffle(word):
    r_shuffle(t_word)
    return t_word

def combinate_words(word):
    combinated_words = [word]
    for i in range(1, len(word)**2):
        ords = str2ord(word)
        r_shuffle(ords)
        string = ord2str(ords)
        combinated_words.append(string)
    return list(set(combinated_words))

def hashme(lit):
    # t_prime = a special large number this word maps to
    ords = str2ord(lit)
    sum = listsum(ords)
    t_prime = PRIMES[ (ord(lit[-1]) * PRIMES[0]) % len(PRIMES) ]**2
    total = (sum * (t_prime)) % MAX
    rt_string =  "{:20s} => {:10d} * {:d} % {:d} =  {:022d}".format(
                  lit,      sum,     t_prime,  MAX,    total
    )  #22 is 1 more than the mod value length
    return "{:022d}".format(total)



def main(TEST_DATA):
    total_words = []

    # format
    # key = hash
    # value = word
    hashes = {}
    for word in TEST_DATA:
        for wordlet in combinate_words(word):
            total_words.append(wordlet)
            hash=hashme(wordlet)
            if not hashes.has_key(hash):
                hashes[hash] = [ wordlet ]
            else:
                hashes[hash].append(wordlet)

    # totals

    print("Started with: {} words".format(len(TEST_DATA)))
    print("Scrambled into: {} words total".format(len(total_words)))

    # let's see how much we reduced it to
    print("Sorted into : {} hash buckets".format(len(hashes)))

    # count by hand to ensure we actually stored them
    counts = [ len(x) for x in hashes.values() ]
    print("Crawled : {} total values at the end".format(listsum(counts)))

    if yes_no("Would you like to see the 1st summary? (shrt) [y/N] "):
        # summary counts of distribution
        pprint( [ "{1:} buckets with {0:} items".format(x,y) for x,y in listcount(counts).iteritems() ] )

    if yes_no("Would you like to see a histogram? (SHORT) [y/N] "):
        groups = [ "{:d}".format( x*y ) for x,y in listcount(counts).iteritems() ]
        SCREEN_W=120
        SCREEN_H=40
        for R in range(0, SCREEN_H):
            for C in range(0, len(groups)-1):
                if groups[C] >= (SCREEN_H - C):
                    print('*'),
                else:
                    print(' '),
            print('\n'),


    if yes_no("Would you like to see ALL the hashes? (LONG) [y/N] "):
        pprint(hashes)

if __name__ == '__main__':
    # just in case test data
    TEST_DATA = [
        'terrac',
        'abc',
        'a really long phrase with spaces',
    ]


    if len(sys.argv) >= 2:
        TEST_DATA = sys.argv[1:]

    main(TEST_DATA)

    if yes_no("Would you like to see the x86_64 ASM code? (LONG) [y/N] "):
        dis.dis(main)
