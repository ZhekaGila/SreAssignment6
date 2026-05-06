const BASE = "http://zhandos.website";

function show(data) {
  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}

async function login() {
  const res = await fetch(`${BASE}:8003/login`, {
    method: "POST"
  });
  show(await res.json());
}

async function authorize() {
  const res = await fetch(`${BASE}:8003/authorize`);
  show(await res.json());
}

async function getProducts() {
  const res = await fetch(`${BASE}:8001/products`);
  show(await res.json());
}

async function createOrder() {
  const res = await fetch(`${BASE}:8002/orders`, {
    method: "POST"
  });
  show(await res.json());
}

async function checkOrderHealth() {
  const res = await fetch(`${BASE}:8002/health`);
  show(await res.json());
}

async function getUsers() {
  const res = await fetch(`${BASE}:8004/users`);
  show(await res.json());
}

async function sendMessage() {
  const user = document.getElementById("chatUser").value;
  const text = document.getElementById("chatText").value;

  const res = await fetch(`${BASE}:8005/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ user, text })
  });

  show(await res.json());
}

async function getMessages() {
  const res = await fetch(`${BASE}:8005/messages`);
  show(await res.json());
}
