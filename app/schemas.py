from typing import List, Optional
from pydantic import BaseModel


class TaskSchema(BaseModel):
    name: str
    description: Optional[str] = None


class ConditionSchema(BaseModel):
    name: str
    description: Optional[str] = None
    source_task: str
    outcome: str
    target_task_success: str
    target_task_failure: str


class FlowSchema(BaseModel):
    id: str
    name: Optional[str] = None
    start_task: str
    tasks: List[TaskSchema]
    conditions: List[ConditionSchema]


class FlowExecuteRequest(BaseModel):
    flow: FlowSchema


class FlowExecuteResponse(BaseModel):
    flow_id: str
    status: str
    executed_tasks: List[str]
    failed_task: Optional[str] = None
