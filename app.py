import subprocess
import sys
import platform

def open_terminal(command):
    """Open termianl based on OS"""
    if platform.system() == "Windows":
        subprocess.Popen(['start', 'cmd', '/K', command], shell=True)
    elif platform.system() == "Darwin":
        subprocess.Popen(['osascript', '-e', 'tell app "Terminal" to do script "{}"'.format(command)])
    else:
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

if __name__ == "__main__":
    print("Hola")

    open_terminal('python3 server.py')
    open_terminal('python3 client.py')
