import os
import json

def alter_config(path):
    with open(path,'r', encoding='utf-8') as f:
        configs = json.load(f)
    configs["token"] = os.environ["DISCORD_BOT_TOKEN"]
    with open('config.json','w') as f:
        f.write(json.dumps(configs,indent=3))
