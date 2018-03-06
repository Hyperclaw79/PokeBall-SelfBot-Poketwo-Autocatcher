# PokeBall SelfBot
This selfbot is an extension of [PokecordCatcher](https://github.com/xKynn/PokecordCatcher) which catches pokemon when they are spawned by the Pokecord discord bot.  

## Features
1. Automatically catch a pokemon in whichever server you are in if the PokeCord bot spawns a pokemon.
2. Delay and catch rates to finesse the behaviour of the selfbot.
3. A log command to log all your pokemon along with their numbers.
4. A trade command to bulk trade the pokemon to your main account.
5. Priority and Safe List to control the pokemon you catch and trade.

## Requirements
* Python 3.6+
* A server/local sytem to host it.
* A discord account. (Preferably two - one main and one alt)

## Setup

1. First replace the `os.environ["DISCORD_BOT_TOKEN"]` in `secret.py` with your bot token. Refer the tutorial below to get the token.
2. Run `setup.bat` to install the requirements.
3. Then simply run `run.bat` to get your bot live.

> If you are on a mac or linux, directly launch `launcer.py` instead of running the bat file. And use `pip install -r requirements.txt` instead to setup.

## Fine-Tuning

* Keep the `catch rate` **low** and `delay` **high** for it to act normally.  
* `Priority` pokemon <u>bypass</u> catch rate.
If a priority pokemon is caught, it will be removed from priority list in the current session, manually remove it from config if you restart.
* Use the `Safe List` to prevent trading some pokemon to your main account in case you want them on the selfbot's account.  
* `Catch Rate` is a percentage out of 100.  
* `Delay` is in seconds.  
* `delay_on_priority` can be set to **true** or **false**, false means it won't wait and will instantly catch a pokemon if its in priority.  
* Preferably run this on an alt and then trade them to you main account.
* Use the `pokelog` command before performing a trade in order to sync up all your newly caught pokemon.

Example config:
```json
{
  "token": "<your token>",
  "command_prefix": "P^",
  "priority": ["Groudon", "Geodude"],
  "safe_list": ["Mew"],
  "catch_rate": 90,
  "delay": 2,
  "delay_on_priority": true
}
```

## Disclaimer
* The creators of this bot are not responsible for any actions you perform using it. Use it at you own risk.
* Selfbots violate discord TOS and you can get banned. Be careful about how you use the bot.
* Do not use this in official PokeCord Discord server.... for obvious reasons.

## Contributions
If you find any bugs or would like to add new features or somehow improve the code, feel free to open an Issue or a Pull Request.

## Acknowledgements
* xKynn for the [PokeCordCatcher](https://github.com/xKynn/PokecordCatcher).
* Rapptz for [Discord.py](https://github.com/Rapptz/discord.py)