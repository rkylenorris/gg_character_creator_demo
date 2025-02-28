async function updateDescription(type, element) {
    const id = element.value;
    if (!id) {
        document.getElementById(`${type}_desc`).innerText = "";
        return;
    }

    const response = await fetch("/get_description", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ type: type, id: id })
    });

    const data = await response.json();
    document.getElementById(`${type}_desc`).innerText = data.description || "Description not found.";
}