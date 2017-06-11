# clock
A clock for Pimoroni's Display-O-Tron HAT (for Raspberry Pi)

## Installation
```bash
git clone https://github.com/juniorRubyist/clock.git
cd clock
./install.sh # Follow onscreen instructions
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