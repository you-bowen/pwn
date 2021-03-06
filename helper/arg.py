import argparse
parser = argparse.ArgumentParser(
    description="process helper",
)
parser.add_argument('-i','--ida',  action="store_true", help="ida mode")
parser.add_argument('-d','--debug',  action="store_true", help="debug mode")
parser.add_argument('-o','--og',  action="store_true", help="update one_gadget info in .helper")
parser.add_argument('-b','--buu',  type=int, help="buuoj ubuntu version")
parser.add_argument('-H','--host',  type=str, help="host u want to connect")
parser.add_argument('-p','--port',type=int, help="specify port")
parser.add_argument('-P','--patch',type=float, help="patch AIO version")
parse_args = parser.parse_args
