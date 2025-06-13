async function fetchRequests() {
      const res = await fetch('/get');
      const data = await res.json();
      const list = document.getElementById('requestsList');
      list.innerHTML = '';
      data.forEach(req => {
        list.innerHTML += `
          <div>
            <strong>${req.type}</strong> - ${req.location}<br>
            ${req.description}<br>
            <small>By ${req.name}</small>
            <button onclick="deleteRequest(${req.id})">✅ Solved</button>
          </div><hr>`;
      });
    }

    async function deleteRequest(id) {
      await fetch(`/delete/${id}`, { method: 'DELETE' });
      fetchRequests();
    }

    document.getElementById('requestForm').addEventListener('submit', async (e) => {
      e.preventDefault();
      const form = e.target;
      const data = {
        name: form.name.value,
        type: form.type.value,
        location: form.location.value,
        description: form.description.value
      };
      await fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      form.reset();
      fetchRequests();
    });

    fetchRequests();
  