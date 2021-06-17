import os
import pyautogui

BASE_TOOL_PATH = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\FLARE\\"

tool_paths = {
    'exeinfope': os.path.join(BASE_TOOL_PATH, 'Utilities\exeinfope.lnk')
}

# TODO: Malware needs to be passed in from the web interface
MALWARE = "C:\\WINDOWS\\System32\\calc.exe"


def exeinfope():
    program_path = tool_paths['exeinfope']
    os.system(f'"{program_path}" {MALWARE}')
    return 'Working!'


manifest = {
    'exeinfope': exeinfope
}