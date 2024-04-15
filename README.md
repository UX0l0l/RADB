# Resource Allocator Discord Bot
Simple bot that can copy all messages from a channel to a different channel as long as the bot has access to them (bot must be in the server(s) containing the channels and have adequate permissions to view, read, and send messages in them)

## Installation/Setup
First, start off by cloning the repository using git, then cd into the cloned directory and install the required dependencies using pip:

```bash
git clone https://github.com/UX0l0l/RADB.git
cd RADB
pip install -r requirements.txt
```

Second, go to the [Discord developers page](https://discord.com/developers/applications/) and create a new application. Then, proceed to set up the bot, add whatever permissions you need in the installation tab, then proceed to invite it to the servers you need it in using the Discord provided install link. You can also add whatever custom name, profile picture, etc to your bot during this step.

After the initial setup is done, create a new .env file in the cloned directory with the same format of the .env file in the repository, and paste in the bot's token, and the IDs of both channels that you want to use, then save the file.

Finally, run the script using `python3 bot.py`

If all the steps were executed correctly, the script should run smoothly and copy all the messages from the source channel to the target channel successfully.
