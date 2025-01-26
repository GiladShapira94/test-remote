
import mlrun

def handler(context,event):
  project = mlrun.get_or_create_project("test-workflow-gilad")
  project.run(workflow_path="workflow.py")





