# meta developer: @zenmhy

import re
from .. import loader
import logging

logger = logging.getLogger(__name__)

@loader.tds
class yg_actCryptoBotModule(loader.Module):
    """Активатор чеков @CryptoBot которые отправляют в виде ссылки"""
    strings = {
        "name": "CryptoLink+",
    }

    async def client_ready(self, client, db):
        self.client = client
        await client.send_message('CryptoBot', '/start')

    async def watcher(self, message):
        if message.raw_text and 't.me/CryptoBot?start=' in message.raw_text:
            urls = re.findall(r't.me/CryptoBot\?start=([A-Za-z0-9]+)', message.raw_text)
            for code in urls:
                command = f'/start {code}'
                await message.client.send_message('CryptoBot', command)
                await message.mark_read()

    async def CryptoBotcmd(self, message):
        """Включить Активатор"""
        await message.edit("<b>Активатор @CryptoBot работает ✅")