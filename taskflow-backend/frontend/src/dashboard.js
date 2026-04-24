import React, { useEffect, useState } from "react";
import API from "./api";

function Dashboard() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const fetchTasks = async () => {
      const token = localStorage.getItem("token");

      const res = await API.get("/tasks", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setTasks(res.data);
    };

    fetchTasks();
  }, []);

  const logout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };

  const createTask = async () => {
    const token = localStorage.getItem("token");

    const params = new URLSearchParams();
params.append("title", "New Task");
params.append("description", "Demo task");

await API.post("/tasks", params, {
  headers: {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/x-www-form-urlencoded",
    },
    });
    window.location.reload();
  };

  const deleteTask = async (id) => {
    const token = localStorage.getItem("token");

    await API.delete(`/tasks/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    window.location.reload();
  };

  return (
    <div>
      <h2>Tasks</h2>

      <button onClick={logout}>Logout</button>
      <button onClick={createTask}>Add Task</button>

      {tasks.length === 0 ? (
        <p>No tasks yet</p>
      ) : (
        tasks.map((task) => (
          <div key={task.id}>
            <p>{task.title}</p>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </div>
        ))
      )}
    </div>
  );
}

export default Dashboard;