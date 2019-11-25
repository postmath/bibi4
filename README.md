# bibi4
Site to administer secret santa gatherings, written in Python with Flask

This site will offer the following features:
* Create a group for a single secret santa event, where everyone gets one or more gifts for others
* Add logins for all participants - or let them create their own login
* Set up rules for who can pick whom to get something for - e.g. spouses don't get each other, or, in the future, you don't get the same person as last year
* Make the secret pick of who gets something for whom -- you can only see your own pick
* Optionally register wishes with the site
* Claim someone else's wish(es), so that multiple people don't get the same thing for the same person, which everyone except the intended recipient can see

To set up on a dev machine, follow the standard steps for a flask project, which I'll include below for easy reference.
* `python3 -m venv venv`
* `. venv/bin/activate`
* `pip3 install flask`
* `export FLASK_APP=bibi4`
* `export FLASK_ENV=development`
