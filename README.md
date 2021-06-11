# pxpowershell

This module lets you interact with a Powershell Prompt from Python.   It is intended to provide similar functionality to "pxssh" or "redexpect" but for Powershell.

Why not subprocess? Subprocess does something different.  It executes a single process and captures the output. pxpowershell lets you enstantiate a powershell process and then interact with it.  Variables are saved form command to command.  Functions defined in one command can be called later and so forth.

# Usage

```
    x = pxpowershell()
    x.start_process()
    x.run("$a = 10000")
    print(x.run("$a + 1"))
    result = x.run("get-process")
    print(result)
    x.stop_process()
```

# Installing
I recommending setuping up a virtual machine (although not required)

```
c:\> py -m venv \path\to\new\venv\folder
c:\> \path\to\new\venv\folder\bin\activate.bat
```
Then pip install:
```
c:\> py -m pip install git+https://github.com/markbaggett/pxpowershell
```

# Example

If you used a virtual environment so the install can run properly you now have a new command line utility called "dir2iso" installed:
```
(pxpowershell) C:\Users\User\Documents\GitHub\pxpowershell>dir2iso --help
usage: dir2iso [-h] source destination title

positional arguments:
  source       The path to the directory to turn into an ISO
  destination  The destination ISO file to create (including path).
  title        The title of the ISO.


optional arguments:
  -h, --help   show this help message and exit
```
This utility will create a .ISO file containing the specified directory. This is done using a demonstration script to shows how easily you can interact with Powershell. The Powershell Script that does all the real work came from @wikijm. Buy him a coffee.

https://github.com/wikijm/PowerShell-AdminScripts/blob/master/Miscellaneous/New-IsoFile.ps1

Here is everything the script really does:
```
def dir2iso(src, dest, title="Created by pxpowershell"):
    pshell = pxpowershell.PxPowershell(debug=False)
    x = pshell.start_process()
    x = pshell.run(powershell_script, 10)
    x = pshell.run(f"cd {src}")
    result = pshell.run(f"New-IsoFile {src} -path {dest} -title {title} -Force", 60*60)
    result = pshell.run(f"ls {dest}")
    pshell.stop_process()
    return result
```

You start the powershell process. We send in the new-isofile script, then execute it capturing the results.  Notice that each call to .run passes the command to send to powershell and a timeout to wait for the command to finish and return to the Powershell Prompt.  If no timeout is provided the default is 3 seconds.
