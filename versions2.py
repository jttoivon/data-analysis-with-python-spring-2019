#!/usr/bin/env python3

from pkg_resources import parse_version

libraries = {
    "python":     "3.7",
    "numpy":      "1.13.3",
    "pandas":     "0.22.0",
    "matplotlib": "2.1.1",
    "sklearn":    "0.19.1",
    "scipy":      "0.19.1",
    "seaborn":    "0.8.0",
    "statsmodels":    "0.9.0",
#    ["lxml":       "4.2.5"
}

installed = {}


import sys
missing=[]
old=[]

def helper(name, required_version):
    try:
        x = __import__(name)
    except ModuleNotFoundError:
        x = None
    if x:
        #print("%s version: %s from file %s" % (name, x.__version__, x.__file__))
        if parse_version(x.__version__) < parse_version(required_version):
            old.append(name)
        installed[name] = (x.__version__, x.__file__)
    else:
        #print("%s not installed" % name)
        installed[name] = ("-", "-")
        missing.append(name)

python_version = ".".join(map(str, sys.version_info[:3]))
#print(python_version)
print("Python version:", sys.version.split('\n')[0])
for library, required_version in libraries.items():
    if library == "python":
        installed[library] = (python_version, "-")
        if parse_version(python_version) < parse_version(libraries[library]):
            old.append(library)
    else:
        helper(library, required_version)

library_length = max([ len(library) for library in installed ])
version_length = max([ len(version) for version, location in installed.values() ])
required_length = max([ len(required_version) for required_version in libraries.values() ])
library_length = max(library_length, len("Library"))
version_length = max(version_length, len("Version"))
required_length = max(required_length, len("Required"))
print("%-*s %*s %*s %s" % (library_length, "Library", version_length, "Version", required_length, "Required",
                          "Location"))
for library in installed:
    version, location = installed[library]
    required = libraries[library]
    print("%-*s %*s %*s %s" % (library_length, library, version_length, version, required_length, required, location))
print()


if missing:
    print("The following libraries are missing:")
    for library in missing:
        print(library)

if old:
    print("The following libraries are too old:")
    for library in old:
        print(library)
#print(installed)

print()

if missing or old:
    print("Installation is not complete!")
else:
    print("Installation is complete!")
    
