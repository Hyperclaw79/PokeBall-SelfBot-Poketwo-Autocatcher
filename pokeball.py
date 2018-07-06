import asyncio
import discord
import json
import re
import random
import json
import inspect
from paginator import Paginator
from math import ceil
import subprocess
import aiohttp
import hashlib

class PokeBall(discord.Client):
    def __init__(self, config_path: str, guild_path: str, pokelist_path: str, pokenames_path: str, *args, **kwargs):
        self.version = "v3.3.2"
        self.config_path = config_path
        self.guild_path = guild_path
        self.pokelist_path = pokelist_path
        with open(self.guild_path) as f:
            self.prefix_dict = json.load(f)
        with open(self.config_path) as f:
            self.configs = json.load(f)
        self.prefix = self.configs['command_prefix']
        super().__init__()
        with open(self.pokelist_path, 'r', encoding='utf-8') as f:
            self.pokelist = f.read().splitlines()
        self.legendaries = [
            'Arceus', 'Articuno', 'Azelf', 'Celebi', 'Cobalion', 'Cosmoem', 'Cosmog', 'Cresselia',
            'Darkrai', 'Deoxys', 'Dialga', 'Diancie', 'Entei', 'Genesect', 'Giratina', 'Groudon',
            'Heatran', 'Ho-Oh', 'Hoopa', 'Jirachi', 'Keldeo', 'Kyogre', 'Kyurem', 'Landorus',
            'Latias', 'Latios', 'Lugia', 'Lunala', 'Magearna', 'Manaphy', 'Marshadow', 'Meloetta',
            'Mesprit', 'Mew', 'Mewtwo', 'Moltres', 'Necrozma', 'Palkia', 'Phione', 'Raikou',
            'Rayquaza', 'Regice', 'Regigigas', 'Regirock', 'Registeel', 'Reshiram', 'Shaymin', 'Silvally',
            'Solgaleo', 'Suicune', 'Tapu Bulu', 'Tapu Fini', 'Tapu Koko', 'Tapu Lele', 'Terrakion', 'Thundurus',
            'Tornadus', 'Type: Null', 'Uxie', 'Victini', 'Virizion', 'Volcanion', 'Xerneas', 'Yveltal',
            'Zapdos', 'Zekrom', 'Zeraora', 'Zygarde'
        ]
        pokemons = [pokemon.split(' -> ')[0] for pokemon in self.pokelist]
        self.trash = list({dup for dup in pokemons if pokemons.count(dup) > int(self.configs["max_duplicates"]) - 1})
        self.priority_only = self.configs["priority_only"]
        self.auto_catcher = self.configs["autocatcher"]
        self.mode = "blacklist"
        self.guild_mode = "blacklist"
        self.autolog = self.configs["autolog"]
        self.ready = False
        with open(pokenames_path, 'r', encoding='utf-8') as f:
            self.pokenames = json.load(f)

    def run(self):
        super().run(self.configs['token'], bot=False)

    def refresh_trash(self):
        pokemons = [pokemon.split(' -> ')[0] for pokemon in self.pokelist]
        self.trash = list({dup for dup in pokemons if pokemons.count(dup) > int(self.configs["max_duplicates"]) - 1})

    def junky_trash(self):
        def safe_filter(pokemon):
            names = [pokemon.split(' -> ')[0] for pokemon in self.pokelist]
            checks = [
                pokemon.split(' -> ')[1]!='1',
                pokemon.split(' -> ')[0] not in (
                    self.configs['priority'] +
                    self.legendaries
                ),
                names.count(pokemon.split(' -> ')[0]) > int(self.configs["max_duplicates"]),
                len(pokemon.split(' -> ')) <= 3
            ]
            return all(checks)
        def guard(pokes):
            limit = int(self.configs['max_duplicates'])
            pokelist = pokes[:]
            for poke in pokelist:
                pokename = poke[0]
                mons = [mon[0] for mon in pokelist]
                while mons.count(pokename) > limit:
                    pokelist.pop(mons.index(pokename))
                    mons = [mon[0] for mon in pokelist]
            return pokelist
        results = [pokemon.split(' -> ') for pokemon in self.pokelist if safe_filter(pokemon)]
        junk = sorted(results, key=(lambda x: (x[0], int(x[2]))))
        safe = guard(junk)
        pokes = [poke for poke in junk if poke not in safe]
        return pokes

    def is_legend(self, pokemon):
        return pokemon in self.legendaries

    def get_id(self, pokename, search=False):
        def assert_name(pokemon):
            return pokemon.split(' -> ')[0].lower() == pokename.lower()
        def search_name(pokemon):
            return pokename.lower() in pokemon.split(' -> ')[0].lower()
        results = []
        if search:
            results = [
                pokemon.split(' -> ') for pokemon in self.pokelist if search_name(pokemon)
            ]
        else:
            results = [
                pokemon.split(' -> ')[1] for pokemon in self.pokelist if assert_name(pokemon)
            ]
        return results or "\u200B"    
    
    def new_guild(self, message, pref):
        if message.guild.id not in self.prefix_dict.keys(): 
            self.prefix_dict[message.guild.id] = pref.split('catch')[0]
            with open(self.guild_path, 'w') as f:
                f.write(json.dumps(self.prefix_dict))
    
    async def match(self, url):
        async with await self.sess.get(url) as resp:
            dat = await resp.content.read()
        m = hashlib.md5(dat).hexdigest()
        return self.pokenames[m]
        
    async def on_message(self, message):
        def pokecord_reply(msg):
            return msg.author.id == 365975655608745985
        
        if not self.ready:
            return

        if "guild" not in dir(message): #Skip DMs to avoid AttributeError (alt)
            return
        
        if message.guild is None: #Skip DMs to avoid AttributeError
            return
        else:
            blacklist_checks = [
                self.mode == "blacklist",
                message.channel.id in self.configs["blacklists"]    
            ]
            whitelist_checks = [
                self.mode == "whitelist",
                message.channel.id not in self.configs["whitelists"]    
            ]
            blackguild_checks = [
                self.guild_mode == "blacklist",
                message.guild.id in self.configs["blacklist_guilds"]    
            ]
            whiteguild_checks = [
                self.guild_mode == "whitelist",
                message.guild.id not in self.configs["whitelist_guilds"]    
            ]
            return_checks = [
                all(blacklist_checks),
                all(whitelist_checks),
                all(blackguild_checks),
                all(whiteguild_checks)
            ]
            if any(return_checks):
                return
        
        #AutoCatcher
        pokeball_checks = [
            message.author.id == 365975655608745985,
            message.embeds,
            self.auto_catcher
        ]
        if all(pokeball_checks):
            def log_formatter(pokemon):
                params = pokemon.split(' | ')
                name = params[0].replace('**', '')
                level = params[1].replace('Level: ', '')
                number = params[2].replace('Number: ', '')
                return f"{name} -> {number} -> {level}"
            
            emb = message.embeds[0]
            try:
                embcheck = emb.title.startswith('A wild')
            except AttributeError:
                return    
            if embcheck:
                name = await self.match(emb.image.url.split('?')[0])
                name = name.title()
                if not name:
                    print(f"Unable to find a name for {name1}.")
                    return
                duplicate_checks = [
                    name in self.trash,
                    name not in (
                        self.configs['priority'] + 
                        self.legendaries
                    ),
                    self.configs["restrict_duplicates"]
                ]
                proc = random.randint(1, 100)
                sub_checks = [
                    name in self.configs['priority'],
                    name in self.legendaries
                ]
                def catch_checks(name):
                    if self.priority_only:
                        return any(sub_checks)
                    elif not any(sub_checks):
                        catch_subchecks = [
                            proc <= self.configs['catch_rate'],
                            name not in self.configs['avoid']
                        ]
                        return all(catch_subchecks)
                    else:
                        return True
                catcher = catch_checks(name)
                if catcher:
                    async with message.channel.typing():
                        pref = emb.description.split()[5]
                        self.new_guild(message, pref)
                        delay_checks = [
                            self.configs['delay_on_priority'],
                            name in (
                                self.configs["priority"] +
                                self.legendaries
                            )
                        ]        
                        if all(delay_checks) or not any(sub_checks):
                            await asyncio.sleep(self.configs['delay'])
                        if all(duplicate_checks):
                            print(f"Skipping the duplicate: {name}")
                            return    
                    await message.channel.send(f"{pref} {name}")
                    reply = await self.wait_for('message', check=pokecord_reply)
                    if self.user.mentioned_in(reply):
                        print(f'Caught **{name}** in *{message.guild.name}* in #{message.channel.name}')
                        if self.autolog:
                            await message.channel.send(f"{pref.replace('catch','pokemon')} --name {name}")
                            reply = await self.wait_for('message', check=pokecord_reply)
                            if reply.embeds and reply.channel.id == message.channel.id:
                                raw_list = reply.embeds[0].description.splitlines()
                                refined_list = [
                                    log_formatter(pokeline) for pokeline in raw_list if log_formatter(pokeline) not in self.pokelist
                                ]
                                self.pokelist.append(refined_list[0])
                                with open(self.pokelist_path, 'w', encoding='utf-8') as f:
                                    f.write('\n'.join(self.pokelist))

        #SelfBot Commands
        prefix_checks = [
            message.content.startswith(self.prefix),
            message.author.id == self.user.id
        ]
        if all(prefix_checks):
            def arg_check(arg):
                str_mentions = [str(mention) for mention in raw_mentions]
                if not raw_mentions:
                    return True
                checks = [
                    raw_mentions,
                    arg != '',
                    arg.replace('<@','').replace('>','') not in str_mentions 
                ]
                return all(checks)

            raw_mentions = message.raw_mentions or None
            detokenized = message.content.split(' ')
            cmd = detokenized[0]
            args = []
            if len(detokenized) > 1:
                if raw_mentions:
                    args = [
                        arg for arg in detokenized[1:] if arg_check(arg)
                    ]
                else:
                    args = [arg for arg in detokenized[1:] if arg != '']
            cmd = cmd.replace(self.prefix,'cmd_').lower()
            try:
                method = self.__getattribute__(cmd)
            except AttributeError: # Not a selfbot command, so execute it as a PokeCord command.
                cmd = cmd.replace('cmd_', '')
                args.insert(0, cmd)
                method = self.cmd_poke_exec
            kwargs = {
                'message':message,
                'args': args,
                'mentions': []
            }
            if message.mentions:
                kwargs['mentions'] = message.mentions
            required = inspect.signature(method)
            required = set(required.parameters.copy())
            for key in list(kwargs):
                if key not in required:
                    kwargs.pop(key, None)
            if required == set(kwargs):
                await method(**kwargs)


    async def cmd_pokelog(self, message, args=[]):
        def pokecord_reply(msg):
            if msg.embeds:
                checks = [
                    msg.author.id == 365975655608745985,
                    msg.channel.id == message.channel.id,
                    msg.embeds[0].title.startswith('Your pokémon:')
                ]
                return  all(checks)
            else:
                return False 
        def pokecord_edit(before, msg):
            if msg.embeds:
                checks = [
                    msg.author.id == 365975655608745985,
                    msg.channel.id == message.channel.id,
                    msg.embeds[0].title.startswith('Your pokémon:')
                ]
                return  all(checks)
            else:
                return False
        def log_formatter(pokemon):
            params = pokemon.split(' | ')
            name = params[0].replace('**', '')
            level = params[1].replace('Level: ', '')
            number = params[2].replace('Number: ', '')
            if len(params) == 4:
                nick = params[3].replace('Nickname: ','')
                return f"{name} -> {number} -> {level} -> {nick}"    
            return f"{name} -> {number} -> {level}"
        
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref:
            page = 1
            pokelist = []
            if args:
                page = int(args[0])
                if len(args) > 1 and args[1] == 'continue':
                    with open(self.pokelist_path, 'r', encoding='utf-8') as f:
                        pokelist = f.read().splitlines()
                await message.channel.send(f"{pref}pokemon {args[0]}")
            else:
                await message.channel.send(f"{pref}pokemon")
            reply = await self.wait_for('message', check=pokecord_reply)
            pokemons = reply.embeds[0].description.split('\n')
            pokelist += [log_formatter(pokemon) for pokemon in pokemons]
            await asyncio.sleep(random.randint(2,3))
            while True:
                delme = await message.channel.send(f"{pref}n")
                try:
                    before, reply = await self.wait_for('message_edit', check=pokecord_edit, timeout=10.0)
                except:
                    await message.channel.send(f"{pref}pokemon {page + 1}")
                    try:
                        reply = await self.wait_for('message', check=pokecord_reply, timeout=10.0)
                    except:
                        await message.channel.send(f"Logged up to page {page}.")
                pokemons = reply.embeds[0].description.split('\n')
                try:
                    await delme.delete()
                except:
                    pass
                page += 1
                pokelist += [log_formatter(pokemon) for pokemon in pokemons]
                with open(self.pokelist_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(pokelist))
                self.pokelist = pokelist
                if len(pokemons) < 20:
                    break
                else:
                    await asyncio.sleep(random.randint(5,7))
            self.pokelist = pokelist
            self.refresh_trash()    
            print('Logged all the pokemon successfully.\n')
            await self.cmd_total(message=message)
        else:
            print('No prefix found for this guild.')

    async def cmd_trade(self, message, mentions, args=[]):
        def safe_filter(pokemon):
            checks = [
                pokemon.split(' -> ')[1]!='1',
                pokemon.split(' -> ')[0] not in self.configs['priority']
            ]
            return all(checks)

        def user_reply(msg):
            checks = [
                msg.author.id == user.id,
                word in msg.content
            ]
            return all(checks)

        def pokecord_reply(msg):
            return msg.author.id == 365975655608745985 and msg.channel.id == message.channel.id

        def pokecord_embed(msg):
            checks = [
                msg.author.id == 365975655608745985,
                msg.channel.id == message.channel.id,
                msg.embeds
            ]
            return all(checks)    

        def id_extracter(pokemon):
            params = pokemon.split(' | ')
            name = params[0].replace('**', '')
            level = params[1].replace('Level: ', '')
            number = params[2].replace('Number: ', '')
            return int(number)

        user = mentions[0]
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref:
            with open(self.pokelist_path,'r', encoding='utf-8') as f:
                pokelist = f.read().splitlines()
            if args:
                if "fav" in args:
                    await message.channel.send(f"{pref}fav")
                    try:
                        reply = await self.wait_for('message', check=pokecord_reply, timeout=2.0)
                    except:
                        await message.channel.send(f"{pref}ping")
                        await message.channel.send(f"{pref}fav")
                        reply = await self.wait_for('message', check=pokecord_reply)
                    if reply.embeds and reply.embeds[0].title == "Your pokémon:":
                        pokemons = reply.embeds[0].description.split('\n')
                        numbers = [id_extracter(pokeline) for pokeline in pokemons]
                else:
                    numlist = []
                    for arg in args:
                        if all(char.isalpha() for char in arg):
                            numlist += self.get_id(args[0].title())
                        else:
                            numlist.append(arg)
                    numbers = numlist            
            else:
                numbers = [pokemon.split(' -> ')[1] for pokemon in self.pokelist if safe_filter(pokemon)]
                numbers = sorted(numbers,reverse=True)
            numbatches = [numbers[i:i+25] for i in range(0, len(numbers), 25)]
            for numbers in numbatches:
                await message.channel.send(f"{pref}trade {user.mention}")    
                word = f"{pref}accept"
                reply = await self.wait_for('message', check=user_reply)
                confirmation = await self.wait_for('message', check=pokecord_embed)
                for number in numbers:
                    await message.channel.send(f"{pref}p add {number}")
                    await asyncio.sleep(2.0)
                await message.channel.send(f"{pref}confirm")
                confirmation = await self.wait_for('message', check=pokecord_reply)
                if confirmation.content == "Trade confirmed.":
                    await asyncio.sleep(3.0)
                else:
                    continue
            print('Successfully traded away all pokemon.')    
            await self.cmd_pokelog(message)

    async def cmd_poke_exec(self, message, args=[], mentions=None):
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref and args:
            command = args.pop(0)
            pokeargs = ' '.join(args)
            pokementions = ' '+' '.join([mention.mention for mention in mentions]) or ''
            pokecmd = f"{pref}{command}{pokementions}{pokeargs}"
            await message.channel.send(pokecmd)        

    async def cmd_echo(self, message, args=[], mentions=None):
        if args:
            await message.channel.send(f"{' '.join(args)} {' '.join([mention.mention for mention in mentions])}")

    async def cmd_id(self, message, args=[]):
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref and args:
            if len(args) > 1 and args[0] == 'search':
                pokename = args[1]
                results = self.get_id(pokename, True)
                embeds = []
                for i in range(0, len(results), 10):
                    embed = discord.Embed(title="Search Results", description="\u200B", color=15728640)
                    if results == "\u200B":
                        continue
                    else:
                        for result in results[i:i+10]:
                            embed.add_field(name=result[0], value=f"**ID**: {result[1]}\n**LEVEL**: {result[2]}", inline=False)
                        embeds.append(embed)
                try:
                    base = await message.channel.send(content=None, embed=embeds[0])
                    pager = Paginator(message, base, embeds, self)
                    await pager.run()
                except:
                    await message.channel.send(":cold_sweat: | No results found.")
            else:
                pokename = args[0]
                results = self.get_id(pokename, True)
                embed = discord.Embed(title=pokename.title(), description="\u200B", color=15728640)    
                if results  == "\u200B":
                    await message.channel.send(":cold_sweat: | No results found.")
                    return
                else:        
                    for result in results:
                        embed.add_field(name="**ID**", value=f"{result[1]}", inline=False)
                        embed.add_field(name="**LEVEL**", value=f"{result[2]}", inline=False)
                        embed.add_field(name="-----", value="\u200B", inline=False) 
                    await message.channel.send(content=None, embed=embed)

    async def cmd_duplicates(self, message, args=[]):
        pokemons = [pokemon.split(' -> ')[0] for pokemon in self.pokelist]
        limit = 2
        if args:
            limit = int(args[0])
        dups = {dup for dup in pokemons if pokemons.count(dup) >= limit}
        if len(dups) == 0:
            await message.channel.send("There is no pokemon with so many duplicates. Try a smaller number.")
            return
        dups = list(dups)
        dups = sorted(dups)
        embeds = []
        for i in range(0, len(dups), 10):
            embed = discord.Embed(title="Duplicates", description="\u200B", color=15728640)
            for dup in dups[i:i+10]:
                results = self.get_id(dup, True)
                data = [f"**ID**: {result[1]}\t**LEVEL**: {result[2]}" for result in results]
                data.append('-------------------------------------------------')    
                embed.add_field(name=f"**{dup}**", value='\n'.join(data), inline=False)
            embed.set_footer(text=f"{(i//10)+1}/{ceil(len(dups)/10)}")
            embeds.append(embed)
        base = await message.channel.send(content=None, embed=embeds[0])
        pager = Paginator(message, base, embeds, self)
        await pager.run()

    async def cmd_legendary(self, message):
        embeds = []
        for i in range(0, len(self.legendaries), 5):
            embed = discord.Embed(title="Legendaries", description="\u200B", color=15728640)
            for legend in self.legendaries[i:i+5]:
                embed.add_field(name=legend, value='\n'.join(self.get_id(legend)), inline=False)
            embeds.append(embed)
        base = await message.channel.send(content=None, embed=embeds[0])
        pager = Paginator(message, base, embeds, self)
        await pager.run()

    async def cmd_total(self, message):
        await message.channel.send(f"Total number of pokemon:\n{len(self.pokelist)}")

    async def cmd_mass_release(self, message, args=[]):
        def pokecord_reply(msg):
            return msg.author.id == 365975655608745985 and msg.channel.id == message.channel.id

        def pokecord_embed(msg):
            checks = [
                msg.author.id == 365975655608745985,
                msg.channel.id == message.channel.id,
                msg.embeds
            ]
            return all(checks)    

        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref and args:
            if "dupes" in (arg.lower() for arg in args):
                junk = self.junky_trash()
                numbers = [mon[1] for mon in junk]
            else:
                numbers = args
            numlist = list(set(sorted(numbers, key=lambda x: int(x), reverse=True)))
            for numbers in numlist:
                num_str = ' '.join(numbers)
                await message.channel.send(f"{pref}release {num_str}")
                desc = await self.wait_for('message', check=pokecord_embed)
                desc = desc.embeds[0]
                criticals = (
                    self.configs["priority"] + 
                    self.legendaries
                )
                desc = desc.to_dict()["fields"][0]["value"]
                for pokemon in criticals:
                    if pokemon in desc:
                        print(f"WOAH! Almost deleted {pokemon}!")
                        return
                await asyncio.sleep(1.0)
                await message.channel.send(f"{pref}confirm")
                await self.wait_for('message', check=pokecord_reply)
                await self.cmd_pokelog(message)
            print("Successfully Released all the specified pokemons.")

    async def cmd_priority_only(self, message, args=[]):
        if args:
            if args[0].lower() == 'off':
                self.priority_only = False
                print('Catching all pokemons.\n')
            elif args[0].lower() == 'on':
                self.priority_only = True
                print('Catching only priority and legendary pokemon.\n')
            else:
                print(args)

    async def cmd_autocatcher(self, message, args=[]):
        if args:
            if args[0].lower() == 'off':
                self.auto_catcher = False
                print('Switching to Commands Only mode.\n')
            elif args[0].lower() == 'on':
                self.auto_catcher = True
                print('Activated autocatcher.\n')
            else:
                print(args)

    async def cmd_autolog(self, message, args=[]):
        if args:
            if args[0].lower() == 'off':
                self.autolog = False
                print('Disabled Autologger.\n')
            elif args[0].lower() == 'on':
                self.autolog = True
                print('Enabled Autologger.\n')
            else:
                print(args)            

    async def cmd_toggle_mode(self, message, args=[]):
        if args and args[0].lower() in ["blacklist", "whitelist"]:
            self.mode = args[0].lower()
            print(f"Switched to {args[0].title()} mode.")

    async def cmd_toggle_guildmode(self, message, args=[]):
        if args and args[0].lower() in ["blacklist", "whitelist"]:
            self.guild_mode = args[0].lower()
            print(f"Switched to {args[0].title()}ed guilds mode.")    

    async def cmd_gift(self, message, mentions, args=[]):
        def user_reply(msg):
            checks = [
                msg.author.id == user.id,
                word in msg.content
            ]
            return all(checks)

        def pokecord_reply(msg):
            return msg.author.id == 365975655608745985 and msg.channel.id == message.channel.id

        def pokecord_embed(msg):
            checks = [
                msg.author.id == 365975655608745985,
                msg.channel.id == message.channel.id,
                msg.embeds
            ]
            return all(checks)

        user = mentions[0]
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref and args:
            money = args[0]
            await message.channel.send(f"{pref}trade {user.mention}")    
            word = f"{pref}accept"
            reply = await self.wait_for('message', check=user_reply)
            confirmation = await self.wait_for('message', check=pokecord_embed)
            await message.channel.send(f"{pref}c add {money}")
            await asyncio.sleep(2.0)
            await message.channel.send(f"{pref}confirm")
            confirmation = await self.wait_for('message', check=pokecord_reply)
            if confirmation.content == "Trade confirmed.":
                print(f'Successfully gifted {money}c to {user}.')

    
    async def on_ready(self):
        async def updater():
            def bordered(text): # Kudos to xKynn for this.
                lines = text.splitlines()
                width = max(len(s) for s in lines) + 2
                res = ['┌' + '─' * width + '┐']
                for s in lines:
                    res.append('│ ' + (s + ' ' * width)[:width - 1] + '│')
                res.append('└' + '─' * width + '┘')
                return '\n'.join(res)

            async def file_modifier(filename):
                async with aiohttp.ClientSession(headers=api_headers, loop=self.loop) as sess:
                    async with sess.get(f"{api_base_url}/{filename}") as resp:
                        if ".json" in filename:
                            code = await resp.read()
                            code = code.decode()
                        else:    
                            code = await resp.text()
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(code)

            def config_patcher(base_configs):
                with open('config.json', 'r', encoding='utf-8') as f:
                    configs = json.load(f)
                if list(configs.keys()) != list(base_configs.keys()):
                    keys = [key for key in list(base_configs.keys()) if key not in list(configs.keys())]
                    for key in keys:
                        configs[key] = base_configs[key]
                    with open('config.json', 'w', encoding='utf-8') as f:
                        f.write(json.dumps(configs, indent=3))
                        
            api_base_url = "https://api.github.com/repos/Hyperclaw79/PokeBall-SelfBot/contents"
            if self.configs["update_checker"]:  # For those with error connecting to api.github.com
                api_headers = {
                    "Accept": "application/vnd.github.v3.raw+json",
                    "User-Agent": f"Pokeball-Selfbot_{self.user}"
                }
                async with aiohttp.ClientSession(headers=api_headers, loop=self.loop) as sess:
                    async with sess.get(f"{api_base_url}/_version.json") as resp:
                        ver_data = await resp.read()
                ver_data = json.loads(ver_data)    
                vnum = int(ver_data["version"].split('v')[1].replace('.', ''))
                lnum = int(self.version.split('v')[1].replace('.', ''))
                if vnum > lnum:
                    vtext = 'There is a new version available.\nDownload it for new updates and bug fixes.\n'
                    vtext += f'Your version: {self.version}\nNew Version: {ver_data["version"]}\n'
                    print(bordered(vtext))
                    if self.configs["auto_update"]:
                        print("Automatic updates are enabled.")
                        await asyncio.sleep(2.0)
                        print(f'Automatically updating to {ver_data["version"]}....')
                        mod_files = [filename for filename in ver_data["modified_files"] if filename not in __file__ and filename != 'config.json']
                        for _file in mod_files:
                            await file_modifier(_file)
                            await asyncio.sleep(1.0)
                        if "config.json" in ver_data["modified_files"]:
                            async with aiohttp.ClientSession(headers=api_headers, loop=self.loop) as sess:
                                async with sess.get(f"{api_base_url}/config.json") as resp:
                                    configs_data = await resp.read()
                            base_configs = json.loads(configs_data)
                            config_patcher(base_configs)
                            await asyncio.sleep(1.0)
                        if "pokeball.py" in ver_data["modified_files"]:
                            await file_modifier("pokeball.py")
                        subprocess.run("run.bat") # Change this to run.sh if you're on a mac/linux

        self.sess = aiohttp.ClientSession(loop=self.loop)
        await updater()    
        priorities = self.configs['priority']
        prio_list = '\n'.join([
            ', '.join(priorities[i:i+5]) for i in range(0, len(priorities), 5)
        ])
        try:
            blackies = '\n'.join([
                ', '.join([str(channel) for channel in self.configs['blacklists'][i:i+5]]) for i in range(0, len(self.configs['blacklists']), 5)
            ])
        except:
            blackies = "None"
        try:    
            whities = '\n'.join([
                ', '.join([str(channel) for channel in self.configs['whitelists'][i:i+5]]) for i in range(0, len(self.configs['whitelists']), 5)
            ])
        except:
            whities = "None"
        try:
            blackgs = '\n\t'.join([
                ', '.join([str(channel) for channel in self.configs['blacklist_guilds'][i:i+5]]) for i in range(0, len(self.configs['blacklist_guilds']), 5)
            ])
        except:
            blackgs = "None"
        try:    
            whitigs = '\n\t'.join([
                ', '.join([str(channel) for channel in self.configs['whitelist_guilds'][i:i+5]]) for i in range(0, len(self.configs['whitelist_guilds']), 5)
            ])
        except:
            whitigs = "None"    
        print(
            f"\n---PokeBall SelfBot {self.version}----\n\n"
            f"Bot name: {self.user}\n\n"
            f"Command Prefix: {self.configs['command_prefix']}\n\n"
            f"Priority:\n~~~~~~~~~\n{prio_list}\n\n"
            f"Catch Rate: {self.configs['catch_rate']}%\n\n"
            f"Catch Delay: {self.configs['delay']} seconds\n\n"
            f"Delay On Priority: {'On' if self.configs['delay_on_priority'] == True else 'Off'}\n\n"
            f"Restrict Catching of Duplicates: {'On' if self.configs['delay_on_priority'] == True else 'Off'}\n\n"
            f"Maximum Number of Duplicates: {self.configs['max_duplicates']}\n\n"
            f"Blacklisted Channels:\n~~~~~~~~~~~~~~~~~~~~\n{blackies}\n\n"
            f"Whitelisted Channels:\n~~~~~~~~~~~~~~~~~~~~\n{whities}\n\n"
            f"Blacklisted Guilds:\n~~~~~~~~~~~~~~~~~~~~\n{blackgs}\n\n"
            f"Whitelisted Guilds:\n~~~~~~~~~~~~~~~~~~~~\n{whitigs}\n\n"
            f"Autocatcher: {'On' if self.configs['autocatcher'] == True else 'Off'}\n\n"
            f"Priority Only: {'On' if self.configs['priority_only'] == True else 'Off'}\n\n"
        )
        self.ready = True
                                       
