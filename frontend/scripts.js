

function show(data) {
  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}

async function login() {
  const res = await fetch("/api/auth/login", {
    method: "POST"
  });
  show(await res.json());
}

async function authorize() {
  const res = await fetch("/api/auth/authorize");
  show(await res.json());
}

async function getProducts() {
  const res = await fetch("/api/products/products");
  show(await res.json());
}

async function createOrder() {
  const res = await fetch("/api/orders/orders", {
    method: "POST"
  });
  show(await res.json());
}

async function checkOrderHealth() {
  const res = await fetch("/api/orders/health");
  show(await res.json());
}

async function getUsers() {
  const res = await fetch("/api/users/users");
  show(await res.json());
}

async function sendMessage() {
  const user = document.getElementById("chatUser").value;
  const text = document.getElementById("chatText").value;

  const res = await fetch("/api/chat/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ user, text })
  });

  show(await res.json());
}

async function getMessages() {
  const res = await fetch("/api/chat/messages");
  show(await res.json());
}
