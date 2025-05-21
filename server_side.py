import subprocess
import time

def run_local_command(command):
    try:
        # Run the command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr

    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' returned non-zero exit status {e.returncode}")
        print(f"Error output: {e.stderr}")
timestep = int(time.time())
error = 'grep -i "error" /var/log/syslog | wc -l'
info = 'grep -i "info" /var/log/syslog | wc -l'
warn = 'grep -i "warn" /var/log/syslog | wc -l'

error_run = run_local_command(error)
info_run = run_local_command(info)
warn_run = run_local_command(warn)

print(timestep)
print(f'error: {error_run}')
print(f'info {info_run}')
print(f'warn {warn_run}')

