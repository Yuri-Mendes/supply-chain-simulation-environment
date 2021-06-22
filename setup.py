import os
from setuptools import setup, find_packages

# Declare your non-python data files:
# Files underneath configuration/ will be copied into the build preserving the
# subdirectory structure if they exist.
data_files = []
for root, dirs, files in os.walk('configuration'):
    data_files.append((os.path.relpath(root, 'configuration'),
                       [os.path.join(root, f) for f in files]))

setup(
    # SupplyChainSimulationEnvironment
    # We could also call it miniscot, however I prefer keeping the name more (technically) precise.
    name="scse",
    version="1.0",
    license=
    'Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.',
    url=
    'https://code.amazon.com/packages/SupplyChainSimulationEnvironment/trees/mainline',
    author='Supply Chain Optimization Technology',
    author_email='miniscot@amazon.com',

    # declare your packages
    packages=find_packages(where="src", exclude=("test", )),
    package_dir={"": "src"},

    # include data files
    data_files=data_files,
    package_data={"": ["*.csv", "*.csv.gz", "*.txt", "*.json"]},
    include_package_data=True,

    # declare your scripts
    # If you want to create any Python executables in bin/, define them here.
    # This is a three-step process:
    #
    # 1. Create the function you want to run on the CLI in src/supply_chain_simulation_environment/cli.py
    #    For convenience I usually recommend calling it main()
    #
    # 2. Uncomment this section of the setup.py arguments; this will create
    #    bin/SupplyChainSimulationEnvironment (which you can obviously change!) as a script
    #    that will call your main() function, above.
    #
    #entry_points="""\
    #[console_scripts]
    #miniscot = scse.main.cli:main
    #""",
    entry_points={'console_scripts':['miniscot=scse.main.cli:main']},
    #
    # 3. Uncomment the Python interpreter and Python-setuptools in the
    #   dependencies section of your Config. This is necessary to guarantee the
    #   presence of a runtime interpreter and for the script generated by
    #   setuptools to find its function.

    # Control whether to install scripts to $ENVROOT/bin. The valid values are:
    # * "default-only": install scripts for the version corresponding to
    #   Python-default in your version set. If this package doesn't build for
    #   that version, you won't get root scripts.
    # * True: always install scripts for some version of python that the package
    #   builds for (in practice, this will be the last version that is built).
    #   Note that in this case, you also need to ensure that the appropriate
    #   runtime interpreter is in the dependency closure of your environment.
    # * <a specific python version, e.g. "python3.6" or "jython2.7">: only
    #   attempt to install root scripts for the specific interpreter version. If
    #   this package is in a version set where that interpreter is not enabled,
    #   you won't get root scripts. You almost certainly don't want this.
    root_script_source_version="default-only",

    # Use the pytest brazilpython runner. Provided by BrazilPython-Pytest.
    test_command='brazilpython_pytest',

    # Use custom sphinx command which adds an index.html that's compatible with
    # code.amazon.com links.
    doc_command='amazon_doc_utils_build_sphinx',

    # This is used for local deployment (outside of Brazil).
    # This needs to be updated manually as Config changes.
    install_requires = [
        'numpy == 1.*',
        'scipy == 1.*',
        'pandas == 0.24.*',
        'networkx == 2.*',
        'cmd2 == 0.8.*',
        'boto3 == 1.*',
        's3fs == 0.1.*',
        'docker == 3.7.*',
        'requests == 2.*',
        'gym == 0.17.0',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=['pytest', 'pytest-cov'])
