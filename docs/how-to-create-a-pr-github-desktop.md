# How to create a PR using Github Desktop

**NOTE: Github Desktop is only for Windows and macOS users!**

You can find official documentation of Github Desktop [here](https://docs.github.com/en/desktop).

## Requirements

Download [Github Desktop](https://desktop.github.com/).

## Making your changes

1. Make sure you have selected your fork of azerothcore-wotlk.

1. Create a new branch (Ctrl + Shift + N)

  1. Create a branch name that will make it easy for you to remember what you have fixed.

1. Now you can go ahead and make your changes.

1. Commit your changes

  1. Write a relevant commit summary. We have standard commit prefixes that we prefer be used, you can find them [here](commit-standards).

  1. (Optional) Describe your changes in the description. 
  
    1. (Situational) If your changes has been cherry-picked from another project, you should include the link to the original commit.

  1. (Situational) If your changes has been cherry-picked from another project, you should include the authors as Co-Authors.

1. Make sure your brach is up-to-date with Master branch.

  1. Merge into Current Branch (Ctrl + Shift + M)

  1. Search for Master and select **upstream/master**.

  1. If it is not up-to-date, press Merge **upstream/master** into **your-branch**

1. Publish your branch (Ctrl + P).

1. Create a Pull Request (Ctrl + R).

1. Name your Pull Request after the [Commit Standards](commit-standards).

1. Fill in all relevant fields in the PR Template.

  1. Describe the changes you have made.

  1. Search for an existing issue, if there is one, link it to be closed.

  1. If you have any sources, it is nice if you provide them.

  1. Describe the test you have performed. Does not need to be detailed.

  1. Describe how to test the change detailed.

  1. Is there anything missing from the PR that needs to be done at a later stage?
