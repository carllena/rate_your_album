async function sendDataToCreateAccount() {
  var user = {
    login: document.getElementById("login").value,
    password: document.getElementById("password").value,
    name: document.getElementById("name").value,
    surname: document.getElementById("surname").value,
  };
  user = JSON.stringify(user);
  const response = await fetch("http://192.168.0.220:5123/create_account", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
    },
    body: user,
  });
  response.json().then((data) => {
    console.log(data);
  });
}

function httpGet() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", "http://192.168.0.220:5123/health", false); // false for synchronous request
  xmlHttp.setRequestHeader("Access-Control-Allow-Origin", "*");
  xmlHttp.setRequestHeader("Access-Control-Allow-Headers", "*");
  xmlHttp.setRequestHeader("Accept", "text/plain");
  xmlHttp.setRequestHeader("Content-Type", "text/plain");
  xmlHttp.send(null);
  // return xmlHttp.responseText;
  console.log(xmlHttp.responseText);
}
