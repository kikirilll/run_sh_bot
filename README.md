# run_sh_bot

## Request
I have a server and I want to run some commands there to get the status.

## Solution
I decided to use telegram bot commands to run scripts on servers and get results in telegram too. Bot would work on the same server where I need to run commands.

## Create Telegram bot
I started with creating my Telegram bot. Don't want to describe a lot here, you could you one of thousands of tutorials online.
As a result, you would need a `TOKEN` and your `CHATID`.<br/>💡Note: There is no such entity as a 'private bot'. Everyone will be able to find your bot and start using it. So, there're at least 2 solutions how to prevent someone else use your bot and run commands:
1. Create a group chat with you and your bot and use that chatID to send bot messages there.
2. Use `CHATID` of your and bit private chat (I prefer this option).

## Server side
Keep server updated:
```
$ sudo apt update
```

The bot will be written in Python, and some packages would be needed. First of all, instal pip:
```
$ sudo apt install python3-pip
```

Subprocess.run is used to run commands on the server:
```
$ sudo pip install subprocess.run
```

💡Note: I also need to run commands on another server. So, to run commands on one server from another I'm using Sshpass for this:
```
$ sudo apt-get install sshpass
```

I'm using pyTelegramBotAPI library, because I found it easier for me. Nevertheless, it's pretty flexible:
```
$ pip install pyTelegramBotAPI
```

So, all dependencies have been set up! The last thing that is needed is to run bot.py even if the session is over.
Set up process on background:
```
nohup python3 bot.py &
```

As a result, you'll have a `processID` for your script. Also, you can get it with this command:
```
pidof python3 bot.py
```
To stop the process:
```
kill processID
```

## Notes
1. Yes, it's not secure to have a password inside the code (bad practice), but I needed a fast solution, so it was fine for me. Password could be stored in another file and be linked in the code.
2. In case server would be down, bot won't work and command won't be executed (yeah, obvious). Probably it's better to have bot to be set up on another server. But again, I just needed a fast solution and I didn't care about such things.