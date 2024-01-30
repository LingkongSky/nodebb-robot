import asyncio
import yaml
from decode import inputs


async def main():
    with open('./config.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        for i in result['robots']:
            await inputs(i)


loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
