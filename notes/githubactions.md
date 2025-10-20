```
GitHub Actions Notes

- Platform to automate dev workflows
- Does CI/CD but also does more like repository tasks
- When something happens in or to your repo, automatic actions are executed in response (events)
- Listen to events, then trigger the workflow
- Most common workflow for your repo is CI/CD (Commit code -> Test -> Build -> Push -> Deploy)
- Set up for the pipeline is pretty easy
- Integration with other tools is important
- Has workflow templates that can be based on project technologies (will automatically create yml file for setup and workflow logic)
- Managed by GitHub (but you can also host your own)
- Whenever you create a new job or workflow for every single job, a fresh new GH server will be prepared to execute all those steps inside the job
- Jobs run in parallel by default, but you can change this if needed
