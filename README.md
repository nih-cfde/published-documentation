# published-documentation

This repository builds the public technical documentation for the CFDE: https://docs.nih-cfde.org/en/latest/ (note that the ReadTheDocs [website](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/) redirects to this public URL).

The website is a compilation of 4 data sources:

<!-- - https://github.com/nih-cfde/c2m2 -->

- the `master` branch of the c2m2 repo is pulled in here as the submodule docs/c2m2

- https://github.com/nih-cfde/the-fair-cookbook

  - the `master` branch is pulled in here as the submodule docs/the-fair-cookbook

- https://github.com/nih-cfde/cfde-submit

  - the `main` branch is pulled here as the submodule docs/cfde-submit

- The other directories in the docs/ directory of this repo are local to this repo

Contents:
1. [Updating the Documentation in the Public Documentation Site from a submodule](#submod-repos)
2. [Updating the Documentation in the Public Documentation Site from this repo](#this-repo)

# Updating the Documentation in the Public Documentation Site from a submodule <a name="submod-repo"></a>

## Overview

- To update documents or layout relating to the FAIR cookbook, make changes to the `master`branch of https://github.com/nih-cfde/the-fair-cookbook

- Updates to documents or layout relating to the c2m2 are made on the `master` branch of the c2m2 repo https://github.com/nih-cfde/c2m2

- To update documents or layout relating to `cfde-submit`, make changes to https://github.com/nih-cfde/cfde-submit

- To update the overall style of this website, the contents of the "About" pages, or to add additional data sources, make changes to this repository.

A robot watches for changes made to the `master` branches of all the submodules. When changes are detected, the robot will automatically pull the changes into this repository and:

  - attempt to render them as a preview site so the author can see how they will look in the public site.
  - make a PR to incorporate your changes into the stable branch so they can be merged into the public site.

You should use the preview site to check that the changes look the way you want. If they do, you should positively review (i.e., approve) the PR to the stable branch so it can be merged in.

## Detailed Instructions for Updating the Published Documentation Website

### Make your desired changes in the correct repo

To update documents or layout relating to the FAIR cookbook, make changes to https://github.com/nih-cfde/the-fair-cookbook

Updates to documents or layout relating to the c2m2 are made on the c2m2 repo
  <!-- - https://github.com/nih-cfde/c2m2 -->

To update documents or layout relating to `cfde-submit`, make changes to https://github.com/nih-cfde/cfde-submit

The robot checks hourly for changes to these repositories. We recommend working in a personal branch, and pushing those changes to `master` once you are happy with them.

The only consideration for content changes is appropriate/correct linking.

 - if you are linking to other docs *within* that repo, use relative links

 - if you are linking to the *glossary*, or across repos, you need to use a full link to the rendered version of the docs, for e.g. `[asset inventory](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/CFDE-glossary/#asset-inventory)`

If you are adding or removing pages, or otherwise changing how the navigation of the pages should work, you do that using `.pages` files.

- Directories without a `.pages` file will have their contents rendered in alphabetical order, using the yaml header information for page titles if available, or the first header in the markdown file as the page title.

- Directories with a `.pages` file will have their contents rendered according to the specifications in the `.pages` file:
  - `title: XXX` will render that folder navigation title as XXX
  - you can redundantly hide a folder and its contents with `hide: true`
  - you can order the contents of the directory with `nav:`
     - `nav:` should be followed by an ordered list of files as bullet points. Be sure to nest bullets with spaces. Using tabs instead of spaces will cause it to fail.
     - It will render the file title from the yaml header or first header line as above. You can override this behavior by specifying a file title as in `First page: page1.md`
  - you can make a link to a different web address with `- Link Title: https://lukasgeiter.com`
- For more options and examples see [awesome pages documentation](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)

### Check the preview site

If the robot detects changes to either sub repository, it automatically:

- makes a branch called `update-<repo>-preview` with the changes
- makes a PR to merge that branch into `<repo>preview`
- runs a series of build checks

If those build checks all pass, it will then automatically merge and close the PR, then build a preview site for you to browse

#### Preview sites
c2m2: https://cfde-published-documentation.readthedocs-hosted.com/en/c2m2preview/
fair cookbook: https://cfde-published-documentation.readthedocs-hosted.com/en/cookbookpreview/
cfde-submit: https://cfde-published-documentation.readthedocs-hosted.com/en/cfde-submitpreview/

If your preview site looks as expected, go to [Publishing your changes](#Publishing-your-changes)

If your preview site does not look right, continue making changes to the appropriate repo or look at the next section of this document on Troubleshooting.

#### Troubleshooting

If this preview pull request runs and closes itself without you doing anything, then it worked as intended!

If the preview pull request does not merge and close itself, then there was a problem.

There are four possible reasons the PR might not automatically merge into `XXXpreview/XXXpreview`:

- The most likely reason is that the preview branch needs to be refreshed

- The second possibility is that a stale preview was already in the `XXXpreview` branch and is clashing with yours. To fix this problem delete the `XXXpreview` branch and wait for the next hourly run. If it's a fresh preview branch, your changes may have made the repos incompatible. Tag @ACharbonneau in your PR and she'll help

- Very occasionally, the github robot fails for server related reasons when there is otherwise no problem. Removing the `XXXpreview` branch so that the robot tries again generally fixes this. Or tag @ACharbonneau

- Github has imposed a 60 day limit on actions, so if the robot hasn't detected a change in the original repo for more than 60 days, it stops watching the repo. You can this by looking at the [actions tab for this repo](https://github.com/nih-cfde/published-documentation/actions). Each original repo has two actions: a 'preview' and a 'stable'. If the actions for your repo have been automatically stopped, you can restart them by clicking on them. If you cannot restart the action, please contact achar@ucdavis.edu.


### Publishing your changes

If the robot detects changes to any submodule, it also automatically:

- makes a branch called `update-<repo>docs` with the changes
- makes a PR to merge that branch into stable
- runs a series of build checks

This PR will have your changes, and a link to your preview site. You can continue making changes on your local repo, and they will be automatically added to this PR, and a new preview site generated with the addions. Once you are happy with your preview site, approve this PR. An administrator will double check the PR and then merge the changes into the public site https://github.com/nih-cfde/published-documentation. Administrators are automatically tagged by the PR robot. However, if you find they are taking an excessively long time, please re-tag @ACharbonneau

# Updating the Documentation in the Public Documentation Site from this repo <a name="this-repo"></a>

Only overall style of this website and the contents of the "About" pages are editable from this repository.

To make changes to this repo:

- make a branch for work
- when you are happy with your changes, make a PR of your branch to a branch called, exactly, `preview`
- the robot will automatically:
   - run a series of build checks, and if those checks pass
   - build a preview site for you to see your proposed changes at https://cfde-published-documentation.readthedocs-hosted.com/en/preview/
- if your changes are as expected, make a PR of your branch to `stable` and tag @ACharbonneau and @marisalim
- the admin team will check your changes and approve

** if you have admin access to ReadTheDocs you can skip testing your changes in the `preview` branch and use the ReadTheDocs automated preview branch

## Troubleshooting

There are four possible reasons the PR might not automatically merge into preview:

- The most likely reason is that the preview branch needs to be refreshed

- The second possibility is that a stale preview was already in the `preview` branch and is clashing with yours. To fix this problem delete the `preview` branch and wait for the next hourly run. If it's a fresh preview branch, your changes may have made the repos incompatible. Tag @ACharbonneau in your PR and she'll help

- Very occasionally, the github robot fails for server related reasons when there is otherwise no problem. Removing the `preview` branch so that the robot tries again generally fixes this. Or tag @ACharbonneau
- 
- Github has imposed a 60 day limit on actions, so if the robot hasn't detected a change in the original repo for more than 60 days, it stops watching the repo. You can this by looking at the [actions tab for this repo](https://github.com/nih-cfde/published-documentation/actions). Each original repo has two actions: a 'preview' and a 'stable'. If the actions for your repo have been automatically stopped, you can restart them by clicking on them. If you cannot restart the action, please contact achar@ucdavis.edu.
