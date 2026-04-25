const API = "https://SEU-BACKEND";

async function sendPix() {
  const to = document.getElementById("to").value;
  const value = document.getElementById("value").value;

  const res = await fetch(API + "/pix", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      to,
      value: Number(value),
      user: localStorage.getItem("user")
    })
  });

  const data = await res.json();
  alert(data.ok ? "Pix enviado" : data.error);
}