document.addEventListener("DOMContentLoaded", () => {
    const folderList = document.querySelector(".folder-list");
    const noteList = document.querySelector(".note-list");
    const editor = document.querySelector(".editor");
    const currentFolder = document.querySelector(".current-folder");
    const kanbanColumns = document.querySelectorAll(".kanban-col");

    let folders = JSON.parse(localStorage.getItem("folders")) || [];
    let notes = JSON.parse(localStorage.getItem("notes")) || {};
    let currentFolderIndex = null;

    function renderFolders() {
        folderList.innerHTML = "";
        folders.forEach((folder, index) => {
            let li = document.createElement("li");
            li.textContent = folder;

            let deleteBtn = document.createElement("button");
            deleteBtn.textContent = "🗑";
            deleteBtn.classList.add("delete-btn");
            deleteBtn.onclick = () => deleteFolder(index);

            li.onclick = () => selectFolder(index);
            li.appendChild(deleteBtn);
            folderList.appendChild(li);
        });
    }

    function renderNotes() {
        noteList.innerHTML = "";
        if (currentFolderIndex === null) return;

        let folderNotes = notes[folders[currentFolderIndex]] || [];
        folderNotes.forEach((note, index) => {
            let li = document.createElement("li");
            li.textContent = note.title;

            let deleteBtn = document.createElement("button");
            deleteBtn.textContent = "🗑";
            deleteBtn.classList.add("delete-btn");
            deleteBtn.onclick = (event) => {
                event.stopPropagation();
                deleteNote(index);
            };

            li.onclick = () => loadNote(index);
            li.appendChild(deleteBtn);
            noteList.appendChild(li);
        });
    }

    function selectFolder(index) {
        currentFolderIndex = index;
        currentFolder.textContent = folders[index];
        renderNotes();
    }

    function loadNote(index) {
        let folderNotes = notes[folders[currentFolderIndex]] || [];
        editor.value = folderNotes[index].content;
    }

    function saveNote() {
        if (currentFolderIndex === null) {
            alert("Select a folder first!");
            return;
        }

        let content = editor.value;
        let folderName = folders[currentFolderIndex];

        if (!notes[folderName]) notes[folderName] = [];

        notes[folderName].push({ title: `Note ${notes[folderName].length + 1}`, content });
        localStorage.setItem("notes", JSON.stringify(notes));
        renderNotes();
    }

    function deleteFolder(index) {
        let folderName = folders[index];

        folders.splice(index, 1);
        delete notes[folderName];

        localStorage.setItem("folders", JSON.stringify(folders));
        localStorage.setItem("notes", JSON.stringify(notes));

        currentFolderIndex = null;
        currentFolder.textContent = "Select a folder";
        renderFolders();
        renderNotes();
    }

    function deleteNote(index) {
        let folderName = folders[currentFolderIndex];
        notes[folderName].splice(index, 1);
        localStorage.setItem("notes", JSON.stringify(notes));
        renderNotes();
    }

    function addFolder() {
        let folderName = prompt("Enter folder name:");
        if (folderName) {
            folders.push(folderName);
            localStorage.setItem("folders", JSON.stringify(folders));
            renderFolders();
        }
    }

    document.querySelector(".new-folder-btn").addEventListener("click", addFolder);
    document.querySelector(".new-note-btn").addEventListener("click", saveNote);
    document.querySelector(".save-note-btn").addEventListener("click", saveNote);

    // Kanban Functionality
    document.querySelector(".new-task-btn").addEventListener("click", () => {
        let task = prompt("Enter task:");
        if (task) {
            let taskElement = document.createElement("div");
            taskElement.textContent = task;
            taskElement.draggable = true;
            taskElement.ondragstart = dragStart;

            let deleteBtn = document.createElement("button");
            deleteBtn.textContent = "🗑";
            deleteBtn.classList.add("delete-btn");
            deleteBtn.onclick = () => taskElement.remove();

            taskElement.appendChild(deleteBtn);
            document.querySelector('[data-status="todo"]').appendChild(taskElement);
        }
    });

    function dragStart(event) {
        event.dataTransfer.setData("text", event.target.textContent);
    }

    kanbanColumns.forEach(column => {
        column.ondragover = event => event.preventDefault();
        column.ondrop = event => {
            event.preventDefault();
            let data = event.dataTransfer.getData("text");
            let taskElement = document.createElement("div");
            taskElement.textContent = data;
            taskElement.draggable = true;
            taskElement.ondragstart = dragStart;
            column.appendChild(taskElement);
        };
    });

    renderFolders();
});
