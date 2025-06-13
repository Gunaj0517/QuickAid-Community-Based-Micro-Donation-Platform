// Local mock database
let requests = [];

const form = document.getElementById('requestForm');
const listContainer = document.getElementById('requestsList');

form.addEventListener('submit', function(e) {
  e.preventDefault();

  const newRequest = {
    name: document.getElementById('name').value,
    type: document.getElementById('type').value,
    location: document.getElementById('location').value,
    description: document.getElementById('description').value,
    timestamp: new Date().toLocaleString()
  };

  requests.push(newRequest);
  form.reset();
  displayRequests();
});

function displayRequests() {
  listContainer.innerHTML = '';

  requests.forEach((req, index) => {
    const card = document.createElement('div');
    card.className = 'request-card';
    card.innerHTML = `
      <strong>${req.type}</strong> - <em>${req.location}</em><br>
      ${req.description}<br>
      <small>Requested by: ${req.name} at ${req.timestamp}</small>
    `;
    listContainer.appendChild(card);
  });
}
