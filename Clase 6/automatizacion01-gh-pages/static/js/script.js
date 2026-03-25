const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('add-btn');
const taskList = document.getElementById('taskList');

addBtn.onclick = function() {
    const taskText = taskInput.value.trim();
    if (taskText === "") return;

    // Crear el elemento de la lista (li)
    const li = document.createElement('li');
    li.innerHTML = `
        <span>${taskText}</span>
        <button class="delete-btn">X</button>
    `;

    //  eliminar tarea
    li.querySelector('.delete-btn').onclick = function() {
        li.remove();
    };
    // Limpiar input
    taskList.appendChild(li);
    taskInput.value = ""; 
};

// Permitir agregar con la tecla Enter
taskInput.onkeypress = function(e) {
    if (e.key === 'Enter') addBtn.click();
};