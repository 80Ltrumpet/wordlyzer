#
# Copyright (c) 2022 Andrew Lehmer
#
# Distributed under the MIT License.
#
# triegen.py - Generates a character-wise trie in JSON format based on a
# user-provided word list.
#

from io import TextIOWrapper
import json
import sys

def generate_trie(word_list: TextIOWrapper):
  """
  Prints a character-wise trie data structure in JSON format to standard output
  based on a line-delimited list of words. Empty leaves are set to false.
  """
  trie = {}
  while line := word_list.readline():
    word = line.strip()
    if len(word) == 0:
      continue
    node = trie
    for letter in word:
      if letter not in node:
        node[letter] = {}
      parent = node
      node = node[letter]
    parent[word[-1]] = False
  json.dump(trie, sys.stdout)

def main():
  """
  Usage: py triegen.py [path-to-word-list]
  """
  if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as word_list:
      generate_trie(word_list)
  else:
    generate_trie(sys.stdin)

if __name__ == "__main__":
  main()