from collections import defaultdict

pipelines = ['A', 'AB', 'D', 'ABC', 'BCDE', 'BCD', 'CDE']
prefix_dict = defaultdict(list)
print(prefix_dict)

# create a map from prefixes to the list of pipelines that share that prefix
for pipeline in pipelines:
    for i in range(1, len(pipeline)+1):
        prefix = pipeline[:i]
        prefix_dict[prefix].append(pipeline)
        # print(prefix, prefix_map)

# print(prefix_dict.keys())
# print(prefix_dict.items())
# find all prefixes that are shared by more than one pipeline
common_prefixes = {p for p, group in prefix_dict.items() if len(group) > 1}
print(common_prefixes)

longest_common_prefixes = set()
for p in common_prefixes:
    if not any(other != p and other.startswith(p) for other in common_prefixes):
        longest_common_prefixes.add(p)

print(longest_common_prefixes)

