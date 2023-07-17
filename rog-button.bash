#!/bin/bash
# Purpose: Turn the AniMe matrix on or off using the ROG button.
# Usage: KDE Setting -> Shortcuts -> Add command -> Call this script "bash filename"
service="anime-matrix-datetime-battery"

if systemctl is-active --quiet $service
then
  sudo /bin/systemctl stop $service
else
  sudo /bin/systemctl start $service
fi
