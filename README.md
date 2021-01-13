<!--
  Title: PokeBall SelfBot
  Description: This specific selfbot was designed to automatically catch Pokemon spawned on Discord by PokeCord bot. It also offers other utility functions to automate features like trading, releasing, ID search, etc. Apart from autocatching, the bot extends its features to more advanced version with better control.
  Author: Hyperclaw79
  Logo: https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/PokeballSelfbot_Logo.png
  Tags: discord-bot, discord, selfbot, pokeball-selfbot, pokecord, python, pokemon, pokecord-discord-bot, catch-pokemon, pokecord-hack,
        discord bot, pokecord discord bot, catch pokemon, pokecord hack, discord-bot, pokecord-bot, autocatcher, premium, auto-trade,
        donations, pokecord-catcher, pokecord-autocatcher, pokecord-selfbot
-->
<meta name="description" content="This specific selfbot was designed to automatically catch Pokemon spawned on Discord by PokeCord bot. It also offers other utility functions to automate features like trading, releasing, ID search, etc. Apart from autocatching, the bot extends its features to more advanced version with better control."/>
<meta name="keywords" content="discord-bot, discord, selfbot, pokeball-selfbot, pokecord, python, pokemon, pokecord-discord-bot, catch-pokemon, pokecord-hack, discord bot, pokecord discord bot, catch pokemon, pokecord hack, discord-bot, pokecord-bot, autocatcher, premium, auto-trade, donations, pokecord-catcher, pokecord-autocatcher, pokecord-selfbot"/>
<meta name="author" content="Hyperclaw79"/>
<meta name="url" content="https://github.com/Hyperclaw79/PokeBall-SelfBot" />
<meta name="og:title" content="Pokeball SelfBot"/>
<meta name="og:url" content="https://github.com/Hyperclaw79/PokeBall-SelfBot" />
<meta name="og:image" content=" https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/PokeballSelfbot_Logo.png" />
<meta name="og:description" content="This specific selfbot was designed to automatically catch Pokemon spawned on Discord by PokeCord bot. It also offers other utility functions to automate features like trading, releasing, ID search, etc. Apart from autocatching, the bot extends its features to more advanced version with better control."/>
<meta name="google-site-verification" content="EEaJ4rxZqFULJehFinFFOpxt75EdXvYh-bE2t3FoADA" />


