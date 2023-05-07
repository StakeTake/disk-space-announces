Disk Space Announcer
This Python script utilizes the Discord API to send messages with information about the disk usage and server IP address to a designated Discord channel.

Installation
Install required packages:

sh
Copy code
apt install python3-pip screen wget -y
Install required Python packages:

sh
Copy code
pip3 install discord psutil requests
Create the directory to store the script:

sh
Copy code
sudo mkdir $HOME/diskspaceann
Download the script from GitHub:

sh
Copy code
wget -O $HOME/diskspaceann/diskspaceann.py "https://raw.githubusercontent.com/StakeTake/disk-space-announces/main/diskspaceann.py"
Edit the script file using the nano text editor. Make sure to add your Discord bot token and the channel ID where the bot will send messages:

sh
Copy code
nano $HOME/diskspaceann/diskspaceann.py
Run the script in a screen session:

sh
Copy code
screen -S diskspaceann
python3 $HOME/diskspaceann/diskspaceann.py
Detach from the screen session:
Press CTRL+A+D to detach from the screen session and leave the script running in the background.

Usage
The script will automatically send messages to the designated Discord channel every day with information about the disk usage and server IP address.

Credits
This script was created by StakeTake.
