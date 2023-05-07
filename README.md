# Disk Space Announcer
### The script will automatically send messages to the designated Discord channel every day with information about the disk usage and server IP address.

## Installation
### Install required packages:
```
apt install python3-pip screen wget -y
```
### Install required Python packages:
```
pip3 install discord psutil requests
```
### Create the directory to store the script:
```
sudo mkdir $HOME/diskspaceann
```
### Download the script from GitHub:
```
wget -O $HOME/diskspaceann/diskspaceann.py "https://raw.githubusercontent.com/StakeTake/disk-space-announces/main/diskspaceann.py"
```
### Edit the script file using the nano text editor. Make sure to add your Discord bot token and the channel ID where the bot will send messages:
```
nano $HOME/diskspaceann/diskspaceann.py
```
### Start a new screen session:
```
screen -S diskspaceann
```
### Run the Python script in the screen session:
```
python3 $HOME/diskspaceann/diskspaceann.py
```
Detach from the screen session:
Press CTRL+A+D to detach from the screen session and leave the script running in the background.
