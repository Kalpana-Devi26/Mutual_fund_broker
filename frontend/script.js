const API_BASE = "http://localhost:8000";

async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();
  if (res.status === 200) {
    localStorage.setItem("token", data.access_token);
    window.location.href = "portfolio.html";
  } else {
    document.getElementById("error").innerText = data.detail || "Login failed";
  }
}

async function getPortfolio() {
  const token = localStorage.getItem("token");

  const res = await fetch(`${API_BASE}/portfolio`, {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });

  const data = await res.json();
  const list = document.getElementById("portfolio-list");
  data.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.fund_name} - Invested: ₹${item.amount_invested} | Current: ₹${item.current_value}`;
    list.appendChild(li);
  });
}
