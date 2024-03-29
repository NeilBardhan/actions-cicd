# Events to trigger workflows

**Events** are workflow triggers that cause a workflow to run. Some events are **repository based**, wherein, events occuring within that repo like **push**, **merge** or **pull_request** are events that trigger workflow executions.

## Example Events

### `push`

We add the `push` event using `on: push` in our `.yml` file. Every commit that is pushed to the branch triggers that workflow.

## Skipping a workflow run

A workflow can be skipped as follows - 

  - Create a commit with `git commit -m "<message> [skip ci]"`. The `[skip ci]` tells GitHub not to run any push based workflows for this commit.