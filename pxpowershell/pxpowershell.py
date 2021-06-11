import pexpect
import re
import time
import sys
import random

from pexpect.popen_spawn import PopenSpawn

class PxPowershell(object):
    def __init__(self, *args, debug=False, **kwargs):
        self.cmd = "powershell.exe"
        self.unique_prompt = f"XYZPEXPECT{random.randint(1,99999999):0>X}XYZ"
        self.orig_prompt = ""
        self.process = ""
        self.debug = debug
    def start_process(self):
        self.process =  pexpect.popen_spawn.PopenSpawn(self.cmd)
        if self.debug:
            self.process.logfile = sys.stdout.buffer
        time.sleep(4)
        init_banner = self.process.read_nonblocking(4096, 2)
        if self.debug:
            print(init_banner)
        try:
            prompt = re.findall(b'PS [A-Z]:', init_banner, re.MULTILINE)[0]
        except Exception as e:
            raise(Exception("Unable to determine powershell prompt. {0}".format(e)))
        self.process.sendline("Get-Content function:\prompt")
        self.process.expect(prompt)
        #The first 32 characters will be the command we sent in
        self.orig_prompt = self.process.before[32:]
        if self.debug:
            print(f"Original prompt: {self.orig_prompt}  -> {self.unique_prompt}")
        self.process.sendline('Function prompt{{"{0}"}}'.format(self.unique_prompt))
        self.process.expect(self.unique_prompt)
        self.clear_buffer()
    def clear_buffer(self):
        #repeat expecting the prompt until there are no more. One thing that nessesitates this is when extra CRLFs are sent to run().
        while self.process.expect([self.unique_prompt, pexpect.EOF, pexpect.TIMEOUT], timeout=1) == 0:
             pass
    def restore_prompt(self):
        self.process.sendline('Function prompt{{"{0}"}}'.format(self.orig_prompt))
        self.process.expect(self.orig_prompt)
    def run(self,pscommand, timeout=-1):
        self.clear_buffer()
        self.process.sendline(pscommand)
        self.process.expect(self.unique_prompt, timeout=timeout)
        #capture result but trim off the command and the CRLF
        result = self.process.before[len(pscommand)+2:]
        self.clear_buffer()
        return result
    def stop_process(self):
        self.process.kill(9)
