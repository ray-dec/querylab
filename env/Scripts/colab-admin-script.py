#!"c:\users\rayane\documents\02 - workspace\python scripts\02 - querylab\querylab\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'colab==1.13.5','console_scripts','colab-admin'
__requires__ = 'colab==1.13.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('colab==1.13.5', 'console_scripts', 'colab-admin')()
    )
