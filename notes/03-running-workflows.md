# Running a workflow

Once the workflow changes are merged to main for the first time. In the `Actions` tab of the repository [here](https://github.com/NeilBardhan/actions-cicd/actions), we will see our workflows in the left hand side **Actions** panel. We select `first-workflow` in that panel and that shows us the past runs of the workflow and allows us to manually run the workflow using the **Run Workflow** button. The page is [here](https://github.com/NeilBardhan/actions-cicd/actions/workflows/first-workflow.yml).

![workflow-runs](/img/03-actions-workflow-runs.png)

As the green checkmark indicates, our `first-workflow` run has been successful. If we click on the run, we are taken to a detailed view of the workflow run where we can see the jobs in that run.

![workflow-run-jobs](/img/04-workflow-run-jobs-view.png)

In the picture above we can see that `first-job` ran successfully in `0s`. If we click on that, we go another level down the chain to see all the steps playing out in the runner as defined in `first-workflow.yml`.

![job-steps](/img/05-job-steps-view.png)

So in the above picture, we can see all the steps defined in `first-job` being run starting with some pre-defined job set up steps where the runner VM is configured followed by the `print-greeting` and `print-goodbye` steps defined in `first-job` before the job is completed and the runner VM is cleaned up and turned off. We can click on the arrows and expand the logs to help with debugging.