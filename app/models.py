from typing import Dict, List, Optional


class TaskResult:
    """
    Represents the result of a task execution.
    """

    def __init__(
        self,
        success: bool,
        data: Optional[dict] = None,
        error: Optional[str] = None,
    ):
        self.success = success
        self.data = data
        self.error = error


class Task:
    """
    Represents a task in the flow.
    """

    def __init__(self, name: str, description: Optional[str] = None):
        self.name = name
        self.description = description

    def execute(self, input_data: Optional[dict] = None) -> TaskResult:
        """
        Execute the task.
        Must be overridden by concrete task implementations.
        """
        raise NotImplementedError("Task execution not implemented")


class Condition:
    """
    Represents a condition that determines the next task
    based on the result of a source task.
    """

    def __init__(
        self,
        source_task: str,
        target_task_success: str,
        target_task_failure: str,
    ):
        self.source_task = source_task
        self.target_task_success = target_task_success
        self.target_task_failure = target_task_failure

    def evaluate(self, task_result: TaskResult) -> str:
        """
        Decide the next task based on task result.
        """
        if task_result.success:
            return self.target_task_success
        return self.target_task_failure


class Flow:
    """
    Represents a flow definition and its execution state.
    """

    def __init__(
        self,
        flow_id: str,
        start_task: str,
        tasks: Dict[str, Task],
        conditions: Dict[str, Condition],
    ):
        self.flow_id = flow_id
        self.start_task = start_task
        self.tasks = tasks
        self.conditions = conditions
        self.executed_tasks: List[str] = []
