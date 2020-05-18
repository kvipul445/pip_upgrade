import pkg_resources
from subprocess import call,check_output

packages = [dist.project_name for dist in pkg_resources.working_set]
#print(packages)
#package = ['zipp', 'WTForms', 'wrapt', 'widgetsnbextension', 'wheel', 'Werkzeug', 'webencodings', 'wcwidth', 'urllib3', 'typing-extensions', 'typed-ast', 'traitlets', 'tornado', 'toolz', 'testpath', 'terminaltables', 'terminado', 'termcolor', 'tensorflow', 'tensorflow-estimator', 'tensorboard', 'tensorboard-plugin-wit', 'sqlparse', 'SQLAlchemy', 'sq', 'sphinxcontrib-serializinghtml', 'sphinxcontrib-qthelp', 'sphinxcontrib-jsmath', 'sphinxcontrib-htmlhelp', 'sphinxcontrib-devhelp', 'sphinxcontrib-applehelp', 'Sphinx', 'sphinx-gallery', 'sphinx-copybutton', 'snowballstemmer', 'smart-open', 'six', 'SimpleITK', 'simplegeneric', 'shiboken2', 'setuptools', 'Send2Trash', 'seaborn', 'scipy', 'scikit-learn', 'scikit-image', 's3transfer', 'rsa', 'requests', 'requests-oauthlib', 'QtPy', 'qtconsole', 'pyzmq', 'pywinpty', 'pywin32', 'PyWavelets', 'pytz', 'python-dateutil', 'pytest-runner', 'PySide2', 'pyrsistent', 'PyQt5', 'PyQt5-sip', 'pyparsing', 'pymongo', 'Pygments', 'pycparser', 'pyasn1', 'pyasn1-modules', 'protobuf', 'prompt-toolkit', 'prometheus-client', 'pipupgrade', 'pip', 'pip-upgrader', 'pip-review', 'Pillow', 'pickleshare', 'parso', 'pandocfilters', 'pandas', 'packaging', 'opt-einsum', 'oauthlib', 'numpydoc', 'numpy', 'notebook', 'networkx', 'nbformat', 'nbconvert', 'mysql-connector', 'mysql-connector-python', 'mypy', 'mypy-extensions', 'more-itertools', 'mistune', 'matplotlib', 'marshmallow', 'MarkupSafe', 'Markdown', 'kiwisolver', 'Keras-Preprocessing', 'Keras-Applications', 'jupyter', 'jupyter-core', 'jupyter-console', 'jupyter-client', 'jsonschema', 'joblib', 'jmespath', 'Jinja2', 'jedi', 'itsdangerous', 'ipywidgets', 'ipython', 'ipython-genutils', 'ipykernel', 'importlib-metadata', 'imagesize', 'imageio', 'idna', 'html5lib', 'h5py', 'grpcio', 'google-pasta', 'google-auth', 'google-auth-oauthlib', 'gensim', 'gast', 'Flask', 'Flask-WTF', 'Flask-SQLAlchemy', 'Flask-Login', 'Flask-Bcrypt', 'entrypoints', 'docutils', 'docopt', 'Django', 'defusedxml', 'decorator', 'dask', 'Cython', 'cycler', 'cPython', 'colorclass', 'colorama', 'Click', 'chardet', 'cffi', 'certifi', 'cachetools', 'botocore', 'boto3', 'boto', 'bleach', 'bcrypt', 'backcall', 'Babel', 'attrs', 'astropy', 'astor', 'asgiref', 'alabaster', 'absl-py']
#print(package)

print("Getting the list of outdated packages.")
#outdated_packages = call("pip3 list --outdated",shell=True)

_a = check_output(["pip3","list","--outdated"])
_output = _a.decode("utf-8")
print('_output')
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

def get_output():
    a = check_output(["pip3","check"])
    output = a.decode("utf-8")
    lines = output.split('\n')
    d = []
    for line in lines:
        c = line.split(' ')
        d.append(str(c[0]))
        print(d)
    call("pip3 install --upgrade " + ''.join(d),shell=True)
        
if no_of_broken_packages != 0:
    get_output()
print("checking Complete")

