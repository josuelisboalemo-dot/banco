async function login() {
  const user = document.getElementById("user").value;
  const pass = document.getElementById("pass").value;

  const res = await fetch("https://SEU-BACKEND/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({username: user, password: pass})
  });

  const data = await res.json();

  if (data.ok) {
    localStorage.setItem("user", user);
    window.location.href = "dashboard.html";
  } else {
    alert("Login inválido");
  }
}