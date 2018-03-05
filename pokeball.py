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

    def run(self):
        super().run(self.configs['token'], bot=False)

    def new_guild(self, message, pref):
        if message.guild.id not in self.prefix_dict.keys(): 
            self.prefix_dict[message.guild.id] = pref.split('catch')[0]
            with open(self.guild_path, 'w') as f:
                f.write(json.dumps(self.prefix_dict))
    
    async def on_message(self, message):

        if message.author.id == 365975655608745985 and message.embeds:
            async with message.channel.typing():
                emb = message.embeds[0]
                if emb.title.startswith('A wild'):
                    name = self.p.search(emb.image.url.split('/')[-1]).group()
                    proc = random.randint(1, 100)
                    if name in self.configs['priority'] or proc <= self.configs['catch_rate']:
                        if name in self.configs['priority']:
                            self.configs['priority'].pop(name)
                        pref = emb.description.split()[5]
                        self.new_guild(message, pref)        
                        print(f'Caught "{name}" in {message.guild.name} in #{message.channel.name}')
                        if self.configs['delay_on_priority']:
                            await asyncio.sleep(self.configs['delay'])
                        await message.channel.send(f"{pref} {name}")

        if message.content.startswith(self.prefix):
            detokenized = message.content.split(' ')
            cmd = detokenized[0]
            args = None
            if len(detokenized) > 1:
                args = detokenized[1:]
            cmd = cmd.replace(self.prefix,'cmd_')
            method = self.__getattribute__(cmd)
            kwargs = {'message':message}
            if message.raw_mentions:
                kwargs['mentions'] = list(map(message.guild.get_member, message.raw_mentions))
            elif args:
                kwargs['args'] = args
            required = inspect.signature(method)
            required = set(required.parameters.copy())
            if  required == set(kwargs):
                await method(**kwargs)    

    async def cmd_pokelog(self, message):
        def pokecord_reply(msg):
            checks = [
                msg.author.id == 365975655608745985,
                msg.embeds,
                msg.embeds[0].title.startswith('Your pokémon:')
            ]
            return  all(checks) 
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
            with open(self.pokelist_path, 'w') as f:
                f.write('\n'.join(pokelist))
            print('Logged all the pokemon successfully.\n')

    async def cmd_trade(self, message, mentions):
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
            checks = [
                msg.author.id == 365975655608745985,
            ]
            return  all(checks)

        user = mentions[0]
        pref = self.prefix_dict.get(str(message.guild.id), None)
        if pref:
            with open(self.pokelist_path,'r') as f:
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
            

    async def on_ready(self):
        print("Logged in.\n---PokeBall SelfBot v1.0----\n"
              f"Command Prefix: {self.configs['command_prefix']}\n"  
              f"Priority: {', '.join(self.configs['priority'])}\n"
              f"Untradable Pokemon: {', '.join(self.configs['safe_list'])}\n"
              f"Catch Rate: {self.configs['catch_rate']}%\n"
              f"Catch Delay: {self.configs['delay']} seconds\n"
              f"Delay On Priority: {'On' if self.configs['delay_on_priority'] == True else 'Off'}")

