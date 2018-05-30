<!--
  Title: PokeBall SelfBot
  Description: This specific selfbot was designed to automatically catch pokemon spawned on Discord by PokeCord bot. It also offers           other utility functions to automate features like trading, releasing, id search, etc. It is inspired by PokecordCatcher and             extends its features to more advanced version with better control.
  Author: Hyperclaw79
  Logo: https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/PokeballSelfbot_Logo.png
  Tags: discord-bot, discord, selfbot, pokeball-selfbot, pokecord, python, pokemon, pokecord-discord-bot, catch-pokemon, pokecord-hack,
        dicord bot, pokecord discord bot, catch pokemon, pokecord hack
-->
<meta name="description" content="This specific selfbot was designed to automatically catch pokemon spawned on Discord by PokeCord bot. It also offers other utility functions to automate features like trading, releasing, id search, etc. It is inspired by PokecordCatcher and extends its features to more advanced version with better control."/>
<meta name="keywords" content="discord-bot, discord, selfbot, pokeball-selfbot, pokecord, python, pokemon, pokecord-discord-bot, catch-     pokemon, pokecord-hack, dicord bot, pokecord discord bot, catch pokemon, pokecord hack"/>
<meta name="author" content="Hyperclaw79"/>
<meta name="url" content="https://github.com/Hyperclaw79/PokeBall-SelfBot" />
<meta name="og:title" content="Pokeball SelfBot"/>
<meta name="og:url" content="https://github.com/Hyperclaw79/PokeBall-SelfBot" />
<meta name="og:image" content=" https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/PokeballSelfbot_Logo.png" />
<meta name="og:description" content="This specific selfbot was designed to automatically catch pokemon spawned on Discord by PokeCord        bot. It also offers other utility functions to automate features like trading, releasing, id search, etc. It is inspired by              PokecordCatcher and extends its features to more advanced version with better control."/>


# PokeBall SelfBot
![logo](https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/PokeballSelfbot_Logo.png)

