from typing import Optional
from app.models import Task, TaskResult


class FetchDataTask(Task):
    """
    Task 1: Fetch data (mock implementation).
    """

    def execute(self, input_data: Optional[dict] = None) -> TaskResult:
        # Mock fetching data
        data = {"value": 100}
        return TaskResult(success=True, data=data)


class ProcessDataTask(Task):
    """
    Task 2: Process data (mock implementation).
    """

    def execute(self, input_data: Optional[dict] = None) -> TaskResult:
        if not input_data:
            return TaskResult(success=False, error="No input data provided")

        # Mock processing
        processed_value = input_data["value"] * 2
        return TaskResult(success=True, data={"processed_value": processed_value})


class StoreDataTask(Task):
    """
    Task 3: Store data (mock implementation).
    """

    def execute(self, input_data: Optional[dict] = None) -> TaskResult:
        if not input_data:
            return TaskResult(success=False, error="No data to store")

        # Mock storing data (no DB)
        print(f"Storing data: {input_data}")
        return TaskResult(success=True)
