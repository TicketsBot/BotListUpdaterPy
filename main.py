import toml
import requests
import time
import asyncio

async def main():
    config = toml.load("config.toml")

    while True:
        time.sleep(int(config['serverCounter']['cooldown']))

        url = '{}/total'.format(config['serverCounter']['baseUrl'])
        res = requests.get(url).json()
        count = res['count']

        await updateDbots(config, count)
        await updateDblCom(config, count)

async def updateDbots(config, count):
    url = '{}/bots/{}/stats'.format(config['botlists']['dbotsorg']['baseUrl'], config['id'])
    data = {'server_count': count}
    headers = {'Authorization': config['botlists']['dbotsorg']['apiKey']}
    requests.post(url, data=data, headers=headers)

async def updateDblCom(config, count):
    url = '{}/bots/{}/stats'.format(config['botlists']['dblcom']['baseUrl'], config['id'])
    data = {'guilds': count}
    headers = {'Authorization': 'Bot {}'.format(config['botlists']['dblcom']['token'])}
    requests.post(url, data=data, headers=headers)

asyncio.run(main())
