import json

def alter_config(path):
    with open(path,'r') as f:
        configs = json.load(f)
    configs["token"] = "MzYyOTU1NDEwMjU4NTI2MjA5.DX8_xg.h-gkv1wzzizMkeZm8LZ6EnE2AQ4"
    with open('config.json','w') as f:
        f.write(json.dumps(configs,indent=3))
