
from repositories.task_repository import TaskRepository



class TaskService(): 
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo
  
    def read_tasks(self, id):
        tasks = self.task_repo.select_task(id)
        return tasks
  
    def create_task(self, user_id, task_description):
        self.task_repo.insert_task(user_id, task_description)
        
    def delete_task(self, task_id):
        self.task_repo.delete_task(task_id)

    def update_task(self, task_description, task_status, task_id):
        self.task_repo.update_task(task_description, task_status, task_id)
        




        