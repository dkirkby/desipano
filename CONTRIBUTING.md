# Contributors Guide

Welcome contributors and thank you for investing your time in our project!

To get an overview of this project see the [README](README.md) file.

## Issues

If you think you have found a problem or have a suggestion or question, first [search if a relevant issue already exists](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments).  If not, please [open a new issue](https://github.com/dkirkby/desipano/issues/new).

## Developer Testing

To test local changes, you need to run a local static file web server and have an internet connection. Start a local server using:
```
cd docs
python3 -m http.server
```
To view the locally served content in your browser, visit http://localhost:8000/

## Deployment

The static website hosted at https://dkirkby.github.io/desipano/ uses [GitHub Pages](https://pages.github.com/). Any commits to the [main branch docs folder](https://github.com/dkirkby/desipano/tree/main/docs) appear immediately under github.com/dkirkby/desipano but
then take some time (at least a few seconds) to propagate through the GitHub deployment actions and CDN caches.  See [here](https://stackoverflow.com/questions/24851824/how-long-does-it-take-for-github-page-to-show-changes-after-changing-index-html) for details.
