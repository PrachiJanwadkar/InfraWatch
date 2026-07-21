async function updateDashboard() {
    const response = await fetch("/api/system");
    const data = await response.json();

    // CPU
    document.getElementById("cpu-value").innerText = data.cpu + " %";
    document.getElementById("cpu-bar").value = data.cpu;

    // Memory
    document.getElementById("memory-value").innerText = data.memory + " %";
    document.getElementById("memory-bar").value = data.memory;

    // Disk
    document.getElementById("disk-value").innerText = data.disk + " %";
    document.getElementById("disk-bar").value = data.disk;

   // Process Table
const table = document.getElementById("process-table");

table.innerHTML = "";

data.processes.forEach(process => {
    table.innerHTML += `
        <tr>
            <td>${process.pid}</td>
            <td>${process.name}</td>
            <td>${process.cpu_percent}</td>
            <td>${(process.memory_percent ?? 0).toFixed(2)}</td>
            <td>${process.status}</td>
        </tr>
    `;
});

    // CPU Alert
    const cpuCard = document.getElementById("cpu-card");

    cpuCard.classList.remove("normal", "warning", "critical");

    if (data.cpu > 80)
        cpuCard.classList.add("critical");
    else if (data.cpu > 60)
        cpuCard.classList.add("warning");
    else
        cpuCard.classList.add("normal");
}

// Update every 2 seconds
setInterval(updateDashboard, 2000);