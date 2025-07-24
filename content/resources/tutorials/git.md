---
title: Basic Software Versioning Using Git
type: docs
weight: 5
---

**[Reproducible neuroimaging principles](/about/principles/#repronims-four-core-principles)**: 3b: Use software version control.

**[Actions](/about/principles/#repronims-four-core-actions)**: Version control.

**Tools**: [Git](https://git-scm.com/).

## Challenge

Once you have a working script or an entire workflow for analyzing your data, the next challenge is figuring out how to share it with your colleagues and how to track changes as you improve the code or expand its functionality. This is where Git, a powerful version control system, comes to the rescue.

Git is a widely used tool that enables individuals and teams to manage code efficiently and track changes over time. In simple terms, Git allows you to:

* **Track every version of your code**: No need to create multiple copies of your script with confusing suffixes. Git maintains a complete history of changes, making it easy to revert to any version.
* **Easily share your code**: Collaborate seamlessly by sharing your code with colleagues or across teams using platforms like GitHub or GitLab.
* **Facilitate contributions**: Allow multiple contributors to work on the same codebase simultaneously, with Git handling version conflicts effectively.
* **Experiment risk-free**: Safely test new ideas or features, knowing you can always revert to a previous working version.

Git not only helps you streamline your workflow but also promotes collaboration, reproducibility, and effective project management.

## Exercise

In this exercise we show how you can create your first git repository with your script and how to start collaborating with your colleagues.

## Before you start

Before I show you specific steps, I think it is useful to learn more about the concept behind `git` and version control systems in general. I recommend reading:

- [Overview of the version control systems from Software Carpentry](https://swcarpentry.github.io/git-novice/01-basics.html)
- [Git Parable to learn more about the philosophy behind git](https://practical-neuroimaging.github.io/git_parable.html#the-git-parable) (don’t worry if you won’t understand everything at first)

## Step by step guide

### Step 1: Install the necessary tools

If you are using Linux or OSX, you will likely already have `git` installed, you can open your terminal and try typing `git –help`. If you need to install on your own, you can follow the instructions from the [website](https://git-scm.com/downloads) (if you are a windows user you might want to install `bash shell` that comes with `git`, you can follow [the instructions](https://carpentries.github.io/workshop-template/install_instructions/#shell)).

If you have not yet set the basic git configuration, run:

```
git config --global user.name "Your Name"
git config --global user.email youremail@example.com
```

### Step 2: Create the repository and add a new file

I recommend watching [the ReproNim/ABCD course lesson, starting from minute 35](https://www.youtube.com/watch?v=SyKmry47SsY&t=2139s&ab_channel=ABCD-ReproNimCourse), if you want to have a bit more guidance (you can start from watching minutes 35-46).

- Let’s say you have a directory `my_project` where you have all scripts that are important to you, let’s say you have `fsl_bet.sh` there. In order to start you repository, you can follow:

```
cd my_project
git init
```

  You can check that this is now a git repository by running:

```
git status
```

  You should see something similar to this:

```
On branch master
No commits yet
Untracked files:
  (use "git add \<file\>..." to include in what will be committed)
	fsl\_bet.sh
nothing added to commit but untracked files present (use "git add" to track)
```

 Where you have information about “branches” (this will not be covered in this part, but please check the “Next Step” section if you’re interested), and about untracked files.

`Git` doesn’t start tracking anything without your knowledge and request, you have to specifically add the file to the repository:

```
git add fsl_bet.sh
```

Now when you run the command `git status` again, you should see:

```
On branch master
No commits yet
Changes to be committed:
  (use "git rm \--cached \<file\>..." to unstage)
	new file:   fsl\_bet.sh
```

### Step 3: Create a snapshot of the file

You can see, that `git` recognized a new file added to the repository, and reports that there are “changes to be committed”. By running `git commit` command you create a snapshot of the current state of your file in `git`, and that will allow you to track progress and revert to this point (or snapshot) if needed anytime in the future.

`Git` always requires a “commit message” to be saved together with the snapshot of your code. You will find it very useful in the future if for any reason you need to come back to the older version of your file so you should provide a meaningful message in your real project, here we can just say:

```
git commit -m “the first version of the bet script” fsl_bet.sh
```

(note, if you don’t provide the message with `-m`, git will open an editor and ask you for the message; you can also provide `-a` flag if you don’t want to specify the file you want to commit, but you want all changes to be committed together)

If you run `git status` now, you should see (if you don’t have any other files in this directory):

```
On branch master
nothing to commit, working tree clean
```

So you have confirmation that all changes have been committed (or saved as a snapshot) and the working tree is clean, which means that there are no files that are not tracked by `git`.	

### Step 4: Change the file content and create another snapshot

You have a working script, but of course you will want to experiment and change various things. Once you modify the file and run `git status` you will see:

```
On branch master
Changes not staged for commit:
  (use "git add \<file\>..." to update what will be committed)
  (use "git restore \<file\>..." to discard changes in working directory)
	modified:   fsl\_bet.sh
no changes added to commit (use "git add" and/or "git commit \-a")
```

Another helpful command is that shows you the difference between the current state of the files and the last snapshot:

```
git diff
```

The output will show you specific changes and point to the file:

```
**diff \--git a/fsl\_bet.sh b/fsl\_bet.sh**
**index ae6df91..a8f4079 100644**
**\--- a/fsl\_bet.sh**
**\+++ b/fsl\_bet.sh**
@@ \-2,7 \+2,7 @@

 INPUT\_FILE="input.nii.gz"
 OUTPUT\_FILE="output\_brain.nii.gz"
\-OPTIONS="-f 0.5"
\+OPTIONS="-f 0.3"

 \# Run the FSL bet command
 echo "Running FSL bet with:"
```

After checking if the changes are what you want to commit, you can create another snapshot again:

```
git commit -am “changing option to -f 0.3”
```

If you want to see the status again you will see that there are no new changes.

Now you can also check your history, by running:

```
git log
```

And the output will contain the history of your changes:

```
commit 53314b7da1e5f3352cecaf2c3ec52875f328a871 (**HEAD \-\> master**)
Author: Author Name \<author\_email@gmail.com\>
Date:   Fri Dec 20 12:16:41 2024 \-0500
    changing option to \-f 0.3
commit 744d47eba6a768b505e31fa75976e025aa7750ad
Author: Author Name \<author\_email@gmail.com\>
Date:   Fri Dec 20 12:08:26 2024 \-0500
    the first version of the bet script
```

Each commit has a unique hash value, e.g., 744d47eba6a768b505e31fa75976e025aa7750ad, that you could later use to compare with or to revert your changes.

You can always compare by running:

```
git diff 744d47eb
```

(note that you have to use the hash value from your history, also you don’t have to use the entire value, the first few numbers are enough).

**This has been a very brief introduction and we only cover how to start the repository and track the changes of your files. If you want to learn more about branching and collaborations, please check the materials from the “Next Step” section.**

## Next steps

The introduction from the previous section was very brief. If you want to have more explanation or learn about additional features, I recommend more extended tutorials that are available online:

- [Software Carpentry lesson](https://swcarpentry.github.io/git-novice/index.html)
- [An interactive course using GitHub platform](https://github.com/Science-Reproducibility/version-control-systems/tree/main)

