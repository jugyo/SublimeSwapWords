SwapWords
========

It provides a command `swap_words` to swap words by regexp (default is `'\s*[\s,\|&]+\s*'`).

## Installation

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
$ git clone https://github.com/jugyo/SublimeSwapWords.git SwapWords
```

## Usage

The `swap_words` command is binded to `Command + k, Command + s`.

## Customize

In your Preferences.sublime-settings:

```
{
  "swap_words_pattern": '\s*[\s,\|&]+\s*'
}
```
