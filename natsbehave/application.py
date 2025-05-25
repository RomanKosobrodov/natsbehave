import json

from natsbehave.compare import Comparator
import nats
import nats.errors
from dataclasses import dataclass
from typing import Union

def serialise(d):
    return json.dumps(d).encode("utf-8")


@dataclass
class Message:
    subject : str
    headers: Union[dict, None]
    data: bytes


class Application:
    def __init__(self, *args, **kwargs):
        self.connection = None
        self.args = args
        self.kwargs = kwargs

    async def __aenter__(self):
        if self.connection is None:
            self.connection = await nats.connect(*self.args, **self.kwargs)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

    def __check__(self):
        if self.connection is None:
            raise RuntimeError("This function can only be called from within the context")

    async def received(self, on):
        self.__check__()
        await self.connection.publish(subject=on["subject"],
                                      payload=serialise(on["data"]),
                                      headers=on["headers"])

    async def sends(self, msg):
        self.__check__()
        subscription = await self.connection.subscribe(msg["subject"])
        timeout = msg.get("timeout", "1.0")
        match = msg.get("match", "equal")
        try:
            nats_message = await subscription.next_msg(timeout=timeout)
            cmp = Comparator[match]
        except nats.errors.TimeoutError:
            return False
        reference = Message(subject=msg["subject"],
                            headers=msg["headers"],
                            data=msg["data"])
        return cmp(nats_message, reference)
