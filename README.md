# Python War Card Game

A console-based implementation of the classic War card game built with Python. The project demonstrates object-oriented programming, core Python fundamentals, data structures, exception handling, game logic, and unit testing.

## Features

* Standard 52-card deck with suits, ranks, and values
* Object-oriented `Card`, `Deck`, and `Player` classes
* Card shuffling and automatic dealing
* Round-based card comparison
* War mechanism for tied cards
* Player hand management
* Game-ending conditions
* Exception handling
* Unit testing with Python's `unittest` framework

## Python Concepts

The project demonstrates:

* Classes and objects
* Instance attributes and methods
* Lists, tuples, and dictionaries
* `for` and `while` loops
* Conditional statements
* Functions
* `try` / `except`
* `isinstance()`
* List operations such as `append()`, `extend()`, and `pop()`
* `__str__()` and `__name__`
* `if __name__ == "__main__"`

## Project Structure

```text
python-war-card-game/
│
├── main.py          # Game classes and game logic
├── test_main.py     # Unit tests
├── .gitignore
└── README.md
```

## Testing

The project uses Python's built-in `unittest` framework to test the `Card`, `Deck`, and `Player` classes and their methods.

Run the tests with:

```bash
python -m unittest discover
```

## Run the Game

```bash
python main.py
```

No external dependencies are required.

## Sample Output

```text
52
Round 1
Round 2
Round 3
Round 4
WAR!
Round 5
Round 6
Round 7
Round 8
...
Round 32
Player two is out of cards
Player one has WON the War!!!
```

*Note: The output and number of rounds vary because the deck is shuffled randomly for each game.*

## Learning Focus

This project demonstrates a strong understanding of Python fundamentals and object-oriented programming (OOP) through practical implementation. It applies classes, objects, data structures, control flow, exception handling, methods, and automated unit testing within a complete working application.
