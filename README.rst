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

knockout.js - for two-way databinding.  Initially, this is the investigation point of this solution;
  - should also look at / compare angular.js and / or ember.js (and possibly their dart ports);
  - for some comparisons of these three, see http://youtu.be/mVjpwia1YN4
  - => will move investigation to angular (js or dart);
  - may eventually involve / investigate
    - react.js

flask (since working examples for KO exist);
  - may one day move up to django, but for getting all the moving parts worked out, flask.
  - equally similar alternative backends:
    - flask (python)
    - bottle (python)
    - itty (python)
    - martini (go)
    - express.js (js)

mongokit (to keep it simple - json for client);
  - this initially looks like it makes sense for this prototyping forray - can move to others things later;
  - sqlalchemy is too far away from "close to what we want for forms" (too low abstraction level at this point);

mako in preference to jinja2, but only if things work;
  - essentially, this is just to keep it "pythonish" as much as possible
  - it also is what edx does (so it is django-transferable in that way);
  - mustache, or other forms of browser templating are used in js frameworks

sass / less - when the theming time comes;

May look into mobile, and HTML5 local storage for off-lining;

 
Running
========

For information on the status, and running the various branches, see the wiki_.

.. _wiki: https://github.com/yarko/uchi-forms/wiki




