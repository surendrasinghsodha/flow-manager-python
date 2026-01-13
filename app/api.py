from fastapi import APIRouter
from app.schemas import FlowExecuteRequest, FlowExecuteResponse
from app.models import Flow, Task, Condition
from app.engine import FlowEngine
from app.tasks import FetchDataTask, ProcessDataTask, StoreDataTask

router = APIRouter()


def build_tasks(task_definitions):
    """
    Map task names to concrete task implementations.
    """
    task_registry = {}

    for task in task_definitions:
        if task.name == "task1":
            task_registry[task.name] = FetchDataTask(task.name, task.description)
        elif task.name == "task2":
            task_registry[task.name] = ProcessDataTask(task.name, task.description)
        elif task.name == "task3":
            task_registry[task.name] = StoreDataTask(task.name, task.description)
        else:
            # Unknown task → generic task (fails)
            task_registry[task.name] = Task(task.name, task.description)

    return task_registry


def build_conditions(condition_definitions):
    """
    Build condition registry keyed by source task name.
    """
    condition_registry = {}

    for condition in condition_definitions:
        condition_registry[condition.source_task] = Condition(
            source_task=condition.source_task,
            target_task_success=condition.target_task_success,
            target_task_failure=condition.target_task_failure,
        )

    return condition_registry


@router.post("/flow/execute", response_model=FlowExecuteResponse)
def execute_flow(request: FlowExecuteRequest):
    """
    Execute a flow based on the provided flow definition.
    """
    # Build tasks and conditions
    tasks = build_tasks(request.flow.tasks)
    conditions = build_conditions(request.flow.conditions)

    # Create Flow object
    flow = Flow(
        flow_id=request.flow.id,
        start_task=request.flow.start_task,
        tasks=tasks,
        conditions=conditions,
    )

    # Execute flow
    engine = FlowEngine()
    result = engine.execute(flow)

    return FlowExecuteResponse(**result)
