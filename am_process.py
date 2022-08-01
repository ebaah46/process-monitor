
class AMProcess:
    def __init__(self, process={}) -> None:
        if len(process) > 0:
            self.pid = process['pid']
            self.name = process['name']
            self.window = process['window']
            self.window_title = process['title']
            self.owner = process['owner']
            self.status = process['window']
            self.createdAt = process['createdAt']
            self.memory = process['memory']
            self.cpu = process['cpu']
            self.active = process['active']

    def kill_process(self, pid) -> int:
        # Kill process implemetation
        pid = 0
        return 0  # return code of kill command
