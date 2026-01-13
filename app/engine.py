from typing import Dict, Optional
from app.models import Flow, TaskResult


class FlowEngine:
    """
    Core engine responsible for executing a flow.
    """

    def execute(self, flow: Flow) -> Dict:
        current_task_name = flow.start_task
        input_data: Optional[dict] = None

        while current_task_name != "end":
            task = flow.tasks.get(current_task_name)

            if not task:
                return {
                    "flow_id": flow.flow_id,
                    "status": "failed",
                    "executed_tasks": flow.executed_tasks,
                    "failed_task": current_task_name,
                }

            # Execute task
            result: TaskResult = task.execute(input_data)
            flow.executed_tasks.append(current_task_name)

            if not result.success:
                return {
                    "flow_id": flow.flow_id,
                    "status": "failed",
                    "executed_tasks": flow.executed_tasks,
                    "failed_task": current_task_name,
                }

            # Prepare data for next task---->
            input_data = result.data

            # Find condition for current task
            condition = flow.conditions.get(current_task_name)
            if not condition:
                return {
                    "flow_id": flow.flow_id,
                    "status": "completed",
                    "executed_tasks": flow.executed_tasks,
                    "failed_task": None,
                }

            # Decide next task
            current_task_name = condition.evaluate(result)

        return {
            "flow_id": flow.flow_id,
            "status": "completed",
            "executed_tasks": flow.executed_tasks,
            "failed_task": None,
        }
