import sys
import traceback

def hook_exception_handle():
    sys.excepthook = traceback.print_exc