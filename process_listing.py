from multiprocessing.dummy import Process
import psutil as p
from am_process import AMProcess as amp
from app_constants import AppConstants as apc
import pprint
from xdolibtest import ScriptRepo


class ProcessListing:

    processes = {}  # List of all running processes

    def __init__(self) -> None:
        self.current_process = None  # pointer to the current process being handled
        pass

        @classmethod
        def all_processes(cls):

            amp(ScriptRepo.list_processes())
            


''' 
    @classmethod
    def list_all(cls) -> None:
        p = subprocess.Popen(["wmctrl", "-lp"], stdout=subprocess.PIPE)
        out, err = p.communicate()
        query_output = out.decode("utf-8")
        lines = query_output.strip().splitlines()
        cls.processes = {}
        for line in lines:
            # retrieve process name
            owner = line.split()[3]
            pid = line.split()[2]
            title = line.split()[4:]

 '''

if __name__ == "__main__":
    ProcessListing.list_all()
    pprint.pprint(ProcessListing.processes)
