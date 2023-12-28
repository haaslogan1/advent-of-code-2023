# Due to performance, I needed to reference: https://www.reddit.com/r/adventofcode/comments/18b4b0r/comment/kc2v876/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# This is a far better solution as it uses a list of maps

# seeds will contain all the seeds
# maps is the rest of the file except double new lines
seeds, *maps = open('input.txt').read().split('\n\n')
seeds = [int(seed) for seed in seeds.split()[1:]]
# modify maps to be a list of maps containing the three ints
maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]



locations = []
# Iterate through every other seed
for i in range(0, len(seeds), 2):
    # range from the seed number to (seed + next seed)
    ranges = [[seeds[i], seeds[i + 1] + seeds[i]]]
    results = []
    # iterate through the maps list for each map of arrays (dest, src, amt) array
    for _map in maps:
        # Iterate through the two ranges
        while ranges:
            # set start range to the current range (seeds[i])
            # set end range to the current range + the next value (seeds[i + 1] + seeds[i])
            start_range, end_range = ranges.pop()
            # iterate through target, start_map, and r being set to the dest, src, and iteration val
            for target, start_map, r in _map:
				# end of map is the src + iteration
                end_map = start_map + r
                # offset is set to dest - src
                offset = target - start_map
                # no overlap
                if end_map <= start_range or end_range <= start_map:  # no overlap
                    continue
                # seed[i] < ard
                if start_range < start_map:
                	# add [seed[i], src] to ranges
                    ranges.append([start_range, start_map])
                    # set seed[i] = src
                    start_range = start_map
                # check if (src + iteration) < (seed[i] + seed[i + 1])
                if end_map < end_range:
                	# add range [src + iteration, seed[i] + seed[i + 1]]
                    ranges.append([end_map, end_range])
                    # set end_range to src + iteration
                    end_range = end_map
                # append [seeds[i] + dest - src, seeds[i + 1] + seeds[i] + dest - src]
                results.append([start_range + offset, end_range + offset])
                break
            else:
                results.append([start_range, end_range])
        ranges = results
        results = []
    locations += ranges
print(min(loc[0] for loc in locations))