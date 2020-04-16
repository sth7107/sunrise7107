# Git codes
## Initiate a git repository

To start track the changes of a folder w/o files, we need to initiate it first.

\```shell

git init

\```

After initialization, there is .git folder inside. It makes it possible to track the change of the folder. If we want to stop to track, delete the .git.

\```shell

rm -rf .git

\```

Then, we no longer track it. If we want to track it again, use the same to initiate.

\```shell

git init

\```

Following, we can run this to check the status of this folder.

\```shell

git status

\```

Here, we can see some untracted files displayed.

To create new files, use this.

\```shell

touch file_name

\```

For example, we can create a file called .gitignore, to filter the files we don't want to share.

\```shell

touch .gitignore

\```

In this .gitignore file, we can list all the files, or types of files that git would not track.

\```shell

.DS_store

file_name1

file_name2

*.file_type

\```

Then, we run

\```shell

git status

\```

We can see file_name1, file_name2 and files in file_type cannot be seen on the screen.



Add files to staging area.

\```shell

git add -A

or

git add .

\```

After adding to the staging area, continue to commit.

\```shell

git commit -m "Initial Commit"

\```



If you want the file back to staging area, use

\```shell

git reset file_name

or

git reset (to remove every file in staging area)

\```





\## Clone a repository and push changes

Go to an empty folder you want to put the remote repository. Let's say folder1_clone. It must be an empty folder for clone. To check if the folder is empty or not, use this.

\```shell

ls -la

\```

<p align="center">

<img src=lsla.png>

</p>



\+ Clone a local repository. <br>

\```shell

git clone <path/folder_name> (where to clone)

e.g. 

 git clone ../folder1 .

\```

 This is to clone the folder1 to the current folder you are in, "folder1_clone". The last character "." means the current folder.



\+ Clone a url repository. <br>

\```shell

git clone <url> (where to clone)

e.g. 

 git clone https://github.com/XXX/XXX.git .

\```

To check the cloned repository. <br>

\```shell

git remote -v

git branch

\```



After doing some changes in this cloned folder, push the change to the origin folder.

\```shell

git diff (to check what differences have been made.)

git add . <br>

git commit -m "any commit" <br>

git pull origin master (change this cloned one with any change from the original folder) <br>

git push origin master (push the cloned folder change to the original folder) 

\```



Perhaps you get this error after git push.

\```shell

remote: error: refusing to update checked out branch: refs/heads/master

remote: error: By default, updating the current branch in a non-bare repository

remote: is denied, because it will make the index and work tree inconsistent

remote: with what you pushed, and will require 'git reset --hard' to match

remote: the work tree to HEAD.

remote:

remote: You can set the 'receive.denyCurrentBranch' configuration variable

remote: to 'ignore' or 'warn' in the remote repository to allow pushing into

remote: its current branch; however, this is not recommended unless you

remote: arranged to update its work tree to match what you pushed in some

remote: other way.

remote:

remote: To squelch this message and still keep the default behaviour, set

remote: 'receive.denyCurrentBranch' configuration variable to 'refuse'.

\```

In this case, you need to make a little change to the config.

\```shell

git config receive.denyCurrentBranch updateInstead (<span style="color:yellow"> This is super important. Without this, the cloned folder's change cannot be pushed to this original folder. </span>)

\```

After this config change, when you push, you can see the following.

\```shell

$ git push origin master

Enumerating objects: 5, done.

Counting objects: 100% (5/5), done.

Delta compression using up to 8 threads

Compressing objects: 100% (2/2), done.

Writing objects: 100% (3/3), 278 bytes | 278.00 KiB/s, done.

Total 3 (delta 1), reused 0 (delta 0), pack-reused 0

To C:/Users/erica/Documents/Git-Basics/Cloned-Repo/../remote_repo.git

  1e9422b..58880f8 master -> master

\```