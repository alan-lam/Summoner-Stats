import requests, json

# champion ID's
res = requests.get('http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json')
id_dict = json.loads(res.text)
ids = list(map(lambda x: int(id_dict['data'][x]['key']), id_dict['data']))
championIdMap = dict(zip(ids, id_dict['data'].keys()))

# queue types
res = requests.get('http://static.developer.riotgames.com/docs/lol/queues.json')
queueTypes = json.loads(res.text)

# items
res = requests.get('http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/item.json')
itemMap = json.loads(res.text)
