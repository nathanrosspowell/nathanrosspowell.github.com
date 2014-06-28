[nathanrosspowell.github.com][homepage]
===========

What is it?
-----------

This is my personal website which is made using the [Python][python] based [Flask][flask] web framework which.


What is it made of?
-------------------

The target platform for my website is [GitHub Pages][ghpages] so I decided to use the [Frozen Flask][frozenflask] static site generator.
I take full advantage of [Twitter Bootstrap][bootstrap] to make sure the website is view-able from all devices.
To deploy the website, the generated `build` folder needs to be copied to the `master` branch (the target for a non-user [GitHub Pages][ghpages] site is `gh-pages`).
This is trivialized with the [Grunt.js][grunt] module [grunt-gh-pages][grunt-gh-pages].
There are a few other [Grunt.js][grunt] modules that are used to tidy up the source of the static site.


How to use it?
--------------

To install all of the needed software, run `install.bash`.
Please review this script before executing it on your machine.

Once you have the source, open a terminal and run `python runserver.py`.
Open your web browser and navigate to `http://localhost:5000/`.

Finally, if you have any changes that need to be committed, use the script `bash deploy.bash "My commit message"` to push everything to the branch and deploy the website to [GitHub Pages][ghpages].

[homepage]: http://nathanrospowell.github.io
[python]: https://www.python.org/
[flask]: http://flask.pocoo.org/
[ghpages]: https://pages.github.com/
[frozenflask]: https://pythonhosted.org/Frozen-Flask/
[bootstrap]: http://getbootstrap.com/
[grunt]: http://gruntjs.com/
[grunt-gh-pages]: https://github.com/tschaub/grunt-gh-pages

