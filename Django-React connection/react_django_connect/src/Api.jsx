import React, {useEffect,useState} from "react";

function TaskList() {
    const[tasks,setTasks] = useState([])


    useEffect(() =>{
        fetch('http://127.0.0.1:8000/tasks/')
        .then((response) => response.json())
        .then((data) => setTasks(data));
    },[]);

    return (
        <div>
            <h1>Task List</h1>
            <ul>
                {tasks.map((task) =>
                <li key={task.id}>
                    {task.task_name} - {task.completed ? 'Completed' : 'Pending'}
                </li>
                )}
            </ul>
        </div>
    )

}

export default TaskList;