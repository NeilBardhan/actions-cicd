# Multiple jobs per workflow

A workflow can have multiple jobs in each workflow. **Every job has it's own runner**. Each job is completely isolated from other machines and jobs.

When developing a python package, developers usually follow this 3 stage process - 

  1. `test`: Developing and testing the package.
  2. `build`: Building the package to generate the package wheel.
  3. `register`: **Uploading** or **deploying** the package to an online registry, usually **pypi** for open source or **artifactory** for proprietary packages.

Each of these 3 stages should be an independent job in a fully automated CI/CD workflow. In the `build-test.yml` workflow, I define these 2 jobs.

By default, **jobs are run in parallel**. However, we can change that based on our needs. Since, we want to optimize the use of computational resources, it is always preferred to run the `test` job first, followed by the `build` job should the `test` job succeed. One way to do this is to add the `needs` keyword in the `build` job. This ensures that `build` is run after the job defined in the `needs` key value pair succeeds.