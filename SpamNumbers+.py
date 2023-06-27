# meta developer: @zenmhy
import asyncio

from .. import loader


def register(cb):
    cb(SpamNumbersMod())


class SpamNumbersMod(loader.Module):
    """Модуль для Spam числами"""

    strings = {"name": "SpamNumbers"}

    spamming = False

    async def spamscmd(self, message):
        """Spam Числами от 1 до 1000"""
        if self.spamming:
            return

        self.spamming = True

        async def spam_task():
            for num in range(1, 1000):
                if not self.spamming:
                    break
                await message.client.send_message(message.to_id, str(num))
                await asyncio.sleep(0.1)

        await spam_task()
        await message.delete()

    async def stopcmd(self, message):
        """Остановить Spam"""
        if not self.spamming:
            return

        self.spamming = False
        await message.delete()
