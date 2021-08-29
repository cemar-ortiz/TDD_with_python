# About this project

This is a repository I worked with as a means to review the practice of Test Driven Development (TDD)

In this repo it is covered with examples written in Python but TDD is a general practice to programming, you can do TDD in technically any language. 

These examples were taken from [this Rubik's Code blogpost](https://rubikscode.net/2021/05/24/test-driven-development-tdd-with-python/) which I encourage you to read along with cloning this repo. It may help you study the subject if you stumbled upon this project wanting to do so.

I added comments and some slight variations on some of them as the blogpost includes exercises I tried to solve on my own first before looking at the posted solution.

I hope you may find this project useful for your interests.

## Installation

Ready to clone and use. If you have already a working python installation, it comes with the module `unittest` built-in which is what is used for designing and running the testing cases.

Normally, it's also good practice to setup a virtual environment and install other requirements, but this is a very simple project where any typical python installation will do.

```
$ git clone 
```

The layout of the tests and modules is made so you can run the tests on a terminal using:

```
# You can run a full test module
$ python -m unittest tests.<test_module>
```
```
# Or even a single test method
$ python -m unittest tests.<test_module>.<test_method>
```
```
# To run all tests (modules or packages named as test*.py)
python -m unittest discover
# Also works without discover for Python 3, which is neat
python3 -m unittest
```

I got this review on how to run tests using the unittest module from an answer on [this question](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure) at Stack Overflow.

