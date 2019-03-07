# Data analysis with Python - Spring 2019

## Authors

Materials created by [Jarkko Toivonen](https://github.com/jttoivon).

# License

The course material is licensed under a [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license.

# Usage:

Create a new branch for your repository with name `gh-pages`.
This is where the html pages will be stored.
They will be visible at https://<account>.github.io/data-analysis-with-python-spring-2019/

In Github choose settings -> Developer settings -> Personal access tokens
and generate an access token and copy it.

In Travis CI (travis-ci.com) select the correct repository and add an environment variable
with key ´GITHUB_TOKEN´ and as value the secret token you got from github.
This allows Travis to push the html pages to the gh-pages branch of the github repository.

You may at some point need to install the Travis CI application to github.

