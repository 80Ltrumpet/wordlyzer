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

from typing import Optional
import triegen
import unittest

def get_word_list(
    node: triegen.TrieNode, path: str="", words: Optional[list[str]]=None):
  """
  Returns a list of strings obtained from a depth-first traversal of a trie.
  """
  if words is None:
    words = []
  for key, child in node.items():
    if child:
      get_word_list(child, path + key, words)
    else:
      words.append(path + key)
  return words

class TriegenTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    # Assumes word_list.txt exists in the current working directory
    with open("word_list.txt", 'r') as word_list:
      TriegenTests.words: set[str] = set(word.strip() for word in word_list)

  def test_uncompressed(self):
    trie = triegen.generate_trie(TriegenTests.words)
    actual = get_word_list(trie)
    self.assertEqual(len(actual), len(TriegenTests.words))
    self.assertEqual(set(actual), TriegenTests.words)

  def test_compressed(self):
    trie = triegen.generate_trie(TriegenTests.words)
    compressed = triegen.compress_trie(trie)
    actual = get_word_list(compressed)
    self.assertEqual(len(actual), len(TriegenTests.words))
    self.assertEqual(set(actual), TriegenTests.words)

if __name__ == "__main__":
  unittest.main()