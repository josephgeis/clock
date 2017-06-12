# clock :octocat:
A clock for Pimoroni's Display-O-Tron HAT (for Raspberry Pi)

[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/juniorRubyist)

## Installation :package:
```bash
git clone https://github.com/juniorRubyist/clock.git
cd clock
./install.sh # Follow onscreen instructions
```
Please leave a star, it means a lot to me.

## Upgrade :arrow_up:
```bash
git pull # While in project directory
./install.sh
```

## Features
* Absolutely no logic for accurate time updates. 
* Runs in background, with help from `screen`. 
* Can run on startup, with `crontab` configuration. 

```
••••••••••••••••••
•    02:47 pm    • Local Time
•     ••••••     • Binary Seconds
•  Jun 08, 2017  • Local Date
••••••••••••••••••
```

## Usage

### Commands :keyboard:
To start clock, execute:
```bash
clock
```

To attach to the clock process, execute:
```bash
screen -r clock
```

To kill the clock, execute:
```bash
screen -r clock
# Send a SIGINT (^C), SIGTSTP (^Z), or SIGKILL (^\\)
```

### Other Usage :bulb:
To initiate the backlight, press the center button.

To switch backlight colors, press the left/right buttons, when _not_ glowing.

## Hacking :hammer:

### Adding Colors
1. Fork the repo (not required, but recommended) and clone it, __or__ pull the latest changes (if you don't want to fork it).
2. Open `share/clock.py` with an editor.
3. Find the `colors` list and add a dictionary with the following syntax (which is similar to JSON).
```python
{'name' : color_name, 'combo' : (r, g, b)}
```
:warning: __Warning:__ It is _imperative_ that `color_name` is a string and the value of `combo` is a tuple.
4. Save the file and reinstall (run `./install.sh`).
__Note:__ Make sure you kill the existing process.

### Sharing Edits and Feature Requests
To share an edit, please push your changes and file a pull request.
If you have a good idea, but don't know how to add it, file an issue. If accepted, we'll add it to the `Next Steps` project.

#### Do you love this? :heart:
If you have enjoyed this project, please leave a star or a [comment on my Say Thanks page](https://saythanks.io/to/juniorRubyist). You can also donate Bitcoin to the address below :point_down:.
```
1JS7RBqqWu5oCUzNfJnAHfkxBC5cPRew8u
```

## Contributions
* Joseph Geis ([@juniorRubyist](https://github.com/juniorRubyist)): Project Owner

Coded with love from California.
