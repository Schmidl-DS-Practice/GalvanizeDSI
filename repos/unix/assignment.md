# Assignment

This is an individual exercise (each person needs to do it), but feel free to work in groups or pairs.  

This assignment has three goals:  
* Make an Amazon Web Services Account and sign up for Galvanize sponsored $1000 credit.  This typically takes a couple of weeks.  Once it goes through you'll be able to spin up and pay for powerful computing services on AWS (instead of just using your laptop).  
* Get you oriented to your working environment for the course from the command line.  The less pointing-and-clicking you do in this course, the better.
* Introduce and give you experience modifying your `~/.bashrc` (Linux),  `~/.bash_profile` (MacOs), or `~/.zshrc` (zshell) script that governs the shell environment you interact with from Terminal.  This includes creating your own environment variables.  
* (If there's time) Introduce some command line utilities that you may find useful in your data science projects.


## Part 1 - Sign up for AWS and your promotional credit.
Follow this [guide.](Galvanize_DSI_AWS_Credit_Instructions.pdf)

## Part 2 - Introduction to `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc`  
When you first start a Terminal on your laptop, a script runs that sets the environment that the Terminal operates in.  The name of the script depends on your operating system.  For MacOs, it's either `~/.bash_profile` or `~/.zshrc`, and for Ubuntu Linux it's `~/.bashrc`.  This file **should already exist** on your system - your shouldn't have to create it.  

1. Navigate to your home directory (`$ cd ~`) and then list all the files there, both not hidden (`$ ls`) and hidden (`$ ls -a`).
2. When you looked for hidden files, you should have seen one of the three above.  On Macs that have upgraded to Catalina, you'll want to use `~/.zshrc`.
3. Open the file using a text editor.  For example, if you're using VSCode you'd type `$ code .bash_profile` if `.bash_profile` is the one you saw.
4. Inspect the file.  Can you find where Anaconda added Anaconda's version of Python to the system path?  
5. Scroll down to the bottom and add your AWS keys as environment variables.  Here'a a [guide](https://blog.gruntwork.io/authenticating-to-aws-with-environment-variables-e793d6f6d02e).  Save and close the file.
6. After you add them, your current terminal session hasn't been updated.  [source](https://stackoverflow.com/questions/4608187/how-to-reload-bash-profile-from-the-command-line) your intialization script, then use `echo` in terminal to check that you can see them.

## Part 3 - Modify your prompt to show git formatting
Follow [these install directions](https://github.com/magicmonty/bash-git-prompt) to install a git formatter for your terminal. If you're on MacOs, use the Homebrew directions.  If Linux, you'll need the Git Clone directions.  In both cases, you'll need to add something to the `~/.bash_profile` or `~/.bashrc` for it to work (read the directions!).

## Part 4 - Unix assignment

This assignment will give you the opportunity to practice basic unix commands in a terminal session.
We will be working with the command line throughout the entirety of this program, and you
will learn plenty as we go, so this assignment is intended to be brief.

1.) Open up your terminal and navigate to your home directory.

2.) In your home directory, create a new directory called
`test_directory`.

3.) Navigate into `test_directory`, and print the working directory
to the screen. Is the pathname printed to the screen an absolute path
or relative path?

4.) Create two files, calling them `test_file1.txt` and `test_file2.txt`.

5.) Use `ls` to make sure that the files are in fact in the directory.

6.) Copy `test_file1.txt` to a new file, calling it `test_file3.txt`. How
many files are there in your directory now?

7.) Rename `test_file3.txt` to `test_file4.txt`. How many files are there
in your directory now?

8.) Within `test_directory`, create a new directory called `inner_directory`.

9.) In one command, move all of the files from `test_directory` into the
`inner_directory`.

10.) In one command, delete `inner_directory` and all its contents.

11.) Navigate back to your root directory, and delete `test_directory` using
`rmdir`. Why does `rmdir` work here (**Hint**: think about what's left in
`test_directory`)?


# (Bonus) Intermediate Introduction to Unix Command Line Interface

0.) You will be using some new commands in the steps below. Read the manual for these new commands: `less`, `grep`, and `sort`. You can access the manual using the `man` command. E.g. run `man less` to read the manual for the `less` command. (Tip: To exit `man`, press 'q' on your keyboard.)

1.) Use `cd` to navigate into the `unix/data/` sub-directory. You should see two files: `2015_sp100.csv` and `plot_stock_prices.py`.

2.) Use `less` to peek at the file (`2015_sp100.csv`). It contains daily stock prices for stocks in the [S&P 100 Index](https://en.wikipedia.org/wiki/S%26P_100) for the year 2015. Notice the lines of the file are in random order.

3.) Use `grep` to print all the lines having prices for Google (symbol: GOOG). Use *bash file redirection* to store these GOOG lines into a file named `2015_goog.csv`.

4.) Use `sort` to sort the lines in `2015_goog.csv`. Use *bash file redirection* to store the sorted lines into a new file named `2015_goog_sorted.csv`.

5.) The Python script `plot_stock_prices.py` knows how to plot stock price data files. Run that script, and use *bash file redirection* to input the file `2015_goog_sorted.csv` into the script's *stdin*.

6.) Combine steps 3, 4, and 5 above into one command using *bash pipes*.

