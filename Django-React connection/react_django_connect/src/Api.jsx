import React, {useEffect,useState} from "react";

function TaskList() {
    const[tasks,setTasks] = useState([])


    useEffect(() =>{
        fetch('')
        .then((response) => response.json)
        .then((data) => setTasks(data));
    },[]);

    return (
        <div>
            <h1>Task List</h1>
            <ul>
                {tasks.map((task) =>
                <li key={task.id}>
                    {task.name} - {task.completed ? 'Completed' : 'Pending'}
                </li>
                )}
            </ul>
        </div>
    )

}

export default TaskList;