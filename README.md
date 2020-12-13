# Cpp2Py Compiler

Warning: This project is not yet complete. If you like, you can fork or clone this repository and work on it.
You can also open an issue if you want a feature to be added as soon as possible. This project is not yet ready for distribution, it is currently written to serve testing purposes. If you wish to use it right now, you may need to tweak some of the code.
(NOTE: The author of this repository is currently busy with ongoing exams, and hopes to be back on track by March 2021)

## Intro
Cpp2Py is a compiler for C++ written in Python. It converts your C++ code into Python programs.
To avoid common errors with Cpp2Py, make sure that the following conditions are satisfied:
1. There is only one command in each line of code. Example:
```cpp
int main(){cout << "Enter your name: "; string a; cin >> a; cout << "Hello " << a << endl; return 0;}
```
should be converted to -
```cpp
int main(){
	cout << "Enter your name: ";
	string a;
	cin >> a;
	cout << "Hello" << a << endl;
	return 0;
}
```

2. All comments are removed. 
This issue should be fixed in future releases!

3. You have already converted the dependencies of the file separately, except for
```cpp
#include "iostream"
```
4. Some methods in C++ do not exist in Python. The Cpp2Py compiler will try to define those methods in the output Python file, but it is best if you do it manually in order to avoid mistakes.

## Features of Cpp2Py Compiler
Watch this space to be notified of new updates.

- `cout`s and `cin`s
- Comments (shorter than 5 words. Example: `# This code does nothing`) (Hope to fix it in future releases!)
- Defining and calling functions without parameters or returns ;-)

## Usage

First clone the repository from Github using
```bash
$ git clone https://github.com/classPythonAddike/Cpp2Py.git
```

Then install the requirements (rply) with
```bash
$ python -m pip install rply
```

Then compile your C++ program with -
```bash
$ python3 __main__.py source.cpp
```
where `source.cpp` is the C++ file you want to compile