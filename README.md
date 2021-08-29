# About this project

This is a repository I worked with as a means to review the practice of Test Driven Development (TDD). TDD is a way of approaching solution design with programming by first writing tests that represent our user stories and then trying to write the minimal piece of code which satisfies our tests. 

That's the gist of the concept, it's a very powerful thing, makes you be more efficient by helping you focus and procrastinate less.

In this review we cover a TDD introduction with examples written in Python but it is a general practice to programming, you can do TDD in technically any language. 

These examples were taken from [this Rubik's Code blogpost](https://rubikscode.net/2021/05/24/test-driven-development-tdd-with-python/) which is a must to read along with cloning this repo. It may help you study the subject if you stumbled upon this project wanting to do so.

I added comments and some slight variations on some of them as the blogpost includes exercises I tried to solve on my own first before looking at the posted solution.

I hope you may find this project useful for your interests.

## Installation

Ready to clone and use. If you have already a working python installation, it comes with the module `unittest` built-in which is what is used for designing and running the testing cases.

Normally, it's also good practice to setup a virtual environment and install other requirements, but this is a very simple project where any typical python installation will do.

```
git clone https://github.com/cemar-ortiz/TDD_with_python
```

The layout of the tests and modules is made so you can run the tests on a terminal using:

```
# You can run a full test module
python -m unittest tests.<test_module>
```
```
# Or even a single test method
python -m unittest tests.<test_module>.<test_method>
```
```
# To run all tests (modules or packages named as test*.py)
python -m unittest discover
# Also works without discover for Python 3, which is neat
python3 -m unittest
```

I got this review on how to run tests using the unittest module from an answer on [this question](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure) at Stack Overflow.

