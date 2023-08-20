#!/bin/sh

# A quick run script
# NOTE: You must have a virtual environment created in this folder.

# Taken from DistroTube's video https://www.youtube.com/watch?v=Wy63jwjpNg4
HERE="$(dirname "$(readlink -f "${0}")")"
cd $HERE
source venv/bin/activate
python3 main_wayland.py
