import pkg_resources
from subprocess import call,check_output,run,PIPE
import numpy as N

#Getting all the python packages in the system
packages = [dist.project_name for dist in pkg_resources.working_set]
print("Getting the list of outdated packages.")

#Getting the outdated packages
_a = check_output(["pip3","list","--outdated"])
_output = _a.decode("utf-8")

print(_output)

outdated_packages = _output.split('\n')
package_name = []

#Function to get the package name
def get_package_name(r):
    p = r.split(' ')
    return p[0]

#Getting all the outdated packages name
if len(outdated_packages) >= 3:
    del outdated_packages[0]
    del outdated_packages[0]

    for i in range(len(outdated_packages)-1):
        package_name.append(get_package_name(outdated_packages[i]))

    del package_name[package_name.index('distro-info')]
    del package_name[package_name.index('tf-nightly')]
    

print("Getting list complete\n Now upgrading packages.")

#Upgrading all the outdated packages
call("pip3 install --upgrade --use-feature=2020-resolver " + ' '.join(package_name), shell=True)

print("Upgrading Packages are complete.")

print("Checking for each package upgrade.")

del packages[packages.index('tf-nightly')]

#Checking and Upgrading individual packages
call("pip3 install --upgrade --use-feature=2020-resolver " + ' '.join(packages),shell=True)

print("Checking for each package upgrade complete.")

print("Checking for the requirements")

print("Starting")

#Checking for the broken requirement
no_of_broken_packages = call("pip3 check", shell=True)

#Function to fix the broken packages
def get_output(output):
    lines = output.split('\n')
    d = []

    for line in lines:
        c = line.split(' ')
        d.append(str(c[0]))

    len_output = len(d)

    del d[len_output -1]

    broken_package = N.array(d)
    broken_package_unique = N.unique(broken_package)
    print("Broken packages")
    print(broken_package_unique)

    call("pip3 install --upgrade --use-feature=2020-resolver " + ' '.join(broken_package_unique),shell=True)
        
while( no_of_broken_packages != 0 ):
    _output1 = run(["pip3","check"],stdout=PIPE).stdout.decode('utf-8')
    get_output(_output1)
    
    no_of_broken_packages = call("pip3 check", shell=True)

print("checking Complete")
