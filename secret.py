import json

with open('config.json','r') as f:
    configs = json.load(f)
configs["token"] = os.environ["DISCORD_BOT_TOKEN"]
with open('config.json','w') as f:
    f.write(json.dumps(configs,indent=3))
