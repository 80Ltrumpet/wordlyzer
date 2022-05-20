#
# Copyright (c) 2022 Andrew Lehmer
#
# Distributed under the MIT License.
#
# triegen.py - Generates a compressed character-wise trie in JSON format based
# on a user-provided word list.
#

from collections.abc import Iterable
import json
import sys

TrieNode = dict[str, "TrieNode"]

def generate_trie(words: Iterable[str]) -> TrieNode:
  """
  Creates a character-wise trie data structure based on a line-delimited list
  of words.
  """
  trie = TrieNode()
  for word in words:
    word = word.strip()
    if len(word) == 0:
      continue
    node = trie
    for letter in word:
      if letter not in node:
        node[letter] = TrieNode()
      node = node[letter]
  return trie

def compress_trie_recursive(node: TrieNode) -> tuple[str, TrieNode]:
  """
  Recursively compresses a character-wise trie such that chains of nodes with
  one child are converted into a single node whose key is the ordered
  concatenation of all of the keys in the original chain. Returns a 2-tuple
  containing:
    1. a string representing the chain path originating at the given node
    2. the node at the end of the chain

  If the node argument does not have exactly one child, (1) is the empty
  string (""), and (2) is the original node argument, potentially modified.
  """
  if len(node) == 1:
    letter, child = next(iter(node.items()))
    path, end = compress_trie_recursive(child)
    return letter + path, end
  # Avoid mutation during iteration.
  replacements: dict[str, tuple[str, TrieNode]] = {}
  for letter, child in node.items():
    path, end = compress_trie_recursive(child)
    if path:
      replacements[letter] = (letter + path, end)
  for letter, (path, child) in replacements.items():
    del node[letter]
    node[path] = child
  return "", node

def compress_trie(trie: TrieNode) -> TrieNode:
  """
  Compresses a character-wise trie such that branches consisting of a chain of
  nodes with one or zero children are converted into a leaf node whose key is
  the ordered concatenation of all of the keys in the original chain. Returns
  the root node of the compressed trie.
  """
  compress_trie_recursive(trie)
  return trie

def main():
  """
  Usage: py triegen.py [path-to-word-list]

  Prints a character-wise trie data structure in JSON format to standard output
  based on a line-delimited list of words.
  """
  def trie():
    if len(sys.argv) > 1:
      with open(sys.argv[1], 'r') as word_list:
        return generate_trie(word_list)
    else:
      return generate_trie(sys.stdin)
  json.dump(compress_trie(trie()), sys.stdout)

if __name__ == "__main__":
  main()