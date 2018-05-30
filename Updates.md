**16 March 2018**

* Added multipage support for pokelogs.
* Fixed timing error in multipage pokelog.
* Fixed Nidoran's Male/Female symbol bug.
* Added PokeExec command.
* Minor code restructuring.
* Added Echo command.
* Added id command.
* Fixed DMChannel Bug and Echo command.
* Added search to id command.
* Restructured Typing.
* Added trade by id.
* Fixed Args-Mention Conflict.
* Added Duplicates command.

**22 ‎March ‎2018**

* Added Legendary Command.
* Added Stealth Mode if you're in PokeCord Official Server.
* MultiTrade using args.
* `{prefix}poke_exec command args` is now `{prefix}command args`.
  So you can easily use pokecord commands.
* Major Code Refactoring.
* Added Pagination to embeds.
* Multiple bug fixes.
* Merged safe_list into priority.
* Added Mass Release command.

**23 March 2018**

* Added Total command.
* Altered pokelog to wait for embed edits.
* Altered on_ready display messages.
* Added priority_only mode.
* Added toggler for autocatcher.

**26 March 2018**

* Fixed autocatcher issues.
* User mentions can now be passed to poke_exec.
* Page Number as args for pokelog.
* Rewrote Trade command. Additionally, you can now provide pokemon names as args along with known ids.

**27 March 2018**

* Added continue mode for pokelog.
  >Use `{prefix}pokelog {page_number} continue` to resume the pokelog from that page instead of from the start.
* Fixed DMChannel bug which pops up when the user is DMed.
* Slightly refactored code for better efficiency.

**15 April 2018**

* Expanded Legendaries list
* Toggler for Autocatcher
* Added Blacklist/Whitelist mode
* Fixed autocatcher's name bug
* Logs now include levels
* Better trash control
* Fixed error for id command when the pokemon is not found
* Case insensitive toggler commands

**29 April 2018**

* Trade by Fav option added.
  >You can now simply trade all the pokemon in your fav list to the other account.
* Fixed spelling for Yveltal.
* Other Minor changes.

**10 May 2018**
* No need to use `pokelog`, after catching every new pokemon, anymore. The selfbot will take care of that automatically.
* Fixed bugs in display of Whitelists and Blacklists.
* Other minor improvements.

**14 May 2018**
* [Breaking] Fixed the autocatcher. It is now a few seconds slower than before but it works. This was a result of PokeCord's update.
* Fixed a small bug in autologging.

**17 May 2018**
* [Breaking] Added more delays to take care of PokeCord's ratelimits. (Realtime testing required.)
* Added `avoid` config to skip all the unrequired pokemon.

**26 May 2018**
* Fixed the `Trade` bug where the first pokemon gets added before the trade begins.
* Fixed the freezing `clean_trash` command.
* Added a gift command to transfer cash quickly.
  > `P^gift @user2 10000` is the syntax.
* Fixed indentation in autocatcher to fix the `pref referenced before local assignment` bug.  

**29 May 2018**
* [Major] Added blacklist/whitelist modes for guilds.
* [Major] Added config key and toggler function for Autolog.
* [Major] Pokelog has been rewritten and is now fully automatic.
* Commands are now case insensitive.
* Fixed spellings on Mesprit and Thundurus in the legendaries list.
* Fixed pokemon name conflicts in priority_only mode.
* [Major] Deprecated Stealth Mode in favor of Blacklist Guilds.

**31 May 2018**
* Isolated version number as a class instance.
* Added Version Control message.
* Fixed indentation mismatch in toggler commands.