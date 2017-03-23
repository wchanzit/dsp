# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
* show current working directory path - pwd
* creating a directory - mkdir _dir_
* deleting a directory - rmdir _dir_
* creating a file using `touch` command - touch _file.txt_
* deleting a file - rm _filename.txt_
* renaming a file - mv _oldfilename_ _newfilename_
* listing hidden files - ls -a
* copying a file from one directory to another cp _olddir/filename.txt_ _newdir/filename.txt_
* finding a string within a file - grep _string_ _filename.txt_
* getting command help - man _command_
---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >
`ls`       display directories and files within current working directory
`ls -a`    include hidden files and folders
`ls -l`    display long-format listing
`ls -lh`   display files with human-readable format
`ls -lah`  display files with human-readable format, including hidden files
`ls -t`    displays newest files first
`ls -Glp`  displays colored, long-format files and directories, with "/" marking directories
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >
`ls -d`    displays only directories
`ls -m`    displays the names as a comma-separated list
`ls -R`    includes subdirectories
`ls -lS`   sort by file size
`ls --help`help page
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 
`xargs` adds arguments from the standard input to complete commands, allowing a command to be executed on multiple folders and/or files at once.

e.g. `find . -name "viper*.txt" | xargs rm` deletes all txt files with filenames beginning with "viper" from the working directory
 

