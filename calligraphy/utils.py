class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def console_error(text):
    print(bcolors.FAIL + str(text) + bcolors.ENDC)

def console_warn(text):
    print(bcolors.WARNING + str(text) + bcolors.ENDC)

def console_success(text):
    print(bcolors.OKGREEN + str(text) + bcolors.ENDC)
