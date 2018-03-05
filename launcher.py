import sys
import secret
from pokeball import PokeBall

if __name__ == "__main__":
    try:
        config_path = sys.argv[1]
        guild_path = sys.argv[2]
        pokelist_path = sys.argv[3]
    except:
        config_path = 'config.json'
        guild_path = 'guilds.json'
        pokelist_path = 'pokelist.log'

    bot = PokeBall(config_path, guild_path, pokelist_path)
    bot.run()
