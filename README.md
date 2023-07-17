# AniMe matrix clock & battery level for linux

This script is designed to be used with asusctl to use the AniMe matrix on the Asus ROG Matrix laptops to show the current battery level, date and time.\
This works by creating an image with the current data every second and sending it to the display with asusctl.

# Install

1. Ensure you have [`asusctl`](https://asus-linux.org/asusctl/), `python3` and `pip` installed
1. cd into the `/opt` folder with `cd /opt`
1. Clone the git repo with `sudo git clone https://github.com/florian-h05/anime-matrix-datetime-battery.git`
1. Change ownership to your user with `sudo chown -R $USER:$USER anime-matrix-datetime-battery`
1. cd into that folder with `cd anime-matrix-datetime-battery`
1. Install dependencies with `pip install -r requirements.txt`
1. Set your username in some files with `sudo sed -i "s/%USER/$USER/g" anime-matrix-datetime-battery.service anime-matrix-datetime-battery`
1. Copy the systemd service file with `sudo cp anime-matrix-datetime-battery.service /etc/systemd/system`
1. Enable and start the service with `sudo systemctl enable --now anime-matrix-datetime-battery`
1. Copy the `sudoers.d` file with `sudo cp anime-matrix-datetime-battery /etc/sudoers.d/`
1. Add a keyboard shortcut to your desktop environment, e.g. KDE: Settings -> Shortcuts -> Add command -> Paste "bash bash /opt/anime-matrix-datetime-battery/rog-shortcut.bash" -> Add the ROG button as shortcut

# Usage

Use the ROG button (M4) to turn the AniMe matrix off and on.

## Credits

[Blobadoodle](https://github.com/Blobadoodle) for creating the original repo [Blobadoodle/anime-matric-clock](https://github.com/Blobadoodle/anime-matrix-clock)!

![ga401qc](.github/laptop.png)