# PokeBall SelfBot
![Python Version](https://img.shields.io/badge/python-3.8-blue.svg?style=for-the-badge) ![License](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge) ![Maintained?](https://img.shields.io/badge/Maintained%3F-Premium%20Version+-red.svg?style=for-the-badge) ![Donor Count](https://img.shields.io/badge/Donations%20Count-268-yellow?style=for-the-badge)
<img src="https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/finalLogo.png" width="500" />

This specific selfbot was designed to automatically catch Pokemon spawned on Discord by PokeCord bot. It also offers other utility functions to automate features like trading, releasing, ID search, etc. Apart from autocatching, the bot extends its features to more advanced version with better control.

![It actually works lol](https://github.com/Hyperclaw79/PokeBall-SelfBot-Pokecord-Automation/raw/master/assets/New%20Pokeball%20Selfbot.gif)

**Current Version**: `v3.3.2` (13th June 2018)

**Premium Version**: `v7.0.0` (30th October 2020) (Autocatcher uses Artificial Intelligence now!)
  > **The `autocatcher` is now officially fixed and is a Premium Version only feature.**
  It was troublesome fixing this again and again as the open source code is easily readable and patched against. To avoid this in the future, autocatcher is now a Premium feature to make it harder to get. I know that most of you will hate this move, but it was necessary. You guys can continue using the other features like auto-trade and auto-release, etc. which do not really harm anyone.
Thank you all for being patient and sticking around until now.

> **The Public Version is now intended for testing only.**
After the recent Pokecord updates, the selfbot commands are being flagged by pokecord and the account using it will most likely get reset. So use this only on your alts and to check how the bot is working. If you want a stealth mode which makes the selfbot commands un-flaggable, please switch to the Premium Version which has a mechanism to avoid this.

**After the recent changes in PokeRealm and PokeTwo, hashes will definitely fail. Pleased to announce that this is the only selfbot which employes the power of Artificial Intelligence to detect pokemons!**
> Has as astounding accuracy of 99% on PokeTwo spawns which are impossible to be caught by any other selfbot. PokeRealm spawns can be captured as well with the same code.

The donations for Premium Version are open again.

Scroll down to [Donations section](https://github.com/Hyperclaw79/PokeBall-SelfBot#donations) for details.
So if you want the autocatcher along with other amazing commands, DM me on Discord for the PayPal details after reading the [donations section](https://github.com/Hyperclaw79/PokeBall-SelfBot/blob/master/README.md#donations).

## Features
1. Automatically catch a Pokemon in whichever server you are in if the PokeCord bot spawns a Pokemon. [Premium Only]
2. Delay and catch rates to finesse the behaviour of the selfbot.
3. A log command to log all your Pokemon along with their numbers.
4. A trade command to bulk trade the Pokemon to your main account.
5. Priority List to control the Pokemon you catch and trade.
6. Toggle catching of duplicates.
7. Mass release of thrash Pokemon. (Limited)
8. Toggle autocatching to use in Command_Only mode.
9. Blacklist and Whitelist channels to control the scope of the selfbot. And a toggler function for the switch.
10. Toggle priority_only mode.
11. List out all the legendaries you've caught so far.
12. A gift command to send credits. (isolated to prevent conflict with Trade)
13. Blacklist/Whitelist toggle for entire guilds.
14. Toggle Autolog after catching new Pokemon.
15. Case-insensitive Commands. (Args are still sensitive.)
16. Auto-updates available.

## Requirements
* Python 3.7
* A server/local sytem to host it.
* A discord account. (Preferably two - one main and one alt)

## Setup
### Windows
1. [First install Git for Windows](https://git-scm.com/download/win) and then run `setup.bat` to install the requirements.
2. Then, add your bot token in the `config.json`'s `"token"` key. Refer the tutorial below to get the token.
    > The token should be withing the `""` like:
      >> `"token": "Mxy.23e2d3_2er3.sf4t4.....xyz"`
      >> Make sure it's exactly within one pair of `""`.
    > Users deploying it on server, can uncomment the lines 3 and 17 and use the token as an environment variable.   
3. Then simply run `run.bat` to get your bot live.
  > If you are on a mac, directly launch `launcher.py` instead of running the bat file. And use `pip install -r requirements.txt` instead to setup.
4. The autocatcher is **off** by default. To enable it, you need to send a message in Discord as `P^autocatcher on`.
  > `P^` is the default command_prefix for the selfbot. Feel free to change it. Note that, this is not the same as PokeCord's prefix.
  > If you don't want to toggle it on every time after restart, look for the line `self.autocatcher = False` under the `__init__()` function and change it to `True` instead of `False`.
5. Most of the commands need you to catch a Pokemon in the new guild with autocatcher on, at least once, followed by a restart.
  > There is a way to manually bypass this. You need to turn the Developer Mode on your Discord on, get the guild ID and alter `guilds.json` to include the `,guild_id:"pokecord prefix in that guild"`.
### Linux
1. First install git by doing "sudo apt install git-all", cd to directory, and then run "setup.sh" with "./setup.sh". Make sure to give permission to "setup.sh" and "run.sh" by "chmod +x [file name here]".
2. Then follow step number "2" in the "Windows" section above.
3. Finally, run "run.sh" to get your self-bot online and running. Now you can configure stuff and enjoy.
## Fine-Tuning
* To find out how to get your token visit [Token Tutorial](https://github.com/TheRacingLion/Discord-SelfBot/wiki/Discord-Token-Tutorial).

### Configs explanations:

  * Keep the `catch rate` **low** and `delay` **high** for it to act normally.  
  * `Priority` Pokemon <u>bypass</u> catch rate.
  If a priority Pokemon is caught, it will be removed from priority list in the current session, manually remove it from config if you restart.
  * Use the `Safe List` to prevent trading some Pokemon to your main account in case you want them on the selfbot's account.  
  * `Catch Rate` is a percentage out of 100.  
  * `Delay` is in seconds.  
  * `delay_on_priority` can be set to **true** or **false**, false means it won't wait and will instantly catch a Pokemon if it is in priority.
  * `restrict_duplicates` can be set to **false** to catch unlimited number of duplicates. If **true**, use `max_duplicates` to control the number of duplicates you can catch. 
  * `blacklists` and `whitelists` can be filled with the channel IDs to choose where the selfbot should work. You can use the `toggle_mode` command to choose which mode it should run in.
  * `blacklist_guilds` and `whitelist_guilds` can be filled with the guild IDs to filter entire guilds. You can use the `toggle_guildmode` command to choose which mode it should run in.
    > Always keep the default value in the list. It is the ID for Official PokeCord Server. 
  * `avoid` can be filled with all the Pokemon that shouldn't be caught automatically.
  * `autolog` can be used to choose whether the `p!pokemon --name FreshlyCaughtPokemon` should be used immediately after catching a new Pokemon. To be stealthy, use `false`.
  * `update_checker` can be set to `false` if you don't wanna bother checking for new updates.
    > Highly unrecommended.
  * `auto_update` can be set to `false` to disable automatic update of code and other files.
    > You will need to manually re-clone the repo and make modifications in your config again if disabled.
      Auto-updater makes sure that your previous configs stay intact and only makes additions.  

* Use the `pokelog` command before performing a trade in order to sync up all your newly caught Pokemon.
* Regularly run `pokelog` to keep the list synchronized. Especially, before `clean_trash` as it might result in releasing the wrong Pokemon.
* For args based trading/releasing, always provide the IDs in a descending order.
* Preferably run this on an alt and then trade them to you main account.
* To get channel IDs, mention you channel in a message and add a `\` before the mention. The integer part of it is the channel ID.
    > For example:
      >> Sending `\#pokechannel` will give `<#1234>`.
      >>> In  <#1234>, channel ID is 1234.

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
  "autolog": true,
  "update_checker": true,
  "auto_update": true
}
```

## Disclaimer
* The creators of this bot are not responsible for any actions you perform using it. Use it at you own risk.
* Selfbots violate discord & PokeCord TOS and you will get banned if caught using them. Be careful about how you use the bot.
  > The selfbot is intended to give you a boost and get the edge over your friends, not hoard 40K pokemon lol.
* Do not use this in official PokeCord Discord server.... for obvious reasons.
  > Similarly do not use in public servers which explicitly prohibit this.
* The implications of ban might also affect other accounts which interact with this selfbot. Use with caution.  


## Donations
* The public version of this selfbot doesn't contain the following to keep the bot usage to minimum and not break Pokecord bot:
  + Auto-Catcher [Major] 
  + Auto-Spammer [Major]
  + Mass seller [with IV lock and more options]
  + Auto-dueler for Credits farming [Major]
  + Logging catches to owner's DMs in multimode
  + Help command that displays usage instruction for other commands. [Major]
  + Trade command can use Pokemon names as args
  + DM commands - some commands can be used by DMing the bot.
  + Stealth from Pokecord
  + Full Disclosure of Source Code [Major]
  + Unlimited usage (no time trails) [Major]
  + Autobuy Rare Candies
  + Autoclaim newly caught Pokemon on pokedex
  + Autofav pokemons with total IV above desired IV.
  + Autosleep
  
  > *These features are based upon multimode which involves having multiple selfbot accounts.*
* To avail these features, contact me on Discord @**Hyperclaw79#3476** and I'll give you my PayPal ID. 
  *Please ping me only for donations and not for support (unless you are already a donor). Currently the price is just $25. Better donate fast as the price will be bound to go up along with the demand.*
  *In your DM message, use the keyword `#Premium` to let me know that you've read the Readme.*
* The other **advantages** upon being a donor would be:
  + Be the first to avail any bug fixes and new updates.
  + A special mention of your username in this readme. *(optional)*
  + Bot related Support on Discord DMs. (Don't ask me how to install Python xD)
    + >~~*This version is to suggested to be used after you've tried out the public version.*~~
    + >*The support doesn't include how to setup the public bot. Use [GitHub Issues](https://github.com/Hyperclaw79/PokeBall-SelfBot/issues) for that one.
  + You can propose new features and I shall implement them *based on the plausibilty*.
* **Advanced Extension**
  + The premium version also got an advanced extension which adds more game to the bot.
    It contains the following features:
    + This one works on a multi-user mode with 3+ bots. It follows a master-slave system where one master bot can trigger the commands on multiple slave selfbots.
    + `Best_stats` command to check for the Pokemon which has the best total stats or a specific stat, like Speed, Attack, etc., among your fav list or list of IDs. Pretty useful for the traders.
    + `Incubate` command to automatically level up all the Pokemon in your fav list or list of IDs, through the autospammer module. You don't need to check for the level of your Pokemon and manually switch to the next one anymore.
    + `iter` command to chain a series of pokecord commands for a list of IDs.
    + `sudo_exec` and `sudo_echo` commands for the master-slave control.
    + `sudo_duel` command for launching multiple duels at once.
  + The current price for this extension is just $10 and will change with demand, just like the premium version.  
* **Terms & Conditions apply**:
  + You shall receive the source code and deployment instructions after the payment has been acknowledged.
  + You shall not disclose the obtained code to anyone directly. Refer them to this repo instead.
    > The obtained code is not open-source and MIT License doesn't apply to it.
  + Support is subject to my availability.
  + Not all requested features are possible to implement.
  + Since Pokecord keeps updating, some of the older code might break. Stay patient until I send you a patch for it.
  + All donations are non-refundable.
  + Me or the contributors for this repo and not responsible for any legal suits.

* If you'd like to simply donate to support the cause instead of buying the Premium Version, you can always send me your support. Click that image below.

  <a href="https://www.paypal.me/hyperclaw79"><img src="https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot/master/assets/pikadonor.png" width="100" height="100" alt="Feature Requests"/></a>

Don't forget to let me know that you're the one who paid it. ;)

## Referrals
* If you refer this to another person and they successfully purchase the Premium Version or above, you will get:
    + A 5% discount per referral while donating in the future.
* DM me on Discord with the name of the person you referred to and ask them to include your username too while contacting me about the donation.
* You need to also Star this repo before referring to others.
* Maximum number of stackable discounts would be 4, i.e. maximum possible discount would be 20%.
* The benefits are provided only **after** the referred person makes a donation.
* The discount rate is subject to change based on the referral activity and donation price.

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
* Rapptz for [Discord.py](https://github.com/Rapptz/discord.py)

### Contributors
* [ThePythonDoge](https://github.com/ThePythonDoge)
* [4-mat](https://github.com/4-mat)
* [ajmeese7](https://github.com/ajmeese7)
* [KKonas](https://github.com/Kkonas)

### Testimonials
![testimonial](https://raw.githubusercontent.com/Hyperclaw79/PokeBall-SelfBot-Pokecord-Automation/master/assets/testimonial.gif)

### Donors


| No.| Alias         | Version     |
|----| ------------  | ----------  |
| 1  |  August.0     | Advanced 💎 |
| 2  | SwiftBrass    | Premium  💵 |
| 3  | Leschx        | Advanced 💎 |
| 4  | KappaBotter   | Advanced 💎 |
| 5  | BestGunner    | Advanced 💎 |
| 6  | Matt          | Premium  💵 |
| 7  | DaddyNew      | Premium  💵 |
| 8  | Damned        | Advanced 💎 |
| 9  | Flamlier      | Premium  💵 |
| 10 | NM135         | Advanced 💎 |
| 11 | Rooster       | Premium  💵 |
| 12 | L1ghtblade    | Advanced 💎 |
| 13 | ipwner        | Advanced 💎 |
| 14 | Nick          | Premium  💵 |
| 15 | Skiel         | Premium  💵 |
| 16 | Robin         | Premium  💵 |
| 17 | ScriptKiddie  | Advanced 💎 |
| 18 | Jakob         | Advanced 💎 |
| 19 | kReaz         | Advanced 💎 |
| 20 | Khymaera      | Premium  💵 |
| 21 | ClueSkull     | Premium  💵 |
| 22 | Tortoises     | Premium  💵 |
| 23 | Soldier40     | Premium  💵 |
| 24 | Beanie        | Premium  💵 |
| 25 | Pablo         | Premium  💵 |
| 26 | Noel          | Premium  💵 |
| 27 | Void          | Premium  💵 |
| 28 | Kyros         | Premium  💵 |
| 29 | Tri           | Premium  💵 |
| 30 | Snorlax       | Premium  💵 |
| 31 | Zope_RSM      | Premium  💵 |
| 32 | Inori         | Advanced 💎 |
| 33 | Jessie        | Premium  💵 |
| 34 | Fisa 51       | Premium  💵 |
| 35 | Daddy         | Advanced 💎 |
| 36 | Ariusll       | Advanced 💎 |
| 37 | Obelisk       | Advanced 💎 |
| 38 | NightX        | Premium  💵 |
| 39 | Weapon X      | Premium  💵 |
| 40 | Pokester      | Advanced 💎 |
| 41 | Naruto0       | Premium  💵 |
| 42 | KaiDmore      | Advanced 💎 |
| 43 | G.e.n.c.h     | Advanced 💎 |
| 44 | Takeen        | Advanced 💎 |
| 45 | NopeW         | Advanced 💎 |
| 46 | Coyote        | Premium  💵 |
| 47 | VA_Charm      | Premium  💵 |
| 48 | TimeTitan     | Premium  💵 |
| 49 | Y !-          | Premium  💵 |
| 50 | Anonymous     | Advanced 💎 |
| 51 | XaoBlackbirdz | Premium  💵 |
| 52 | MagicalChaos  | Advanced 💎 |
| 53 | Dranzer       | Advanced 💎 |
| 54 | Liemal        | Premium  💵 |
| 55 | GarryPeanut   | Premium  💵 |
| 56 | Ethanol       | Advanced 💎 |
| 57 | DanceMusic    | Premium  💵 |
| 58 | Gorgeous      | Premium  💵 |
| 59 | RegisteredDad | Advanced 💎 |
| 60 | Plido         | Premium  💵 |
| 61 | Taichi        | Premium  💵 |
| 62 | JBKuma        | Advanced 💎 |
| 63 | ManlyDeer     | Advanced 💎 |
| 64 | Pikachiha     | Premium  💵 |
| 65 | SatanicCat    | Premium  💵 |
| 66 | Vaderson      | Advanced 💎 |
| 67 | Mackaw        | Premium  💵 |
| 68 | Caliber       | Premium  💵 |
| 69 | Kayosu        | Premium  💵 |
| 70 | Garbage       | Premium  💵 |
| 71 | KawfeeMan     | Premium  💵 |
| 72 | Steppin       | Premium  💵 |
| 73 | Clonemon      | Advanced 💎 |
| 74 | Whocome       | Premium  💵 |
| 75 | Kazitov       | Premium  💵 |
| 76 | Errorcast     | Premium  💵 |
| 77 | Abopp         | Premium  💵 |
| 78 | McFlippy      | Premium  💵 |
| 79 | Mr. Stealth   | Premium  💵 |
| 80 | Jewsus        | Premium  💵 |
| 81 | ImageletC     | Advanced 💎 |
| 82 | Kanairo       | Premium  💵 |
| 83 | DestinyCave   | Premium  💵 |
| 84 | Poombamom     | Premium  💵 |
| 85 | Gentle7an     | Premium  💵 |
| 86 | SuTuMuKu      | Premium  💵 |
| 87 | Pokechibi     | Premium  💵 |
| 88 | Syerahn       | Premium  💵 |
| 89 | Nausea3Max    | Premium  💵 |
| 90 | Winterland    | Premium  💵 |
| 91 | TelescopicGem | Premium  💵 |
| 92 | DeathPaint    | Premium  💵 |
| 93 | FamilyFire%d3 | Advanced 💎 |
| 94 | Kitsune       | Advanced 💎 |
| 95 | Maukingino    | Premium  💵 |
| 96 | MortiemRickus | Advanced 💎 |
| 97 | Waterie       | Premium  💵 |
| 98 | ForgetfulVoid | Premium  💵 |
| 99 | Sayruhruruh69 | Premium  💵 |
| 100 | PandaCoffee  | Premium  💵 |
| 101 | Sensei       | Premium  💵 |
| 102 | Spongebob    | Premium  💵 |
| 103 | XZuluXed     | Premium  💵 |
| 104 | TrickySleeve | Premium  💵 |
| 105 | Ao-sama      | Premium  💵 |
| 106 | IntrudePoop  | Premium  💵 |
| 107 | Toyleg       | Premium  💵 |
| 108 | JohnnySins   | Premium  💵 |
| 109 | UnknownKanji | Premium  💵 |
| 110 | AnoOtoko     | Advanced 💎 |
| 111 | DoperPop     | Premium  💵 |
| 112 | WoodenCandle | Premium  💵 |
| 113 | Tylimb       | Premium  💵 |
| 114 | C3H6N6O6     | Premium  💵 |
| 115 | Armadillo    | Premium  💵 |
| 116 | DrumyZart    | Premium  💵 |
| 117 | Tornado      | Advanced 💎 |
| 118 | CoffeeAids   | Premium  💵 |
| 119 | LongNeccing  | Premium  💵 |
| 120 | CountJesus   | Premium  💵 |
| 121 | WonderJames  | Premium  💵 |
| 122 | GrassySitmu  | Premium  💵 |
| 123 | CherryMaddi  | Premium  💵 |
| 124 | ThunderDoggo | Advanced 💎 |
| 125 | TheGrimer    | Premium  💵 |
| 126 | MandyBatson  | Advanced 💎 |
| 127 | OddlySane    | Premium  💵 |
| 128 | XSciFi       | Premium  💵 |
| 129 | Spring783    | Premium  💵 |
| 130 | Squealer     | Premium  💵 |
| 131 | CabelHabibi  | Advanced 💎 |
| 132 | GaspinBrave  | Advanced 💎 |
| 133 | PorkLoaf     | Premium  💵 |
| 134 | SlimeDesuKa  | Premium  💵 |
| 135 | GunnedParent | Premium  💵 |
| 136 | Snapcraft    | Premium  💵 |
| 137 | PaperAngel   | Premium  💵 |
| 138 | JSGodRB      | Premium  💵 |
| 139 | PoochyBella  | Premium  💵 |
| 140 | Plajuda      | Premium  💵 |
| 141 | Ouldm@n      | Advanced 💎 |
| 142 | Hazukashi    | Premium  💵 |
| 143 | PotatoDude   | Advanced 💎 |
| 144 | Moesin       | Premium  💵 |
| 145 | BurningHen   | Premium  💵 |
| 146 | Hollowetsu   | Advanced 💎 |
| 147 | YiteRabt.py  | Advanced 💎 |
| 148 | MarcStark    | Premium  💵 |
| 149 | AvengersIW   | Premium  💵 |
| 150 | NoWinchester | Premium  💵 |
| 151 | Rivery       | Advanced 💎 |
| 152 | RayXX        | Advanced 💎 |
| 153 | AC2AB2BC2    | Advanced 💎 |
| 154 | Favonius     | Premium  💵 |
| 155 | DoggoFuji    | Advanced 💎 |
| 156 | SeasameSt    | Advanced 💎 |
| 157 | Pathiple     | Advanced 💎 |
| 158 | Appyster     | Advanced 💎 |
| 159 | Mr.Xiaomi    | Premium  💵 |
| 160 | Reeling      | Premium  💵 |
| 161 | Fanooth      | Advanced 💎 |
| 162 | AnnoDomini   | Premium  💵 |
| 163 | Fempasta     | Premium  💵 |
| 164 | Mandela      | Advanced 💎 |
| 165 | Vidfilext    | Premium  💵 |
| 166 | Commercial   | Premium  💵 |
| 167 | Rudolph      | Advanced 💎 |
| 168 | DeltaSilver  | Advanced 💎 |
| 169 | DunkinDonut  | Premium  💵 |
| 170 | VeryGlobal   | Premium  💵 |
| 171 | EchoBirb     | Premium  💵 |
| 172 | Owopunch     | Advanced 💎 |
| 173 | Duokami      | Advanced 💎 |
| 174 | ChingChongXP | Advanced 💎 |
| 175 | MinionLove   | Premium  💵 |
| 176 | Jojopanzee   | Premium  💵 |
| 177 | RavenBurger  | Premium  💵 |
| 178 | TangentBeta  | Premium  💵 |
| 179 | Wresort      | Advanced 💎 |
| 180 | SlothLot3000 | Premium  💵 |
| 181 | NoticeMe∆    | Premium  💵 |
| 182 | KrissArcbine | Premium  💵 |
| 183 | UhohWeDidIt  | Advanced 💎 |
| 184 | MarvelFlash  | Premium  💵 |
| 185 | HiddenChain  | Premium  💵 |
| 186 | Shinoboi     | Premium  💵 |
| 187 | GameXCodex   | Advanced 💎 |
| 188 | BoomChica    | Advanced 💎 |
| 189 | MortalCrown  | Premium  💵 |
| 190 | RNGormie     | Premium  💵 |
| 191 | Grandevor    | Premium  💵 |
| 192 | GuiltyClark  | Premium  💵 |
| 193 | AoNoMaou     | Premium  💵 |
| 194 | Anthonie#8407(232167484940091402) | Scammer! |
| 195 | Senior1Crab  | Premium  💵 |
| 196 | PawsOfDeath  | Premium  💵 |
| 197 | Bmw1Series   | Advanced 💎 |
| 198 | VideoOff     | Advanced 💎 |
| 199 | Yes_Warp     | Advanced 💎 |
| 200 | BirbFakes    | Advanced 💎 |
| 201 | Jeapord      | Premium  💵 |
| 202 | Farinheat    | Premium  💵 |
| 203 | AyeDee       | Advanced 💎 |
| 204 | ZebraYen     | Premium  💵 |
| 205 | ScreamAww    | Premium  💵 |
| 206 | SisMac       | Premium  💵 |
| 207 | Lowten#4918(174171205115445248) | Scammer! |
| 208 | SupCage      | Premium  💵 |
| 209 | GreekCake    | Premium  💵 |
| 210 | UntightMan   | Premium  💵 |
| 211 | 𝓜𝓻𝓒𝓮𝓻𝓫𝓮𝓻𝓾𝓼#0666(607806601105113110) | Scammer! |
| 212 | LuvTrio      | Premium  💵 |
| 213 | Wraserface   | Premium  💵 |
| 214 | RackShaper   | Premium  💵 |
| 215 | SpeedyBoi    | Premium  💵 |
| 216 | SocialAgent  | Premium  💵 |
| 217 | ShindaGami   | Premium  💵 |
| 218 | 50Strokes    | Premium  💵 |
| 219 | Cahytion     | Premium  💵 |
| 220 | Mystrixo     | Advanced 💎 |
| 221 | Terminator   | Advanced 💎 |
| 222 | Bixxin       | Advanced 💎 |
| 223 | SawAGenie    | Premium  💵 |
| 224 | RuthLynx     | Premium  💵 |
| 225 | TheAme       | Premium  💵 |
| 226 | LittleAlpha  | Premium  💵 |
| 227 | Rezzerez     | Premium  💵 |
| 228 | 200IQPlays   | Premium  💵 |
| 229 | Progressive  | Advanced 💎 |
| 230 | Naxillous    | Premium  💵 |
| 231 | Yuugeeyoh    | Premium  💵 |
| 232 | VeryCoronic  | Premium  💵 |
| 233 | DonaldTrump  | Advanced 💎 |
| 234 | AlphaMan     | Premium  💵 |
| 235 | ResumeJ      | Advanced 💎 |
| 236 | Beefolution  | Premium  💵 |
| 237 | Modeloff     | Premium  💵 |
| 238 | Beary3       | Premium  💵 |
| 239 | Scarlet5     | Advanced 💎 |
| 240 | MarkNecker   | Premium  💵 |
| 241 | Kuzu3.14     | Premium  💵 |
| 242 | Dipotassium  | Advanced 💎 |
| 243 | Nanalala     | Premium  💵 |
| 244 | CoolSoul     | Premium  💵 |
| 245 | HaloSensei   | Premium  💵 |
| 246 | ProfessorPro | Premium  💵 |
| 247 | Raineko      | Premium  💵 |
| 248 | CheekyGod    | Advanced 💎 |
| 249 | Mr.Cable     | Advanced 💎 |
| 250 | Chlorophyll  | Premium  💵 |
| 251 | BananaShark  | Premium  💵 |
| 252 | Chapati      | Advanced 💎 |
| 253 | Takoyaki     | Premium  💵 |
| 254 | Celestial    | Premium  💵 |
| 255 | NekoRamen    | Premium  💵 |
| 256 | iDoggo       | Premium  💵 |
| 257 | Dissing      | Premium  💵 |
| 258 | Marshal      | Premium  💵 |
| 259 | Sgt.PewPew   | Premium  💵 |
| 260 | Tracing      | Premium  💵 |
| 261 | Armani       | Premium  💵 |
| 262 | Barley       | Premium  💵 |
| 263 | Xdbuild      | Premium  💵 |
| 264 | FateCrow     | Premium  💵 |
| 265 | Bengax       | Premium  💵 |
| 266 | LucidHair    | Premium  💵 |
| 267 | E.vil@1010   | Premium  💵 |
| 268 | NeoPredator  | Premium  💵 |
