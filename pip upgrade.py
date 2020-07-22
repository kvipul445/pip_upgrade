import pkg_resources
from subprocess import call,check_output,run,PIPE

packages = [dist.project_name for dist in pkg_resources.working_set]
print("Getting the list of outdated packages.")

_a = check_output(["pip3","list","--outdated"])
_output = _a.decode("utf-8")
print(_output)
outdated_packages = _output.split('\n')
package_name = []

def get_package_name(r):
    p = r.split(' ')
    return p[0]
if len(outdated_packages) >= 3:
    del outdated_packages[0]
    del outdated_packages[0]

    for i in range(len(outdated_packages)-1):
        package_name.append(get_package_name(outdated_packages[i]))

print("Getting list complete\n Now upgrading packages.")
call("pip3 install --upgrade " + ' '.join(package_name), shell=True)
print("Upgrading Packages are complete.")
print("Checking for each package upgrade.")
call("pip3 install --upgrade " + ' '.join(packages),shell=True)
print("Checking for each package upgrade complete.")
print("Checking for the requirements")
print("Starting")
no_of_broken_packages = call("pip3 check", shell=True)

def get_output(output):
    lines = output.split('\n')
    d = []
    for line in lines:
        c = line.split(' ')
        d.append(str(c[0]))
    len_output = len(d)
    del d[len_output -1]
    print("Broken packages")
    print(d)
    call("pip3 install --upgrade " + ' '.join(d),shell=True)
        
if no_of_broken_packages != 0:
    _output1 = run(["pip3","check"],stdout=PIPE).stdout.decode('utf-8')
    get_output(_output1)
print("checking Complete")
