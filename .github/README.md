# AzerothCore Wiki

See in: [English :en:](README.md) | [Español :es:](README_es.md)

Wiki for the AzerothCore project available here: https://www.azerothcore.org/wiki/home

Welcome to the AzerothCore Wiki! This repository provides comprehensive documentation for setting up, configuring, and customizing the AzerothCore WoW emulator.

If you want to contribute to the wiki please open a PR in the /docs/ directory.

Any problems? [Open a issue](https://github.com/azerothcore/wiki/issues/new).

# Building and Running AzerothCore Wiki Locally
To build and run the wiki site locally to test your changes, you will need to [install Ruby](https://www.ruby-lang.org/en/documentation/installation/#rubyinstaller) on your system.

Once this is done, install bundler:
```sh
gem install bundler
```

After bundler is installed, clone the repository and change the directory in your shell to the root of the checked out repository. To install the required gems we need, we will run the following command:
```sh
bundle install --gemfile=./.env-files/Gemfile.github 
```

Now that our gems are installed, we can now build the site and run it to see what our changes look like:
```sh
bundle exec --gemfile=./.env-files/Gemfile.github jekyll serve --destination _site --baseurl /wiki --verbose --open-url
```