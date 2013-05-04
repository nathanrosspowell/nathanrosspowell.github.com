title: "Project Euler"
published: True
date: "2012-08-07T21:26:35+00:00"
comments: True
short: "An update to the compilers used in my Project Euler testbed"
tags:
- project-euler
- c++
- bash
- linux

I've just update the test code for my [Project Euler][pe] testing scripts. Now a list of `Execute` classes will run on each language implementation. I've started by adding Clang to the GCC tests.

<a href="http://imgur.com/WOllJ"><img class="article" src="http://i.imgur.com/WOllJ.png" alt="" title="run.py working it's magic on CPP 2 and 11" /></a>

Also I stopped the nasty red *ERROR* messages for files that exist when there is an answer for that problem, but it's not finished in a specific language (problem 11 is only sloved in `python` currently).

Time to get cracking on the next problem, currently [PE15][pe15] (I've got up to PE16, but only after I chickened out on PE15...)

See my `code` page [here][nrppe].

[pe]: http://github.com/nathanrosspowell/euler "Project Euler on GitHub"
[pe15]: http://projecteuler.net/problem=15 "Project Euler problem 15"
[nrppe]:http://nathanrosspowell.com/code/project-euler "NRP - Code - Project Euler" 
