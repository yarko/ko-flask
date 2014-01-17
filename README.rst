Overview
========

Set up a MVVM-ish framework for processing large (think IRS-1040-ish) forms
for projects, with minimal editing.

The idea / motivation between trying this with an MVVM is that it is essentially
a light  client-server configuration, the idea being to communicate the json
form of the data model from server to client, and have the client "just lay
out" the entry, and deal with the data-binding.

History
=======

I initially tried this with django, but did not find success in getting the
server to talk to a knockout.js client.

Since there are working flask examples, I next jumped to that.
However, knockoutJS's talk of potential components and frameworking in 2014
make me look at Angular more seriously.
That is the current investigative direction.


Plans (sort of)
===============

Intent:

two-way databinding - Initially, knockout.js was the investigation point of this solution;
  - also looked at / compare angular.js and / or ember.js (and possibly their dart ports);
  - also looked at [react.js](http://facebook.github.io/react/)
  - for some comparisons of these three, see [http://youtu.be/mVjpwia1YN4](http://youtu.be/mVjpwia1YN)
  - => will move investigation to angular (js or dart);
  - may eventually involve / investigate [react.js](http://facebook.github.io/react/)

flask (since working examples exist);
  - may one day move up to django, but for getting all the moving parts worked out, flask.
  - equally similar alternative backends:
    - [flask](http://flask.pocoo.org/) (python)
    - [bottle](http://bottlepy.org/) (python)
    - [itty](https://github.com/toastdriven/itty) (python)
    - [martini](http://martini.codegangsta.io/) (go)
    - [express.js](http://expressjs.com/) (js) --- See [mean.io](mean.io) & [yeoman.io](yeoman.io)

data - [mongokit](http://namlook.github.io/mongokit/) (to keep it simple - json for client);
  - this initially looks like it makes sense for this prototyping forray - can move to others things later;
  - [sqlalchemy](http://www.sqlalchemy.org/) is too far away from "close to what we want for forms" (too low abstraction level at this point);
  - use HTML5 [web storage](http://www.w3.org/TR/webstorage/), or [indexed DB](http://www.w3.org/TR/IndexedDB/)  also, particularly for [mobile](http://www.ng-newsletter.com/posts/angular-on-mobile.html).

templating - [mako](http://www.makotemplates.org/) in preference to [jinja2](http://jinja.pocoo.org/), but only if things work;
  - essentially, this is just to keep it "pythonish" as much as possible
  - it also is what edx does (so it is django-transferable in that way);
  - mustache, or other forms of browser templating are used in js frameworks

sass / less - for theming;


 
Running
========

For information on the status, and running the various branches, see the wiki_.

.. _wiki: https://github.com/yarko/uchi-forms/wiki




