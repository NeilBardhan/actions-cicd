# Creating a workflow

Workflows for GitHub Actions can be created in different ways primarily - 

  - Using the GitHub web UI.
  - Creating the workflow `.yml` files locally.

For the first workflow, let's use the GitHub web UI.

## Using the GitHub web UI

  1. Navigate to the `Actions` tab of the repository.

![actions](/img/02-actions-tab-ui.png)

  2. Click on `Configure` in the suggested `Simple workflow` tile to open an editor window.
  3. This will create a `.github` folder with a `workflows` subfolder which contains a `blank.yml` file. The `blank.yml` file **must be renamed to something else**, for example, `first-workflow.yml`. For GitHub to be able to detect workflows, they must follow this directory structure. **A workflow is defined in `.yml` files.**

```bash
.
└── .github/
    └── workflows/
        └── first-workflow.yml
```
  4. **Each workflow must have a name**. Using the `name` keyword, we can give the workflow a name.

```yml
name: First Workflow
```

  5. Then we must define, **when the workflow should be executed**. This is done by adding the `on` key, which defines the event or events that should trigger this workflow. In the example below, I use `workflow_dispatch` event which makes sure that a user can manually trigger this workflow. **This is an event that waits for the user  to manually start this workflow**. GitHub Actions defines many events of varying complexity and automation.

```yml
name: First Workflow
on: workflow_dispatch
```

  6. Now we have to define, the actual **work that this workflow does** and for this we need the `jobs` key. A job **must have a name** and we must define the **runner** which is the environment in which the job will be executed. GitHub Actions provides a wide variety of runners and this is identified with the `runs-on` key.

```yml
name: First Workflow
on: workflow_dispatch
jobs:
  first-job:
    runs-on: ubuntu-latest
```
  7. Finally we define the **steps** which the job must perform. A job can have multiple steps, each of which are signified by the `-` after the `steps` keyword. Note that, `yml` is an indentation based markup language and the indentation block defines the "section" that the code is part of. So, in our example the indentation after `jobs` means that indented section is part of the `jobs` definition in the workflow `yml` file. Each step, **must have a name**, and within each step the `run` command is where our core actions are defined. These are the commands that either trigger scripts or shell commands. For example, we could simply use `echo` to do some basic printing.

```yml
name: first-workflow
on: workflow_dispatch
jobs:
  first-job:
    runs-on: ubuntu-latest
    steps:
      - name: print-greeting
        run: echo "This is the first step ever!"
      - name: print-goodbye
        run: echo "Done, for now, goodbye!"
```