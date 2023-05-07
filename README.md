This script is a Python program that utilizes the Discord API to send messages with information about the disk usage and server IP address to a designated Discord channel. 
Installing required packages
apt install python3-pip screen wget -y: Installs Python3, pip3, screen and wget.
Installing required Python packages
pip3 install discord psutil requests: Installs the Python modules required for the script to work.
Creating the directory to store the script
sudo mkdir $HOME/diskspaceann: Creates a new directory named "diskspaceann" in the home folder.
Downloading the script from GitHub
wget -O $HOME/diskspaceann/diskspaceann.py "https://raw.githubusercontent.com/StakeTake/disk-space-announces/main/diskspaceann.py": Downloads the script from the specified GitHub repository and saves it as diskspaceann.py in the diskspaceann directory.
Editing the script
nano $HOME/diskspaceann/diskspaceann.py: Edits the script file using the nano text editor. Make sure to add your Discord bot token and the channel ID where the bot will send messages.
Running the script in a screen session
screen -S diskspaceann: Starts a new screen session named "diskspaceann".
python3 $HOME/diskspaceann/diskspaceann.py: Runs the Python script in the screen session.
Detaching from the screen session
Press CTRL+A+D to detach from the screen session and leave the script running in the background.
