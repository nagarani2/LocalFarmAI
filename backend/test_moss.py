import asyncio

from moss_retrieval import (
    load_farming_index,
    search_farming_knowledge
)


async def test():
    await load_farming_index()

    results = await search_farming_knowledge(
        "Why are rice leaves yellow?"
    )

    print(results)


asyncio.run(test())