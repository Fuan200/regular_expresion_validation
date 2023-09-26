# Regular Expression Validation

This repository contains a Python script is designed to help you verify regular expressions (regex). 

## Table of Contents

- [Programming_Language](#programming-language)
- [OS](#os)
- [Author](#author)
- [Requirements](#requirements)
- [Description](#description)
- [Usage](#usage)
- [Example](#example)

## Programming Language

Python 3.11.4

## OS 

GNU/Linux

Kali Linux 6.1.0

## Author

**Juan Díaz** 

* Personal [Github](https://github.com/Fuan200/) 

* School [Github](https://github.com/JuanDiazuwu)

## Requirements

 * Any distribution to unix.

 * Python 3 of higher.

 * subprocess library (included in the Python standard library).

## Description

This is a sequence of characters that specifies a match pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation. Regular expression techniques are developed in theoretical computer science and formal language theory.
Regular expressions are versatile and can be used for various text-processing tasks, including:

 * 1.- Searching: You can use regular expressions to search for specific patterns within a text string. For example, finding email addresses, phone numbers, or URLs in a document.

 * 2.- Validation: Regular expressions are commonly employed to validate input data. For instance, you can use a regex pattern to ensure that an entered email address follows a valid format.

 * 3.- Text Extraction: You can extract specific information from a text using regular expressions. For example, extracting all mentions of hashtags from a tweet or extracting dates from a document.

 * 4.- Text Transformation: Regular expressions can help you replace or modify text based on specific patterns. For instance, you can use regex to remove all non-alphanumeric characters from a string.

Here are a few examples of common regular expressions:

 * `.`: Matches any character except a newline.

 * `*`: Matches zero or more occurrences of the preceding character or group.

 * `+`: Matches one or more occurrences of the preceding character or group.

 * `?`: Matches zero or one occurrence of the preceding character or group.

 * `[]`: Defines a character class, allowing you to match any character from the specified set.

 * `|`: Acts as an OR operator, allowing you to match multiple patterns.

On the code the function `get_expression` and `get_word` are for obtain the expression and the word we want to check if it is accepted by the expression.

Later there is the function `format_terminal`, it receives as parameters the expression and word given by the user, and formats the text and then put it in the terminal.

The function `write_terminal` receive sthe ready text (command), and runs it in the terminal. It then returns the result of running the command

The function `validation` receives the result from the previous function and if it is 0 it means that the word does belong to that expression, on the other hand if it is 1 it does not belong.

Finally, the `main` calls the function `get_expression`, and the do a cycle to validate if the words given by the user belong to the expression.

## Usage

1. Clone the repository:

```
    $ git clone git@github.com:Fuan200/regular_expression_validation.git
```

2. Open the repository.

3. Run the script:

```
    $ python regular_expression.py
```

4. Type the expression.

5. Type the word or words that want verify.

6. If you want to finish the execution of the program, type `Ctrl + C`.

## Example

`[0-9]*`: This expression accepts strings of lenght 0 or infinite to positive integers (0, 1, 2, 3, ..., n).

On the step four you need to type first the expression and next the word:

Expression:

```
[0-9]*
```

Word:

```
69
```

Output: 

```
Yes!!!! The word 69 is on the expression: [0-9]+ 
```

Feel free to clone the repository and test it working.
I hope you find it useful!!!