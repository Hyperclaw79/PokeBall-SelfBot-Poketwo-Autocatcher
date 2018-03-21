import asyncio
import discord

class Paginator:
    def __init__(self, message, base, embeds, obj):
        self.message = message
        self.base = base
        self.pointers = ['👈','👉','❌']
        self.embeds = embeds
        self.cursor = 0
        self.obj = obj

    async def _add_handler(self):
        def reaction_check(reaction,user):
            return user == self.message.author and reaction.message.id == self.base.id and reaction.emoji in self.pointers
        while True: 
            reaction, user = await discord.Client.wait_for(self.obj, event='reaction_add', check=reaction_check)
            op = self.pointers.index(reaction.emoji)
            if op == 1 and self.cursor < len(self.embeds) - 1:
                self.cursor += 1
                await self.base.edit(embed=self.embeds[self.cursor])
            elif op == 0 and self.cursor > 0:
                self.cursor -= 1
                await self.base.edit(embed=self.embeds[self.cursor])
            elif op == 2:
                await self.base.delete()
                break    
            else:
                pass

    async def _remove_handler(self):
        def reaction_check(reaction,user):
            return user == self.message.author and reaction.message.id == self.base.id and reaction.emoji in self.pointers
        while True: 
            reaction, user = await discord.Client.wait_for(self.obj, event='reaction_remove', check=reaction_check)
            op = self.pointers.index(reaction.emoji)
            if op == 1 and self.cursor < len(self.embeds) - 1:
                self.cursor += 1
                await self.base.edit(embed=self.embeds[self.cursor])
            elif op == 0 and self.cursor > 0:
                self.cursor -= 1
                await self.base.edit(embed=self.embeds[self.cursor])
            else:
                pass                    

    async def run(self):
        await self.base.edit(content=self.message.author.mention,embed=self.embeds[0])
        for pointer in self.pointers:
            await self.base.add_reaction(pointer)
        asyncio.ensure_future(self._add_handler())
        asyncio.ensure_future(self._remove_handler())

class Embedder:
    def __init__(self, image):
        self.image = image

    def generate(self, title, fields, current, total):
        def _len_check(embed, field_name, description):
            i = 5
            content = description
            while i > 0:
                if len(content) <= 1024:
                    embed.add_field(name=field_name, value=content, inline=False)
                    break
                else:
                    content = '\n'.join(content.split('\n\n')[:i])
                    i -= 1
        hub_embed = discord.Embed(title=title,description="\u200B",color=15728640)
        for name, content in fields.items():
            _len_check(hub_embed, name, content)
        hub_embed.set_footer(text="{}/{}".format(current, total),icon_url=self.image)
        return hub_embed