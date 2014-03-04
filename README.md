# Presentator #

## Introduction ##

This is a simple django project for testing a presentation app which uses websockets (autobahn.js) to communicate commands from the controller to the presentation show-er running on a machine with no input device. The controller is inteneded to be run from a smartphone browser, but it works fine on any browser. The purpose of such a setup is to have a unique presentation system which is easily controlled from a mobile device, allowing the person to walk around the room and providing more possiblities for customize controls and feedback than a simple remote.

## Features ##
### Current ###

At present, the project is in very early stages. It supports only a simple plain-text slideshow script with no images or other media. The controller links with the slideshow-er and can select a slideshow to load and can increment the slides forwards or backwards.

### Next ###

Up next is a polling feature which allows the presenter to embed quick polls in the slideshow which will be pushed to participant's mobile browsers when the relevant slide comes up.

After that, the participant view will be expanded to allow access to slideshow specific notes.

### Future ###

* Embed audio
* Embed video
* Include images
* Better slideshow script model to handle all the different objects.
* Complex interactive slide objects such as a scoreboard, or timer/stopwatch
* Branching logic.

## Rights ##

Several other projects are included as components of this project, such as the foundation css framework and django code. The rights to the material included from those projects belong to their respective projects.

## Usage ##

In order to use this django project you'll need to write a local_settings.py file which describes the database settings you wish to use. see presentator/local_settings.sample. You'll also need to have a group called "controllers" which has permission to "control presentations", and then put some user in that group. Once you log in you'll see the control interface, all others will see the student view, which at present doesn't contain anything, but will show the quick polls once developed.
