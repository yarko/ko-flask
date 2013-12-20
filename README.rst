Overview
========

Set up a MVVC framework for processing large (think IRS-1040-ish) forms
for projects, with minimal editing.

The idea / motivation between trying this with an MVVC is that it is essentially
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

knockout.js - for two-way databinding.  This is the hub of this solution at the moment;
  - MVVM alternatives might be polymer.dart (but that would be a "Version 2" sort of effort/experiment);

flask (since working examples for KO exist);
  - may one day move up to django, but for getting all the moving parts worked out, flask.

mongokit (to keep it simple - json for client);
  - rethinkdb has no schema-ish niceness to match;
  - sqlalchemy is too far away from "close to what we want for forms" (too low abstraction level at this point);

    - since there is familiarity w/ SQLAlchemy, we may move to this - but not for starters;

mako in preference to jinja2, but only if things work;
  - essentially, this is just to keep it "pythonish" as much as possible
  - it also is what edx does (so it is better django-transferable);

coffeescript - late in the game, if client side develpoment will be easier for it (and demos validate);
  - but really, would probably like to compare this to polymer.dart before getting too committed;

sass / less - when the theming time comes;


WTForms (a flaskism, though will try to stay away all together if possible);

 
Progress
========

- add the flask demo from another repo;


