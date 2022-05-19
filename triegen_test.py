#
# Copyright (c) 2022 Andrew Lehmer
#
# Distributed under the MIT License.
#
# triegen_test.py - Tests the equality of compressed and uncompressed
# character-wise trie data structures produced by the triegen module.
#
# WARNING: A valid word list named "word_list.txt" MUST exist in the
# current working directory for these tests to execute correctly.
#

import triegen
import unittest

def get_word_list(
    node: triegen.TrieNode, words: list[str]=[], path: str="") -> list[str]:
  """
  Converts a character-wise trie into a list of strings for each traversal from
  the root to every leaf.
  """
  for key, child in node.items():
    if child:
      get_word_list(child, words, path + key)
    else:
      words.append(path + key)
  return words

class TriegenTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    # Assumes word_list.txt exists in the current working directory
    with open("word_list.txt", 'r') as word_list:
      TriegenTests.words: list[str] = [word.strip() for word in word_list]

  def test_uncompressed(self):
    trie = triegen.generate_trie(TriegenTests.words)
    actual = get_word_list(trie)
    self.assertEqual(set(actual), set(TriegenTests.words))

  def test_compressed(self):
    trie = triegen.generate_trie(TriegenTests.words)
    compressed = triegen.compress_trie(trie)
    actual = get_word_list(compressed)
    self.assertEqual(set(actual), set(TriegenTests.words))

if __name__ == "__main__":
  unittest.main()