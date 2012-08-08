source: "http://github.com/nathanrosspowell/nathanrosspowell.github.com/blob/dev/website/pages/blog/2012/08/07/project-euler.md"
named: "project-euler"
title: "Project Euler"
published: "2012/08/07"
time: "21:26:35"
w3c: "2012-08-07T21:26:35+00:00"
url: "blog/2012/08/07/project-euler"
template: "blog_post.html"
comments: True
short: "An update to the compilers used in my Project Euler testbed"
tags:
- blog
- "project-euler"
- c++
- bash
- linux

I've just update the test code for my [Project Euler][pe] testing scripts. Now a list of `Execute` classes will run on each language implementation. I've started by adding Clang to the GCC tests.

<a href="http://imgur.com/WOllJ"><img class="article" src="http://i.imgur.com/WOllJ.png" alt="" title="run.py working it's magic on CPP 2 and 12" /></a>

Also I stopped the nasty red *ERROR* messages for files that exist when there is an answer for that problem, but it's not finished in a specific language (problem 11 is only sloved in `python` currently).

Time to get cracking on the next problem, currently [PE16][pe16]

[pe]: http://github.com/nathanrosspowell/euler "Project Euler on GitHub"
[pe16]: http://projecteuler.net/problem=16 "Project Euler problem 16"
