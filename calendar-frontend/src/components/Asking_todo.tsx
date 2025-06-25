import "./asking_todo.css";

function AskingTodo() {
  function handleSubmit() {
    const taskInput = document.getElementById("task") as HTMLInputElement;
    const taskValue = taskInput.value.trim();
    if (taskValue) {
      console.log(taskValue);
      const ul = document.getElementById("task-list") as HTMLInputElement;
      const newTask = document.createElement("li");
      newTask.textContent = taskValue;
      ul.appendChild(newTask);
      cleanInput();
    }
  }

  const cleanInput = () => {
    const taskInput = document.getElementById("task") as HTMLInputElement;
    taskInput.value = "";
  };

  return (
    <div className="container">
      <div className="asking-container">
        <div className="add-todo">
          <input type="text" id="task" placeholder="Add a new task" />
        </div>
        <div className="submit-button">
          <button onClick={handleSubmit}>Submit</button>
        </div>
      </div>
      <div className="todo-list">
        <ul id="task-list"></ul>
      </div>
    </div>
  );
}
export default AskingTodo;
