
# 📘 Flow Manager – Python Backend Service

## Overview 

This project is a **Flow Manager** — a system that runs a series of steps (called *tasks*) **one after another**, making decisions at each step about what should happen next.

Think of it like this:

> “Do Step 1 → if it succeeds, do Step 2 → if that succeeds, do Step 3 → otherwise stop.”

The flow (steps and decisions) is **not hard-coded**.
Instead, it is **defined using a JSON configuration**, which makes the system flexible and reusable.

This service exposes an **API** that:

* Accepts a flow definition
* Executes tasks sequentially
* Evaluates conditions after each task
* Returns the execution result

---

## Why This Project Exists

This project demonstrates:

* Backend system design
* Flow orchestration
* Clean architecture
* Separation of concerns
* API-driven execution

It is intentionally kept **simple**, **generic**, and **easy to understand**, focusing on *design clarity* rather than complex business logic.

---

## High-Level Flow (Concept)

1. A client sends a **flow definition** (JSON) to the API
2. The system starts from the **start task**
3. Each task runs and returns **success or failure**
4. A condition decides:

   * Which task runs next, or
   * Whether the flow should stop
5. The API returns a summary of execution

---

## Example Flow (Human Explanation)

Example flow:

1. Fetch data
2. Process data
3. Store data

Rules:

* If fetching fails → stop
* If processing fails → stop
* Only store data if everything succeeds

---

## Project Structure

```
flow-manager-python/
├── app/
│   ├── main.py
│   ├── api.py
│   ├── engine.py
│   ├── models.py
│   ├── schemas.py
│   └── tasks.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## File-by-File Explanation (Very Important)

### `main.py`

**Purpose:** Application entry point

* Creates the FastAPI application
* Registers API routes
* Provides a `/health` endpoint

Why it matters:

* Confirms the service is running
* Acts as the startup point for the application

---

### `api.py`

**Purpose:** API layer (request → response)

Responsibilities:

* Accept flow definitions from the client
* Convert input data into internal models
* Call the flow engine
* Return execution results

Why it matters:

* Keeps business logic out of the API
* Clean separation between API and core logic

---

### `schemas.py`

**Purpose:** Input & output validation

Defines:

* How the request JSON should look
* How the response JSON should look

Why it matters:

* Prevents invalid input
* Enables automatic API documentation (Swagger)
* Makes the API self-describing

---

### `models.py`

**Purpose:** Core domain models

Contains:

* `Task`
* `TaskResult`
* `Condition`
* `Flow`

Why it matters:

* Pure business logic
* Independent of FastAPI
* Easy to test and extend

---

### `tasks.py`

**Purpose:** Task implementations

Includes example tasks:

* Fetch data
* Process data
* Store data

Why it matters:

* Demonstrates how tasks can be plugged into the system
* Tasks are independent and reusable
* Business logic can be replaced without changing the engine

---

### `engine.py`

**Purpose:** Flow execution engine (core brain)

Responsibilities:

* Executes tasks sequentially
* Evaluates conditions
* Tracks executed tasks
* Stops on failure or completion

Why it matters:

* This is the heart of the system
* Implements condition-based flow control
* Generic and extensible

---

## API Usage

### Start the Server

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

### Health Check

```
GET /health
```

Response:

```json
{ "status": "ok" }
```

---

### Execute a Flow

```
POST /flow/execute
```

#### Example Request

```json
{
  "flow": {
    "id": "flow123",
    "name": "Data processing flow",
    "start_task": "task1",
    "tasks": [
      { "name": "task1", "description": "Fetch data" },
      { "name": "task2", "description": "Process data" },
      { "name": "task3", "description": "Store data" }
    ],
    "conditions": [
      {
        "name": "condition_task1",
        "source_task": "task1",
        "outcome": "success",
        "target_task_success": "task2",
        "target_task_failure": "end"
      },
      {
        "name": "condition_task2",
        "source_task": "task2",
        "outcome": "success",
        "target_task_success": "task3",
        "target_task_failure": "end"
      }
    ]
  }
}
```

---

### Example Response (Success)

```json
{
  "flow_id": "flow123",
  "status": "completed",
  "executed_tasks": ["task1", "task2", "task3"],
  "failed_task": null
}
```

---

### Example Response (Failure)

```json
{
  "flow_id": "flow123",
  "status": "failed",
  "executed_tasks": ["task2"],
  "failed_task": "task2"
}
```

---

## Design Principles Used

* Separation of concerns
* Configuration-driven execution
* Fail-fast behavior
* Clean and readable code
* Extensible architecture

---

## Notes

* No database is used (intentionally)
* Tasks are mock implementations
* Focus is on **flow orchestration**, not data storage
* Easy to extend with new tasks or conditions

---

## Final Words

This project demonstrates how to design and implement a **generic, API-driven flow orchestration system** using clean backend engineering practices.


