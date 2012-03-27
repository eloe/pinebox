import os
import subprocess

if "VIRTUAL_ENV" not in os.environ:
    sys.stderr.write("$VIRTUAL_ENV not found.\n\n")
    parser.print_usage()
    sys.exit(-1)
virtualenv = os.environ["VIRTUAL_ENV"]
file_path = os.path.dirname(__file__)
subprocess.call(["pip", "install", "-E", virtualenv, "--requirement",
                 os.path.join(file_path, "requirements.txt")])
       
dst_dir = os.path.join(virtualenv, "lib/python2.7/site-packages/hardlycode")
hc_lib_path = os.path.dirname(os.getcwd())  
hc_lib_dir = os.path.join(hc_lib_path, "hardlycode/hardlycode")
if not os.path.islink(dst_dir):
    os.symlink(hc_lib_dir, dst_dir)                 