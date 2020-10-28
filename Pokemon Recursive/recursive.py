from time import time

pokemons = '''arceus piplup wooloo tyranitar audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite greninja girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''

# Split based on the spacing
pokemon_list = pokemons.split(" ")

# Split all pokemons into an actual dictionary
pokemon_dict = {}
for names in pokemon_list:
    if names[0] not in pokemon_dict:
        pokemon_dict[names[0]] = [names]
    else:
        pokemon_dict[names[0]].append(names)

longest_count = 0
longest_chain = []
iterations = 0

def longest_name(chain):
    global longest_count
    global longest_chain
    global iterations

    iterations += 1

    # Longest checking
    if len(chain) > longest_count:
        longest_count = len(chain)
        longest_chain = chain

    # The code snippet to find the next value in the chain
    if chain[-1][-1] in pokemon_dict:
        for name in pokemon_dict[chain[-1][-1]]:
            if name not in chain:
                longest_name(chain + [name])

# Code to record time
start_time = time()

# Find all the longest name
for names in pokemon_list:
    longest_name([names])

# Print all the stuff
print("took {} iterations!".format(iterations))
print("{} length: {}".format(longest_chain, longest_count))
print("Done! Program took {} seconds to run.".format(time() - start_time))