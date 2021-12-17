#run.py
#Run subroutines in the operative system return output
# See LICENSE
import subprocess

class Run():
    @staticmethod
    def return_all(command):
        arr = command.split(' ', 1)
        result = subprocess.run(arr, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')