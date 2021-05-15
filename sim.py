from random import shuffle, randint, seed

def sim(switch):
    doors = [0, 0, 1]
    shuffle(doors) # Don't actually need to shuffle but whatever
    choice = randint(0, 2)
    index = 0
    # Choose first goat door the player didn't pick
    while not(choice != index and not doors[index]):
        index += 1
    # If switch switch to the only other door
    if switch:
        next = (choice + 1) % 3
        choice = next if index != next else (choice + 2) % 3
    return doors[choice]

TOTAL = 1_000_000
winners_switch = 0
winners_stay = 0

seed(68_71_71_52_76_89_70_69) # For consistency -- remove if you want
for i in range(TOTAL):
    winners_switch += sim(True)
    winners_stay += sim(False)
print(f"Results of {TOTAL:,} trails:\n\t% Won Switching: {winners_switch/TOTAL:.2%}" + 
        f"\n\t% Won Staying: {winners_stay/TOTAL:.2%}")