This specific selfbot was designed to automatically catch pokemon spawned on Discord by PokeCord bot. It also offers other utility functions to automate features like trading, releasing, id search, etc.
It is inspired by [PokecordCatcher](https://github.com/xKynn/PokecordCatcher) and extends its features to more advanced version with better control.

**Current Version**: `v3.2.0`
   > Keep a lookout for [Updates](https://github.com/Hyperclaw79/PokeBall-SelfBot/blob/master/Updates.md). 

## Features
1. Automatically catch a pokemon in whichever server you are in if the PokeCord bot spawns a pokemon.
2. Delay and catch rates to finesse the behaviour of the selfbot.
3. A log command to log all your pokemon along with their numbers.
4. A trade command to bulk trade the pokemon to your main account.
5. Priority List to control the pokemon you catch and trade.
6. Toggle catching of dupliactes.
7. Mass release of thrash pokemon.
8. Toggle autocatching to use in Command_Only mode.
9. Blacklist and Whitelist channels to control the scope of the selfbot. And a toggler function for the switch.
10. Toggle priority_only mode.
11. List out all the legendaries you've caught so far.
12. A gift command to send credits. (isolated to prevent conflict with Trade)
13. Blacklist/Whitelist toggle for entire guilds.
14. Toggle Autolog after catching new pokemon.
15. Case-insensitive Commands. (Args are still sensitive.)

## Requirements
* Python 3.6+
* A server/local sytem to host it.
* A discord account. (Preferably two - one main and one alt)

## Setup
1. First run `setup.bat` to install the requirements.
2. Then, add your bot token in the `config.json`'s `"token"` key. Refer the tutorial below to get the token.
    > The token should be withing the `""` like:
      >> `"token": "Mxy.23e2d3_2er3.sf4t4.....xyz"`
      >> Make sure it's exactly within one pair of `""`.
    > Users deploying it on server, can uncomment the lines 3 and 17 and use the token as an environment variable.   
3. Then simply run `run.bat` to get your bot live.
  > If you are on a mac or linux, directly launch `launcer.py` instead of running the bat file. And use `pip install -r requirements.txt` instead to setup.
4. The autocatcher is **off** by default. To enable it, you need to send a message in Discord as `P^autocatcher on`.
  > `P^` is the default command_prefix for the selfbot. Feel free to change it. Note that, this is not the same as PokeCord's prefix.
  > If you don't want to toggle it on every time after restart, change line 41 to `True` instead of `False`.
5. Most of the commands need you to catch a pokemon in the new guild with autocatcher on, at least once, followed by a restart.
  > There is a way to manually bypass this. You need to turn the Developer Mode on your Discord on, get the guild id and alter `guilds.json` to include the `,guild_id:"pokecord prefix in that guild"`.


## Fine-Tuning
* To find out how to get your token visit [Token Tutorial](https://github.com/TheRacingLion/Discord-SelfBot/wiki/Discord-Token-Tutorial).
* Keep the `catch rate` **low** and `delay` **high** for it to act normally.  
* `Priority` pokemon <u>bypass</u> catch rate.
If a priority pokemon is caught, it will be removed from priority list in the current session, manually remove it from config if you restart.
* Use the `Safe List` to prevent trading some pokemon to your main account in case you want them on the selfbot's account.  
* `Catch Rate` is a percentage out of 100.  
* `Delay` is in seconds.  
* `delay_on_priority` can be set to **true** or **false**, false means it won't wait and will instantly catch a pokemon if its in priority.
* `restrict_duplicates` can be set to **false** to catch unlimited number of duplicates. If **true**, use `max_duplicates` to control the number of duplicates you can catch. 
* `blacklists` and `whitelists` can be filled with the channel ids to choose where the selfbot should work. You can use the `toggle_mode` command to choose which mode it should run in.
* `blacklist_guilds` and `whitelist_guilds` can be filled with the guild ids to filter entire guilds. You can use the `toggle_guildmode` command to choose which mode it should run in.
   > Always keep the default value in the list. It is the id for Official PokeCord Server. 
* `avoid` can be filled with all the pokemons that shouldn't be caught automatically.
* `autolog` can be used to choose whether the `p!pokemon --name FreshlyCaughtPokemon` should be used immediately after catching a new pokemon. To be stealthy, use `false`.
* Use the `pokelog` command before performing a trade in order to sync up all your newly caught pokemon.
* Regularly run `pokelog` to keep the list synchronized. Especially, before `clean_trash` as it might result in releasing the wrong pokemon.
* For args based trading/releasing, always provide the ids in a descending order.
* Preferably run this on an alt and then trade them to you main account.
* To get channel ids, mention you channel in a message and add a `\` before the mention. The integer part of it is the channel id.
    > For example:
      >> Sending `\#pokechannel` will give `<#1234>`.
      >>> In  <#1234>, channel id is 1234.

Example config:
```json
{
  "token": "Mxy.23e2d3_2er3.sf4t4.....xyz",
  "command_prefix": "P^",
  "priority": ["Groudon", "Geodude"],
  "avoid": ["Croagunk", "Trubbish"],
  "catch_rate": 90,
  "delay": 2,
  "delay_on_priority": true,
  "restrict_duplicates": true,
  "max_duplicates": 2,
  "blacklists": [1234567,654356],
  "whitelists": [123456765,435467777],
  "blacklist_guilds": [382316968394620938],
  "whitelist_guilds": [],
  "autolog": true
}
```

## Disclaimer
* The creators of this bot are not responsible for any actions you perform using it. Use it at you own risk.
* Selfbots violate discord & PokeCord TOS and you can get banned. Be careful about how you use the bot.
* Do not use this in official PokeCord Discord server.... for obvious reasons.

## Contributions
Refer to the new [CONTRIBUTION GUIDE](https://github.com/Hyperclaw79/PokeBall-SelfBot/blob/master/CONTRIBUTING.md).
Also, refer to [Issue Template](https://github.com/Hyperclaw79/PokeBall-SelfBot/blob/master/.github/ISSUE_TEMPLATE/basic-issue-template.md) and [PR Template](https://github.com/Hyperclaw79/PokeBall-SelfBot/blob/master/PULL_REQUEST_TEMPLATE.md).

Best ways to contribute apart from Issues and PRs:
+ **Donations**

  <a href="http://paypal.me/Hyperclaw79"><img src="https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/pikadonor.png" width="100" height="100" alt="Feature Requests"/></a>

+ **Starring the Repo**

  <img src="https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/pikastar.png" width="100" height="100" alt="Feature Requests"/>

+ **Referrals**

## Feature Requests
You can request **new features** in the FeatHub.

  <a href="http://feathub.com/Hyperclaw79/PokeBall-SelfBot"><img src="https://cdn.rawgit.com/Hyperclaw79/PokeBall-SelfBot/8da8c6dd/pika%2B1.png" width="100" height="100" alt="Feature Requests"/></a>

## Acknowledgements
### Creators
* xKynn for the [PokeCordCatcher](https://github.com/xKynn/PokecordCatcher).
* Rapptz for [Discord.py](https://github.com/Rapptz/discord.py)

### Donors
* August.0 [Advanced]
* SwiftBrass
* Leschx [Advanced]
* KappaBotter [Advanced]
* BestGunner [Advanced]
* Matt
* DaddyNew
* Damned [Advanced]

## Donations
* The public version of this selfbot doesn't contain the following to keep the bot usage to minimum and not break Pokecord bot:
  + Auto-Spammer [Major]
  + Trade Offer Generator
  + Auto-dueler for Credits farming [Major]
  + Logging catches to owner's DMs in multimode
  > *These features are based upon multimode which involves having multiple selfbot accounts.*
* To avail these features, contact me on Discord @**Hyperclaw79#3570** and I'll give you my PayPal id. 
  > *Please ping me only for donations and not for support (unless you are already a donor). Currently the price is just $12. Better donate fast as the price will be bound to go up along with the demand.*
* The other **advantages** upon being a donor would be:
  + Be the first to avail any bug fixes and new updates.
  + A special mention of your username in this readme. *(optional)*
  + Bot related Support on Discord DMs. (Don't ask me how to install Python xD)
    + >*This version is to suggested to be used after you've tried out the public version.*
    + >*The support doesn't include how to setup the public bot. Use [GitHub Issues](https://github.com/Hyperclaw79/PokeBall-SelfBot/issues) for that one.
  + You can propose new features and I shall implement them *based on the plausibilty*.
* **Advanced Extension**
  + The premium version also got an advanced extension which adds more game to the bot.
    It contains the following features:
    + This one works on a multi-user mode with 3+ bots. It follows a master-slave system where one master bot can trigger the commands on multiple slave selfbots.
    + `Best_stats` command to check for the pokemon which has the best total stats or a specific stat like Speed, Attack among your fav list or list of ids. Pretty useful for the traders.
    + `Incubate` command to automatically level up all the pokemon in your fav list or list of ids, through the autospammer module. You don't need to check for the level of your pokemon and manually switch to the next one anymore.
    + `iter` command to chain a series of pokecord commands for a list of ids.
    + `sudo_exec` and `sudo_echo` commands for the master-slave control.
  + The current price for this extension is just $8 and will change with demand, just like the premium version.  
* **Terms & Conditions apply**:
  + You shall receive the source code and deployment instructions after the payment has been acknowledged.
  + You shall not disclose the obtained code to anyone directly. Refer them to this repo instead.
    > The obtained code is not open-source and MIT License doesn't apply to it.
  + Support is subject to my availability.
  + Not all requested features are possible to implement.
  + Since Pokecord keeps updating, some of the older code might break. Stay patient till I send you a patch for it.
  + All donations are non-refundable.
  + Me or the contributors for this repo and not responsible for any legal suits.

* If you'd like to simply donate to support the cause instead of buying the Premium Version, you can always send me your support. Click that image below.

  <a href="https://www.paypal.me/hyperclaw79"><img src="https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/pikadonor.png" width="100" height="100" alt="Feature Requests"/></a>

Don't forget to let me know that you're the one who paid it. ;)

## Referrals
* If you refer this to another person and they successfully donate to this repo, you will get the option to choose *one* of the following benefits:
    + Trade Offer Generator module for free.
    + A 5% discount while donating in the future.
* DM me on Discord with the name of the person you referred to and ask them to include your username too while contacting me about the donation.
* You need to also Star this repo before referring to others.
* Maximum number of stackable discounts would be 2, i.e., maximum possible discount would be 10%.
* The benefits are provided only **after** the referred person makes a donation.
* The discount rate is subject to change based on the referral activity and donation price.
