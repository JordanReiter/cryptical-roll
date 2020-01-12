# cryptical-roll
[![Build Status](https://travis-ci.com/JordanReiter/cryptical-roll.svg?branch=master)](https://travis-ci.com/JordanReiter/cryptical-roll)
[![Coverage Status](https://coveralls.io/repos/github/JordanReiter/cryptical-roll/badge.svg?branch=master)](https://coveralls.io/github/JordanReiter/cryptical-roll?branch=master)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://raw.githubusercontent.com/JordanReiter/cryptical-roll/master/LICENSE)
[![contributors](https://img.shields.io/github/contributors/JordanReiter/let-me-in.svg?style=flat-square)](https://github.com/JordanReiter/cryptical-roll/graphs/contributors)

The only die-rolling library & command line tool that uses cryptographically strong random numbers for rolling dice.

## Requirements

Python 3.6 or higher.

## Installation

Right now, **cryptical-roll** must be installed from GitHub:

    pip install -e git+git://github.com/JordanReiter/cryptical-roll.git#egg=cryptical-roll

Or clone:

    git clone https://github.com/JordanReiter/cryptical-roll.git
    cd cryptical-roll
    python setup.py install

Installation will install a binary `crypt-roll` which you can call from the command line.

## Usage

### Command line

To make a cryptographically strong dice roll, use the `crypt-roll` command.

#### Basic Usage

    $ crypt-roll 2d6
    9

#### Modifier

    # crypt-roll 2d6+3
    11

#### Multiple rolls
You can roll as many dice combinations as you want:

    # crypt-roll 2d6 4d4 d20 3d8+7
    4 13 3 25

#### Verbosity
You can use `-v` for more verbose output.

    # crypt-roll -v 3d12+3
    Rolling a d12...9
    Rolling a d12...9
    Rolling a d12...11
    Rolled 9 + 9 + 11 = 29 + 3 = 32
    32

### Use in code

You can add cryptographically strong dice rolling to all of your Python-based programs:

    from crypt_roll.utils import CryptRoll
    
    def adventure():
        roller = CryptoRoll()
        strength = input("What is your STR modifier?")
        try:
            strength = int(strength)
        except ValueError:
            raise RuntimeError("Invalid strength")
        dice = [20] # 1d20
        outcome = roller.get_roll_result(dice, modifier=strength)
        if outcome > 10:
            print("You win!")
        else:
            print("Rocks fall, everyone dies.")

## Acknowledgements

Name inspired by [Critical Role](https://critrole.com/), the web series/podcast.
