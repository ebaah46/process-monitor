from subprocess import PIPE
import subprocess
import pprint as pp
import psutil as p
from brotab import api


class ScriptRepo:

    @staticmethod
    def list_processes() -> dict:
        response = {}
        process = subprocess.Popen(["wmctrl", "-lp"], stdout=PIPE)
        out, err = process.communicate()
        # print(out)
        if err is None:
            windows = out.decode("utf-8").strip().splitlines()
            # Query for active window
            process = subprocess.Popen(
                ["xprop", "-root", "32x", "$0", "_NET_ACTIVE_WINDOW"], stdout=PIPE)
            out, err = process.communicate()
            active = out.decode("utf-8").strip().split("(WINDOW)")[1]
            for line in windows:
                process_details = {}
                # if window is the active window set active marker in data
                # comparison is done via hex conversion since the different ouputs have different hex notations
                process_details['active'] = True if int(line.split()[
                    0], 16) == int(active, 16) else False
                process_details['window'] = line.split()[0]
                process_details['pid'] = line.split()[2]
                process_details['owner'] = line.split()[3]
                process_details['title'] = "".join(line.split()[4:])
                for proc in p.process_iter(["pid", "name"]):
                    proc_details = proc.as_dict()
                    if proc.info['pid'] == int(line.split()[2]):
                        process_details['name'] = proc_details['name']
                        process_details['createdAt'] = proc_details['create_time']
                        process_details['status'] = proc_details['status']
                        process_details['cpu'] = proc_details['cpu_percent']
                        process_details['memory'] = proc_details['memory_percent']
                        break
                response.update({line.split()[2]: process_details})
        return response

    @staticmethod
    def get_browser_tabs() -> dict:
        from brotab import main
        response = {}
        clients = main.create_clients()
        if len(clients) == 0:
            response['success'] = False
            response['message'] = 'No browser clients found'
        # Loop through all browser clients
        for client in clients:
            print(client._pid)
            exit()
            tabs = client.list_tabs_safe(None)
            msg = {}
            for tab in tabs:
                tab_info = tab.split('\t')
                # msg[f'{}']


if __name__ == "__main__":
    processes = ScriptRepo.list_processes()
    pp.pprint(processes)
    ScriptRepo.get_browser_tabs()
