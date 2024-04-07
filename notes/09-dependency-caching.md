# Dependency Caching

Each job has some dependencies that must be made available to the runner VMs. Often these dependencies are the same across multiple jobs. If those jobs were running in parallel, then getting the dependencies would not add to the overall workflow run time. However, many jobs run in a sequence and installing the same dependencies in multiple runner VMs can add to the workflow run time.

![](img/caching-dependencies.png)

Reducing the workflow duration is key to - 

  - Reducing compute costs
  - Deploying faster.

A great way to speed up the process is to **cache the dependencies**. Fortunately GitHub Actions provides an action called [`cache`](https://github.com/actions/cache)