import functools
import os
import subprocess
import sys

import qt5_applications

import qt5_tools


fspath = getattr(os, 'fspath', str)


def run(application_name, environment=os.environ):
    modified_environment = qt5_tools.create_environment(
        reference=environment,
    )
    application_path = qt5_applications._application_path(application_name)

    completed_process = subprocess.run(
        [
            fspath(application_path),
            *sys.argv[1:],
        ],
        env=modified_environment,
    )

    sys.exit(completed_process.returncode)


# designer = functools.partial(run, application_name='designer')
