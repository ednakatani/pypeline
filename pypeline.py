class pypeline():

    def __init__(self, *args, **kwargs):
        self._steps = []
        self._kwargs = kwargs

    def add(self, step):
        self._steps.append(step)
        return self

    def run(self, data):
        for step in self._steps:
            data = step(data, **self._kwargs)
        return data