import sys

from suffix_tree import SuffixTree

with open("test.txt") as f:
    st = SuffixTree(f.read(), case_insensitive=True)

print(st.find_word_by_prefix(sys.argv[1]))
