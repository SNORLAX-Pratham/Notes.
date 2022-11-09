# Git & Github

---

## <p align="center">Index </p>

1. [Setup Git]

<class="git"> GIT </>
:It is a distributed version controle system.
GIT Installation
1.first we ne need to install git from git website
2.Run the git with all default settings
3.Open git bash
4.When first time using git we need to tell the name and email to git
Type command : git config --global user.name Pratham
git config --global user.email Pratham@gmial.c

There are two type GIT Clone /GIT from scrach
Git Clone: When we make a clone in local computer and work on it
Git from scrach : Wher we make all things from begining

Git from scrach
1.Initilize the git in floder
git command: git init
This command create a hidden .git folder in in file to check run command
git command: ls -lart
This command show all the hidden folder

2. Looking at file status there are traked file/untracked file
   git command:git status
   This command check status of file

   untracked-->>Staged-->>Unmodified-->>Modified
   (This cycle the file follow in git)

3. Start tracking file
   git command : git add xyz.abc
   It will put file in staging are and ready to commit
   To add all the file at once we use git command
   git command: git add . (or u can use) git add -A
   All the file will be put in staging are at once

4. Commit the file
   git command : git commit -m "This is the change"

5. How to recover modified file if there is a mistake
   git command: git checkout
   To Recover all file
   git command: git checkout -f

6. To find the commit made by whome
   git command: git log
7. To find differnce between working director and staging directory  
   git command : git diff

8. To remove file from staging and commit
   git command : git rm xyz.abc
   To remove file only from staging area
   git command : git rm --cached xyz.abc

9. Ignoring file :some file make data or you dont want to add file thn we use it git ignore
   git ignore : touch .git ignore (To make file)

Branches in git (IMPORTANT)
If you are working on an important thing and you mess up then it will create a problem therefor branch are used it make a copy of the main project and you can make changes without harming the main project

1. To make a branch
   git command : git branch xyz
   This will create a new branch
   To change branch
   git command:git checkout xyz
2. To merge the branch into master Branch
   git command: git merge xyz
   this command will merge the branch into the master branch

   Github
   It is hosting for git repository
   1.we need to add git remote 2. SSH key deploy 3. git push -u origin xyz

Git Clone to clone the repository
