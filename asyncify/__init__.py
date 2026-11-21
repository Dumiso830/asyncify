#!/usr/bin/env python
def asyncify(func):
    import asyncio
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper