# Multiple jobs per workflow

A workflow can have multiple jobs in each workflow. **Every job has it's own runner**. Each job is completely isolated from other machines and jobs.

When developing a python package, developers usually follow this 3 stage process - 

  1. `test`: Developing and testing the package.
  2. `build`: Building the package to generate the package wheel.
  3. `register`: **Uploading** or **deploying** the package to an online registry, usually **pypi** for open source or **artifactory** for proprietary packages.

Each of these 3 stages should be an independent job in a fully automated CI/CD workflow.

replace `python setup.py sdist bdist_wheel` with `python -m build --sdist` and `python -m build --wheel`