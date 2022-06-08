# About OpenDU
Community has proven to be the strong arm of flight sim environment with time, this enviorioment lacks a freeware, customizable and scalable Display Unit software. In the other hand, Python is one of the most popular programming languages with a very short learning curve and has the advantage to work in multiple platforms, which opens the possibility of getting rid off Windows the most annoying and painful obstacle when working with home cockpits.

OpenDU is a python based application with the purpose of creating a community based display unit of any kind for use within flight simulators, such as Primary Flight Displays, Control Display Units, Instructor Station or even general aviation gauges for use in home cockpits,  

It uses the PyGame library and Vulkan to render the displays and connects via TCP using an in house lua script for use with FSUIPC to Flight Simulator or Prepar3D and via FlyWithLua through XPlane.

The goal of this project is to lower the software costs of homecockpit building for personal and commercial use.

# Hardware Integration
In a near future I will make it available a arduino script sample which also connects to OpenDU via TCP IP. The dream is to make a PoE device and make all the pieces on the simulator connected by one single cable.

In a far future, the plan is to make it work with ARINC 429.

# Pre-requisites
- Python3 with PiP (Package Installer / Manager);
- PyGame Library (python -m pip install -U pygame --user);
- XPlane 10 or Higher (ESP Engine support is still unavailable);
- FlyWithLua Plugin (https://forums.x-plane.org/index.php?/files/file/17468-flywithlua-for-xp9-and-xp10/); or
- FlyWithLua NG (https://forums.x-plane.org/index.php?/files/file/38445-flywithlua-ng-next-generation-edition-for-x-plane-11-win-lin-mac/).

# Dev Schedule
The project is still under development and there is a lot of work to do, so don't expect a working project when you download.

# Join Our Team
Fell free to join our discussion at discord.gg/BE2tgCz2ZT
