import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from models import Task, CreateTask


app = FastAPI()


tasks = list()


@app.get('/', response_class=HTMLResponse)
def welcome():
    return """
        <html>
        <body>
            <h1>Помощь по API</h1>
            <p>Запросы для проверки</p>
            <div>
                <ul>
                    <a>Список задач</a>
                    <li>curl -X 'GET' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json'</li>
                    <a>Получение задачи из списка по ID</a>
                    <li>curl -X 'GET' 'http://127.0.0.1:8000/tasks/1' -H 'accept: application/json'</li>
                    <a>Создание задачи</a>
                    <li>curl -X 'POST' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json' -H 'Content-Type: application/json' \
                        -d '{
                        "name": "string",
                        "completed": false,
                        "definition": "string"
                        }'
                    </li>
                    <a>Редактирование задачи по заданому ID</a>
                    <li>curl -X 'PUT' \
                        'http://127.0.0.1:8000/tasks/1' \
                        -H 'accept: application/json' \
                        -H 'Content-Type: application/json' \
                        -d '{
                        "name": "string",
                        "completed": false,
                        "definition": "string"
                        }'
                    </li>
                    <a>Удаление задачи</a>
                    <li>curl -X 'DELETE' 'http://127.0.0.1:8000/tasks/1' -H 'accept: application/json'</li>
                </ul
            </div>
        </body>
        </html>
        """


@app.get('/tasks/', response_model=list[Task])
async def get_task_list():
    return tasks


@app.get('/tasks/{id}', response_model=Task)
async def get_task_id(id: int):
    task = next((task for task in tasks if task['id'] == id), None)
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return task
    

@app.post('/tasks/', response_model=Task)
async def create_task(task: CreateTask):
    new_task = { 'id': len(tasks) + 1, **task.model_dump()}
    tasks.append(new_task)
    return new_task
    

@app.put('/tasks/{id}', response_model=Task)
async def update_task(id: int, update_task: CreateTask):
    task = next((task for task in tasks if task['id'] == id), None)
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    task.update(update_task.model_dump())
    return task


@app.delete('/tasks/{id}', response_model=dict)
async def del_task(id: int):
    global tasks
    task = next((task for task in tasks if task['id'] == id ), None)
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    tasks = [task for task in tasks if task['id'] != id]
    return {'msg': 'Task deleted'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)