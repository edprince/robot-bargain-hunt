# robot-bargain-hunt

[![Join the chat at https://gitter.im/edprince/robot-bargain-hunt](https://badges.gitter.im/edprince/robot-bargain-hunt.svg)](https://gitter.im/edprince/robot-bargain-hunt?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/edprince/robot-bargain-hunt.svg?branch=master)](https://travis-ci.org/edprince/robot-bargain-hunt)

Repository containing all collaborative work for the robot-bargain-hunt project

If anybody is interested, I'm experimenting with a web app called 'Trello' which
helps manage projects using lists and stuff. Might be worth exploring, but could
be a dead end. https://trello.com/b/fjeu9Pvw/robot-bargain-hunt

##Current Progress##
So far, using Pygame I have a map being loaded, with a (limited + early)
tile set. The map info is stored in **map_data.txt**, and **map.py** parses this
and renders a map based on those tiles and their locations. A player is also
generated and placed onto the map, and can be controlled with the arrow keys.

If anybody can produce some more/better art in terms of tiles/player/items/other
assets (such as trees, bushes, anything at all), I'm working with a 32 x 32
pixel tile set, so it would need to match that. In order to achieve this, I'm
using ![Piskel](http://www.piskelapp.com/) to make them. Also, I've not done
anything with Pygame before really so if you see any obvious mistakes etc. feel
free to modify.

##Ideas##
These are just a bunch of totally random ideas for possibilities for our game.
 - Alien planet game finding creatures/samples etc.
 - Archeology game finding artifacts in a dig site.
 - Zombie epidemic (infected people being sorted and searched based on their
   level of infection)
 - Shopping spree
 - Thief stealing items from a house, steal as much as possible before alarm
   goes off.
 - Easter egg hunt - Each egg has its own value, need to collect as many as 
   you can in a given time.
 - Beach search - Finding rubbish on the beach and sorting them in the 
   increasing value.
