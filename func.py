
import mlrun
import os
def handler(context,event):
  os.chdir("/opt/nuclio")
  project = mlrun.get_or_create_project("test-workflow-gilad")
  context.logger.info(os.getcwd())
  project.run(workflow_path="workflow.py")





