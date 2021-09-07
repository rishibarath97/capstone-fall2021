import subprocess

bashCommand = "./botb-linux-amd64 -find-sockets=True | grep \"docker.sock\""

process = subprocess.run(bashCommand.split(), stdout=subprocess.PIPE)
output = process.stdout.decode('utf-8').split("\n")
if(len(output[2:-2]) > 1):
        # print(output[2:-2])
        for socket in output[2:-2]:
                if("docker" in socket):
                        print("Found DOCKER SOCKET AT",socket.split(":")[-1].strip())
else:
        print("Cannot break out with docker socket. No socket exists!")

bashCommand = "fdisk -l"

try:
    process = subprocess.run(bashCommand.split(), stdout=subprocess.PIPE)
    errorcode = process.returncode
    output = process.stdout.decode('utf-8')
    print(output)
except FileNotFoundError:
    errorcode = 0

if(errorcode == 0):
        print("Does not have privilege flag mounting capabilities")
else:
        print("HAS PRIVILEGE FLAG CAPABILITIES. Can break out of docker!")
