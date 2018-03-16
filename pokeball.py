import asyncio
import discord
import json
import re
import random
import json
import inspect

class PokeBall(discord.Client):
    def __init__(self, config_path: str, guild_path: str, pokelist_path: str, *args, **kwargs):
        self.config_path = config_path
        self.guild_path = guild_path
        self.pokelist_path = pokelist_path
        self.p = re.compile('([A-Z])\w+')
        with open(self.guild_path) as f:
            self.prefix_dict = json.load(f)
        with open(self.config_path) as f:
            self.configs = json.load(f)
        self.prefix = self.configs['command_prefix']
        super().__init__()
        with open(self.pokelist_path) as f:
            self.pokelist = f.read().splitlines()

    def run(self):
        super().run(self.configs['token'], bot=False)

    def new_guild(self, message, pref):
        if message.guild.id not in self.prefix_dict.keys(): 
            self.prefix_dict[message.guild.id] = pref.split('catch')[0]
            with open(self.guild_path, 'w') as f:
                f.write(json.dumps(self.prefix_dict))
    
    async def on_message(self, message):
        def pokecord_reply(msg):
            return msg.author.id == 365975655608745985
        
        prefix_checks = [
            message.content.startswith(self.prefix),
            message.author.id == self.user.id
        ]    
                
        if message.author.id == 365975655608745985 and message.embeds:
            emb = message.embeds[0]
            if emb.title.startswith('A wild'):
                name = self.p.search(emb.image.url.split('/')[-1]).group()
                name = name.split('_')[0]
                proc = random.randint(1, 100)
                if name in self.configs['priority'] or proc <= self.configs['catch_rate']:
                    async with message.channel.typing():
                        if name in self.configs['priority']:
                            self.configs['priority'].pop(name)
                        pref = emb.description.split()[5]
                        self.new_guild(message, pref)        
                        if self.configs['delay_on_priority'] or name not in self.configs["priority"]:
                            await asyncio.sleep(self.configs['delay'])
                    await message.channel.send(f"{pref} {name}")
                reply = await self.wait_for('message', check=pokecord_reply)
                if self.user.mentioned_in(reply):
                    print(f'Caught **{name}** in *{message.guild.name}* in #{message.channel.name}')

        if all(prefix_checks):
            def arg_check(arg):
                if not message.raw_mentions:
                    return True
                checks = [
                    message.raw_mentions,
                    arg != f"<@{message.raw_mentions.pop(0)}>"
                ]
                return all(checks)

            detokenized = message.content.split(' ')
            cmd = detokenized[0]
            args = None
            if len(detokenized) > 1:
                args = [
                    arg for arg in detokenized[1:] if arg_check(arg)
                ]
            cmd = cmd.replace(self.prefix,'cmd_')
            method = self.__getattribute__(cmd)
            kwargs = {'message':message}
            if message.mentions:
                kwargs['mentions'] = message.mentions
            if args:
                kwargs['args'] = args
            required = inspect.signature(method)
            required = set(required.parameters.copy())
            if  required == set(kwargs):
                await method(**kwargs)    

    async def cmd_pokelog(self, message):
        def pokecord_reply(msg):
            if msg.embeds:
                checks = [
                    msg.author.id == 365975655608745985,
                    msg.embeds[0].title.startswith('Your pokémon:')
                ]
                return  all(checks)
            else:
                return False 
        def log_formatter(pokemon):
            params = pokemon.split(' | ')
            name = params[0].replace('**','')
            number = params[2].replace('Number: ','')
            return f"{name} -> {number}"
        
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref:
            await message.channel.send(f"{pref}pokemon")
            reply = await self.wait_for('message', check=pokecord_reply)
            pokemons = reply.embeds[0].description.split('\n')
            pokelist = [log_formatter(pokemon) for pokemon in pokemons]
            await asyncio.sleep(random.randint(3,5))
            while True:
                await message.channel.send(f"{pref}n")
                try:
                    reply = await self.wait_for('message', check=pokecord_reply, timeout=10.0)
                    pokemons = reply.embeds[0].description.split('\n')
                    pokelist += [log_formatter(pokemon) for pokemon in pokemons]
                    await asyncio.sleep(random.randint(5,7))
                except Exception as e:
                    print(str(e))
                    break
            self.pokelist = pokelist        
            with open(self.pokelist_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(pokelist))
            print('Logged all the pokemon successfully.\n')

    async def cmd_trade(self, message, mentions, args=[]):
        def safe_filter(pokemon):
            checks = [
                pokemon.split(' -> ')[1]!='1',
                pokemon.split(' -> ')[0] not in self.configs['safe_list']
            ]
            return all(checks) 

        def user_reply(msg):
            checks = [
                msg.author.id == user.id,
                word in msg.content
            ]
            return all(checks)

        def pokecord_reply(msg):
            return msg.author.id == 365975655608745985

        user = mentions[0]
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref:
            if args:
                numbers = args[0:1]
            else:
                with open(self.pokelist_path,'r', encoding='utf-8') as f:
                    pokelist = f.read().splitlines()
                numbers = [pokemon.split(' -> ')[1] for pokemon in pokelist if safe_filter(pokemon)]
            for number in numbers:    
                await message.channel.send(f"{pref}trade {user.mention}")    
                word = f"{pref}accept"
                reply = await self.wait_for('message', check=user_reply)
                confirmation = await self.wait_for('message', check=pokecord_reply)
                await asyncio.sleep(0.5)
                await message.channel.send(f"{pref}p")
                confirmation = await self.wait_for('message', check=pokecord_reply)
                await asyncio.sleep(0.5)
                await message.channel.send(f"{number}")
                word = f"{pref}c"
                reply = await self.wait_for('message', check=user_reply)
                word = '0'
                reply = await self.wait_for('message', check=user_reply)
                confirmation = await self.wait_for('message', check=pokecord_reply)
                await asyncio.sleep(0.5)
                await message.channel.send(f"{pref}accept")
                await asyncio.sleep(5)
                
            print('Successfully traded away all pokemon.')    
            await self.cmd_pokelog(message)    

    async def cmd_poke_exec(self, message, args=[]):
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref and args:
            command = args.pop(0)
            pokeargs = ' '.join(args)
            pokecmd = f"{pref}{command} {pokeargs}"
            await message.channel.send(pokecmd)        

    async def cmd_echo(self, message, args=[]):
        await message.channel.send(' '.join(args))

    async def cmd_id(self, message, args=[]):
        def assert_name(pokemon):
            return pokemon.split(' -> ')[0].lower() == pokename.lower()
        def search_name(pokemon):
            return pokename.lower() in pokemon.split(' -> ')[0].lower()
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref and args:
            if len(args) > 1 and args[0] == 'search':
                pokename = args[1]
                results = [
                    pokemon.split(' -> ') for pokemon in self.pokelist if search_name(pokemon)
                ]
                embed = discord.Embed(title="Search Results", description="\u200B", color=15728640)
                for name, id_val in results:
                    embed.add_field(name=name, value=id_val, inline=False)
            else:
                pokename = args[0]
                ids = [
                    pokemon.split(' -> ')[1] for pokemon in self.pokelist if assert_name(pokemon)
                ]
                embed = discord.Embed(title=pokename, description="\u200B", color=15728640)    
                for id_val in ids:
                    embed.add_field(name=id_val, value="\u200B", inline=False) 
            await message.channel.send(content=None, embed=embed)

    async def cmd_duplicates(self, message):
        def get_id(pokename):
            def assert_name(pokemon):
                return pokemon.split(' -> ')[0].lower() == pokename.lower()
            ids = [
                    pokemon.split(' -> ')[1] for pokemon in self.pokelist if assert_name(pokemon)
                ]
            return '\n'.join(ids)    
        pokemons = [pokemon.split(' -> ')[0] for pokemon in self.pokelist]
        dups = {dup for dup in pokemons if pokemons.count(dup) > 1}
        embed = discord.Embed(title="Here's the list of duplicate pokemon", description="\u200B", color=15728640)
        for dup in dups:
            embed.add_field(name=dup, value=get_id(dup), inline=False)
        await message.channel.send(content=None, embed=embed)

    async def on_ready(self):
        print("Logged in.\n---PokeBall SelfBot v1.0----\n"
              f"Command Prefix: {self.configs['command_prefix']}\n"  
              f"Priority: {', '.join(self.configs['priority'])}\n"
              f"Untradable Pokemon: {', '.join(self.configs['safe_list'])}\n"
              f"Catch Rate: {self.configs['catch_rate']}%\n"
              f"Catch Delay: {self.configs['delay']} seconds\n"
              f"Delay On Priority: {'On' if self.configs['delay_on_priority'] == True else 'Off'}")

