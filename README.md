# Cpp2Py Compiler

Warning: This project is not yet complete

## Intro
Cpp2Py is a compiler for C++ written in Python. It converts your C++ code into Python programs.
To avoid common errors with Cpp2Py, make sure that the following conditions are satisfied:
1. Each line does not extend for too long. An example of this is:
```cpp
if ((a + b).length() == 5 and . . . . .){
.
.
.
}
```
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
If you are using vscode, then you can delete the .vscode folder

Then install the requirements (rply) with

```
python -m pip install rply
```

Then compile your C++ program with -
```bash
$ python3 __main__.py source.cpp
```
where `source.cpp` is the C++ file you want to compile