class Queue:
    def __init__(self, server):
        self.queue = []
        self.server = server

    def add(self, other):
        self.queue.append(other)

    async def next(self):
        if self.queue:
            res = self.queue[0]  # res - это кортеж со всеми параметрами функции запуска песни (ctx, *args)
            del self.queue[0]
            await self.server.play(*res)
        else:
            return None

    def clear(self):
        self.queue = []

    def get_queue(self):
        return self.queue
