# Cpp2Py Compiler

Warning: This project is not yet complete. If you like, you can fork or clone this repository and work on it.
You can also open an issue if you want a feature to be added as soon as possible.
(NOTE: The author of this repository is currently busy with ongoing exams, and hopes to be back on track by March 2021)

## Features of Cpp2Py Compiler
Watch this space to be notified of new updates.

- `cout`s and `cin`s

## Intro
Cpp2Py is a compiler for C++ written in Python. It converts your C++ code into Python programs.
To avoid common errors with Cpp2Py, make sure that the following conditions are satisfied:
1. Each line does not extend for too long. An example of this is:
```cpp
cout << "Hello " << name << "!! Welcome to C++!" << endl;
```
This should be converted to:
```cpp
cout << "Hello ";
cout << name;
cout << "!! Welcome to C++!";
cout << endl;
```
This issue should be fixed in future releases!

2. You must convert the dependencies of the file separately, except for
```cpp
#include "iostream"
```
3. Some methods in C++ do not exist in Python. The Cpp2Py compiler will try to define those methods in the output Python file, but it is best if you do it manually in order to avoid mistakes.

## Usage

First download the repository from Github using

```git
git clone <repository>
```

Then install the requirements (rply) with

```
python -m pip install rply
```

Then compile your C++ program with -
```bash
$ python3 __main__.py source.cpp
```
where `source.cpp` is the C++ file you want to compile