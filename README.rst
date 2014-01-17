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

Since there are working flask examples, I've jumped to that.


Plans (sort of)
===============

Intent:

two-way databinding - Initially, knockout.js was the investigation point of this solution;
  - also looked at / compare angular.js and / or ember.js (and possibly their dart ports);
  - also looked at FB react.js
  - for some comparisons of these three, see http://youtu.be/mVjpwia1YN4
  - => will move investigation to angular (js or dart);
  - may eventually involve / investigate react.js

flask (since working examples exist);
  - may one day move up to django, but for getting all the moving parts worked out, flask.
  - equally similar alternative backends:
    - flask (python)
    - bottle (python)
    - itty (python)
    - martini (go)
    - express.js (js) --- See mean.io & yeoman.io

data - mongokit (to keep it simple - json for client);
  - this initially looks like it makes sense for this prototyping forray - can move to others things later;
  - sqlalchemy is too far away from "close to what we want for forms" (too low abstraction level at this point);
  - use HTML5 local data also, particularly for mobile.

templating - mako in preference to jinja2, but only if things work;
  - essentially, this is just to keep it "pythonish" as much as possible
  - it also is what edx does (so it is django-transferable in that way);
  - mustache, or other forms of browser templating are used in js frameworks

sass / less - for theming;


 
Running
========

For information on the status, and running the various branches, see the wiki_.

.. _wiki: https://github.com/yarko/uchi-forms/wiki




