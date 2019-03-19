Frequently asked questions
==========================

When logging to tmc first time, whats the server address it asks?
-----------------------------------------------------------------

Your TMC client is old, load newest version from
`tmc-cli <https://github.com/testmycode/tmc-cli>`_

tmc not found
-------------

You installed the TMC client successfully, but the program is not
found when you say `tmc` in the command prompt.
If you are using Windows, use the `doskey` program so that tmc
can be found even if you are not in the same folder as the `tmc`
executable. For instructions, see `tmc-cli <https://github.com/testmycode/tmc-cli>`_.

If you are using Linux, then you may have close the terminal window
and open a new one. Or alternatively, run `source ~/.bashrc`.

`tmc test` says: "Test results: 0/0 tests passed"
-------------------------------------------------

If the output is
Test results: 0/0 tests passed
All tests passed! Submit to server with 'tmc submit'
Then several things can be wrong.

First make sure that the program run correctly, e.g.
`python3 src/hello_world.py`.
If it crashes, then `tmc` will most likely give the above message.

If the program does not crash, you are using Windows, and you
have installed Anaconda, then possibly TMC cannot find Anaconda installation.
Make sure you use TMC version at least 0.9.2. You can check the
version of TMC with `tmc --version`.

What version of Python should I use? What is the name of the executable?
------------------------------------------------------------------------

The Python version should be at least 3.6. You can check your version with
`python3 --version` on Linux or macOS, and with `python --version` on Windows.
Note: on Linux the program `python` might refer to an old Python version 2.
Don't ever use that!

How to load a file that resides in the src folder?
--------------------------------------------------

To be written ...

Tests complain about missing attribute assert_called, assert_called_once, ...
-----------------------------------------------------------------------------

These require at least Python version 3.6. Check your installation.

I cannot understand the error message from a failed test case
-------------------------------------------------------------

First run `tmc update` to make sure I haven't already fixed that
issue. If the problem persists, make a bug report in:

* Telegram: `https://t.me/dap19s <https://t.me/dap19s>`__

* Github `issues <https://github.com/jttoivon/data-analysis-with-python-spring-2019/issues>`__

* Give feedback, when using `tmc submit`

  
