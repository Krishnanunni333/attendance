import subprocess
import os

def calls():
    kill_previous = subprocess.run("ps aux | grep python | grep app_data | grep -E '[0-9]{8}_[0-9]{6}.py' | awk {'print $2'} | xargs kill", shell=True)

        # Run app in subprocess
    run_my_app = subprocess.Popen(f'streamlit run loc.py', shell=True, preexec_fn=os.setsid)

        # Notify user that app is opening in a new window.
    print('Opening app in a new window. Visit http://localhost:8502/ to access app.')
