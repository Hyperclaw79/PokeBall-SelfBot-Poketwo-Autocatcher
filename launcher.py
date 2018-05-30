import sys
from pokeball import PokeBall
#from secret import alter_config

if __name__ == "__main__":
    try:
        config_path = sys.argv[1]
        guild_path = sys.argv[2]
        pokelist_path = sys.argv[3]
        pokenames_path = sys.argv[4]
    except:
        config_path = 'config.json'
        guild_path = 'guilds.json'
        pokelist_path = 'pokelist.log'
        pokenames_path = 'pokenames.json'

    #alter_config(config_path)
    bot = PokeBall(config_path, guild_path, pokelist_path, pokenames_path)
    bot.run()
