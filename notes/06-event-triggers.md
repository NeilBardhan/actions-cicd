# Events to trigger workflows

**Events** are workflow triggers that cause a workflow to run. Some events are **repository based**, wherein, events occuring within that repo like **push**, **merge** or **commit** are events that trigger workflow executions.

## Example Events

### `push`

We add the `push` event using `on: push` in our `.yml` file. Every commit that is pushed to every branch triggers that workflow.