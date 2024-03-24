# Setting up Runners

The workflows, jobs and steps we define in GitHub Actions run on **Runners** which are **virtual machines that are run on GitHub servers or servers specified by us, the users**. The actions are **not being executed inside the repository**. **The repository is not a server** and lives on a different machine owned by GitHub.

While actions and workflows are **defined in the repository**, they are being run on essentially blank virtual machine instances on GitHub servers. The very basic default runners do not have pre-loaded environments and do not have access to the repository code. **We have to create a job or a step to get the runner access to the repo code by downloading our repo inside of the runner environment**.

## Getting the repo code in our runner

### Manual method

In this method, we `git clone` into our repository from the runner CLI, `cd` into our repo git folder and checkout the current branch. 

```yml
name: runner-env-setup
on: push
jobs:
  runner-env-setup:
    runs-on: ubuntu-latest
      steps:
        - name: get-code
          run: |
            echo $GITHUB_WORKSPACE
            git clone https://github.com/NeilBardhan/actions-cicd.git
            cd actions-cicd
            git checkout ${GITHUB_REF##*/}
```

## Using the pre-defined GitHub `checkout` Action from Actions Marketplace

Actions are pre-defined operations that are made available to users of GitHub Actions to simplify tasks that are performed repeatedly.

Actions are developed by the wider GitHub community or by GitHub themselves. GitHub have developed the [checkout](https://github.com/actions/checkout) action that checks out our repository into the runner under `$GITHUB_WORKSPACE`. This enables our workflow to access the repository.

```yml
name: runner-env-setup
on: push
jobs:
  runner-env-setup:
    runs-on: ubuntu-latest
      steps:
        - name: get-code-checkout
          uses: actions/checkout
          with: 
            ref: ... #define branch here
```