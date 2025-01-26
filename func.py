
import mlrun
import os
os.chdir("/opt/nuclio/")
def handler(context,event):
  project = mlrun.get_or_create_project("test-workflow-gilad")
  context.logger.info(os.getcwd())
  project.run(workflow_path="workflow.py")





