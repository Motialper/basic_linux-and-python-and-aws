from SshToServer import SshToServer
import csv
import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(current_dir, "log_summary_from_server.csv")

key_path = r"C:\Users\moti and shira\python_learn\advance python\linux_poject\finelProject_in_linux\mykye.pem"
host = "13.53.200.175"
user = "ubuntu"


commands = {
    "error": 'grep -i "error" /var/log/syslog | wc -l',
    "info":  'grep -i "info" /var/log/syslog | wc -l',
    "warn":  'grep -i "warn" /var/log/syslog | wc -l'
}
my_ssh = SshToServer(key_path, host, user)

results = {}
for key, cmd in commands.items():
    output, error = my_ssh.runRemoteCommand(cmd)
    results[key] = output.strip() if output.strip().isdigit() else "0"

timestamp = int(time.time())

file_exists = os.path.exists(csv_path)

with open(csv_path, mode="a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Timestamp", "Error", "Info", "Warn"])
    writer.writerow([timestamp, results["error"], results["info"], results["warn"]])    

print("log_summary_from_server.csv")
