[![Build Status](https://travis-ci.org/adrielklein/anagram-server.svg?branch=master)](https://travis-ci.org/adrielklein/anagram-server)

## Welcome to AnagramServer
AnagramServer is a web server that finds anagrams of words. Not only that, but it provides an API to load words into the data store, remove them, and even show some cool statistics about the words themselves.


## Routes
- `GET /`: Returns "OK". Useful for testing.
- `POST /words.json`: Takes a JSON array of words and adds them to the corpus (data store).
- `GET /anagrams/:word.json`:
  - Returns a JSON array words that are anagrams of the word passed in the URL.
  - Supports an optional query param that indicates the maximum number of results to return.
- `DELETE /words/:word.json`: Deletes a single word from the data store.
- `DELETE /words.json`: Deletes all contents of the data store.
- `GET /stats`:  Returns a JSON object specifying the count of words in the corpus and min/max/median/average word length
- `GET /most`: Returns a JSON object that identifies alphagrams with the most anagrams in the corpus

## How to start the server
1. Download and install [Python 3.5](https://www.python.org/downloads/release/python-350/)
1. Clone this repository to your machine
1. Open a terminal and change into the root of the repository
1. Install virtualenv `pip install virtualenv`
1. Create a virtual environment `virtualenv venv`
1. Activate the virtual environment `source venv/bin/activate`
1. Install Dependencies `pip install -r requirements.txt`
1. Run `python start_server.py`

## How to run the tests
- Run `python scripts/run_tests.py`

## How to add the English dictionary to the corpus
1. Make sure the server is running
1. Run `scrips/populate_corpus.py`

## Implementation Details

The server is written in Python and uses [Flask](http://flask.pocoo.org/) as a web framework.

The data store is an in-memory hash table where the key is an [alphagram](https://en.wikipedia.org/wiki/Alphagram) and the value is a set of words that map to that alphagram.

For example, the alphagram "dgo" maps to a set containing the words "dog" and "god".

The hash table makes anagram lookups easy. To find an anagram for a word the server simply finds its alphagram, looks it up in the hash table, and returns the corresponding set.
