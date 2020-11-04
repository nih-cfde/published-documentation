# published-documentation

This repository builds the public technical documentation for the CFDE: https://cfde-published-documentation.readthedocs-hosted.com/en/latest/

The website is a compliation of 3 data sources:

- https://github.com/nih-cfde/specifications-and-documentation 
  - the `master` branch is pulled in here as the submodule docs/specification-and-documentation
- https://github.com/nih-cfde/the-fair-cookbook 
  - the `master` branch is pulled in here as the submodule docs/the-fair-cookbook
- The other directories in the docs/ directory of this repo are local to this repo


# Updating the Documentation in the Public Documentation Site from a submodule

## Overview

To update documents or layout relating to the FAIR cookbook, make changes to https://github.com/nih-cfde/the-fair-cookbook 
To update documents or layout relating to the C2M2, make changes to https://github.com/nih-cfde/specifications-and-documentation 
To update the overall style of this website, the contents of the "About" pages, or to add additional data sources, make changes to this repository.

A robot watches for changes made to the `master` branches of both https://github.com/nih-cfde/the-fair-cookbook and https://github.com/nih-cfde/specifications-and-documentation. When changes are detected, the roboto will automatically pull the changes into this repository and:

- attempt to render them as a preview site so the author can see how they will look in the public site
- make a PR to incorporate your changes into the stable branch so they can be merged into the public site

You should use the preview site to check that the changes look the way you want. If they do, you should positively review the PR to the stable branch so it can be merged in.

## Detailed Instructions for Updating the Published Documentation Website

### Make your desired changes in the correct repo

To update documents or layout relating to the FAIR cookbook, make changes to https://github.com/nih-cfde/the-fair-cookbook 
To update documents or layout relating to the C2M2, make changes to https://github.com/nih-cfde/specifications-and-documentation 

The robot checks hourly for changes to the `master` branch of these repositories.

 We recommend working in a personal branch, and pushing those changes to `master` once you are happy with them.

For changes to content, there are no special considerations except for linking.
 - if you are linking to other docs *within* that repo, use relative links
 - if you are linking to the *glossary*, or across repos, you need to use a full link to the rendered version of the docs, for e.g. `[asset inventory](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/CFDE-glossary/#asset-inventory)`

If you are adding or removing pages, or otherwise changing how the navigation of the pages should work, you do that using `.pages` files.

- Directories without a `.pages` file will have their contents rendered in alphabetical order, using the yaml header information for page titles if available, or the first header in the markdown file as the page title
- Directories with a `.pages` file will have their contents rendered according to the specifications in the `.pages` file:
  - `title: XXX` will render that folder navigation title as XXX
  - you can redundantly hide a folder and its contents with `hide: true`
  - you can order the contents of the directory with `nav:`
     - `nav:` should be followed by an ordered list of files as bullet points. Be sure to nest bullets with spaces. Tabs will cause it to fail.
     - It will render the file title from the yaml header or first header line as above. You can override this behavior by specifying a file title as in `First page: page1.md`
  - you can make a link to a different web address with `- Link Title: https://lukasgeiter.com`
- For more options and examples see [awesome pages documentation](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)

### Check the preview site

If the robot detects changes to either sub repository, it automatically:

- makes a branch called update-<repo>-preview with the changes
- makes a PR to merge that branch into <repo>preview
- runs a series of build checks

#### specifications-and-documentation 
If those build checks all pass, it will then automatically merge update-specsdocs-preview into specspreview, and will build a preview site for you to browse at: https://cfde-published-documentation.readthedocs-hosted.com/en/specspreview/

#### the-fair-cookbook 
If those build checks all pass, it will then automatically merge update-fair-preview into cookbookpreview, and will build a preview site for you to browse at: https://cfde-published-documentation.readthedocs-hosted.com/en/cookbookpreview/

If your preview site looks as expected, go to [Publishing your changes](#Publishing-your-changes)

If your preview site does not look right, continue making changes to the appropriate repo or look at Troubleshooting below.

#### Troubleshooting

There are three possible reasons the PR might not automatically merge into specspreview/cookbookpreview:

- The most likely reason, is that the preview branch needs to be refreshed, that a stale preview was already in the specspreview/cookbookpreview branch and is clashing with yours. To fix it delete the specspreview/cookbookpreview branch and wait for the next hourly run
- If it's a fresh preview branch, your changes may have made the repos incompatible. Tag @Acharbonneau in your PR and she'll help
- Very occasionally, the github robot fails for server related reasons when there is otherwise no problem. Removing the specspreview/cookbookpreview branch so that the robot tries again generally fixes this. Or tag @Acharbonneau


### Publishing your changes

If the robot detects changes to either sub repository, it also automatically:

- makes a branch called update-<repo>docs with the changes
- makes a PR to merge that branch into stable
- runs a series of build checks

Once you are happy with your preview site, approve this matching PR, and it will be merged in. An administrator has to merge this PR into the https://github.com/nih-cfde/published-documentation repository, and they are automatically tagged by the PR robot. However, if you find they are taking an excessively long time, please re-tag @Acharbonneau

# Updating the Documentation in the Public Documentation Site from this repo

Only overall style of this website and the contents of the "About" pages are editable from this repository. 

To make changes to this repo:

- make a branch for work
- when you are happy with your changes, make a PR of your branch to a branch called `preview`
- the robot will automaticaly:
   - run a series of build checks, and if those checks pass
   - build a preview site for you to see your proposed changes at https://cfde-published-documentation.readthedocs-hosted.com/en/preview/
- if your changes are as expected, make a PR of your branch to 'stable' and tag @Acharbonneau and @marisalim 


## Troubleshooting

There are three possible reasons the PR might not automatically merge into preview:

- The most likely reason, is that the preview branch needs to be refreshed, that a stale preview was already in the preview branch and is clashing with yours. To fix it delete the preview branch and re-do your PR to preview
- If it's a fresh preview branch, your changes may have made the repos incompatible. Tag @Acharbonneau in your PR and she'll help
- Very occasionally, the github robot fails for server related reasons when there is otherwise no problem. Removing the preview branch so that the robot tries again generally fixes this. Or tag @Acharbonneau


