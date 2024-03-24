# Key Components of GitHub Actions

The fundamentals and key building blocks of GitHub Actions are -

  - **Workflows**: Workflows are attached to GitHub repositories. A repo can have one or more workflows. The workflow is the highest level building block in GitHub Actions. It is a definition of an automation process within GitHub Actions.
  - **Jobs**: A workflow includes one or more jobs, which are "units" of work or a series of tasks that need to be performed. These tasks are tied to a job and are called **steps**.
  - **Steps**: Steps are actual tasks that need to be performed in each job. Each job contains a series of one or more steps, which are **executed in the order in which they are specified**. For example: download the code in the first step, install the package in the second step and run the tests in the third step.
  - **Actions**: An Action is a separate feature offered by GitHub Actions. An Action is different from a workflow in the sense that, it is a custom application that performs a complex, but frequently repeated task.

We can have as many workflows as we want, as many jobs in each workflow with as many steps in each job as we would like.


![components](/img/01-actions-building-blocks.png)

## Workflows

  - Attached to a GitHub repository.
  - Contains one or more jobs.
  - Workflows are not executed all the time but with GitHub Actions we can assign **triggers** or **events** to our workflows. **These events define when a given workflow will be executed.** For example, we can add an event that triggers and executes a workflow whenever a new commit is pushed to a certain branch.

## Jobs

  - Jobs are things inside the workflow that contain the steps that will be executed when an event triggers a workflow.
  - Every job defines a **runner** - which is an execution environment (virtual machine/OS) where the steps will be executed. With GitHub Actions these runners can be pre-defined by GitHub or custom configured by the users.
  - Jobs contain one or more steps that execute in **sequential** order.
  - A workflow can have **one or more** jobs and **by default, jobs are run in parallel**. However, GitHub Actions lets users customize jobs to be run in **sequential order** and we can also set up **conditional jobs**, which will only run if certain conditions are met by preceding jobs.

## Steps
  - This is where the actual work is defined as a command line command or shell script. A step can also be an **Action**, which is a predefined script that performs certain tasks.
  - Steps run in sequence and they can be conditional.

## Actions
  - Actions are complex, pre-defined applications that are distributed in the GitHub Actions Marketplace. These Actions are complex tasks that are commonly performed like, **checking out the gihub code repo** into a blank runner environment.
  - Actions can be defined by the user, but are usually 3rd party applications either built by GitHub themselves or by the community of users. For example [checkout](https://www.github.com/actions/checkout) is an action defined by GitHub that provides a faster way to check out a repo into a runner environment.
  - There is a marketplace for the Actions where different Actions can be found and verified by the community. The marketplace is also where the Actions are documented.