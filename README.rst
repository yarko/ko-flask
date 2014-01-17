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
server to talk to a knockout.js_ client.

Since there are working flask examples, I next jumped to that.
However, knockoutJS's talk of potential components and frameworking in 2014
make me look at Angular more seriously.
That is the current investigative direction.


Plans (sort of)
===============

Intent:

two-way databinding - Initially, knockout.js was the investigation point of this solution;
  - also looked at / compare angular.js_ and / or ember.js_ (and possibly their dart ports);
  - also looked at react.js_
  - for some comparisons of these three, see http://youtu.be/mVjpwia1YN4
  - => will move investigation to angular (js or dart_);
  - may eventually involve / investigate react.js_

flask (since working examples exist);
  - may one day move up to django, but for getting all the moving parts worked out, flask.
  - equally similar alternative backends:
    - flask_ (python)
    - bottle_ (python)
    - itty_ (python)
    - martini_ (go)
    - express.js_ (js) --- See mean.io_ & yeoman.io_

data - mongokit_ (to keep it simple - json for client);
  - this initially looks like it makes sense for this prototyping forray - can move to others things later;
  - sqlalchemy_ is too far away from "close to what we want for forms" (too low abstraction level at this point);
  - use HTML5 `web storage`_, or `indexed DB`_ also, particularly for mobile_.

templating - mako_ in preference to jinja2_, but only if things work;
  - essentially, this is just to keep it "pythonish" as much as possible
  - it also is what edx does (so it is django-transferable in that way);
  - mustache, or other forms of browser templating are used in js frameworks

sass_ / less - for theming;


 
Running
========

For information on the status, and running the various branches, see the wiki_.

.. _angular.js: http://angularjs.org/
.. _bottle: http://bottlepy.org/
.. _dart: http://pub.dartlang.org/packages/angular
.. _ember.js: http://emberjs.com/
.. _express.js: http://expressjs.com/
.. _flask: http://flask.pocoo.org/
.. _indexed DB: http://www.w3.org/TR/IndexedDB/
.. _itty: https://github.com/toastdriven/itty
.. _jinja2: http://jinja.pocoo.org/
.. _knockout.js: http://knockoutjs.com/
.. _less: http://www.lesscss.org/
.. _mako: http://www.makotemplates.org/
.. _martini: http://martini.codegangsta.io/
.. _mean.io: http://mean.io
.. _mobile: http://www.ng-newsletter.com/posts/angular-on-mobile.html
.. _mongokit: http://namlook.github.io/mongokit/
.. _react.js: http://facebook.github.io/react/
.. _sass: http://sass-lang.com/
.. _sqlalchemy: http://www.sqlalchemy.org/
.. _web storage: http://www.w3.org/TR/webstorage/
.. _wiki: https://github.com/yarko/uchi-forms/wiki
.. _yeoman.io: http://yeoman.io





