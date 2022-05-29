#!/bin/bash

function print_random_word {
  # The dictionary file. It contains one word per line.
  dictionary=/usr/share/dict/words

  # The number of words in the dictionary file.
  num_words_in_dictionary=$(wc -l $dictionary )

  echo $num_words_in_dictionary
}

print_random_word
