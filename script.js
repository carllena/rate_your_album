function processCreatingAccount() {
  var loginInput = document.getElementById("login").value;
  var passwordInput = document.getElementById("password").value;
  var nameInput = document.getElementById("name").value;
  var surnameInput = document.getElementById("lastname").value;
  // przyjąć wartość kodu z funkcji createAccount np. let responseCode
  var responseJson = createAccount(
    "http://192.168.0.220:5123/create_account",
    loginInput,
    passwordInput,
    nameInput,
    surnameInput
  );

  responseJson.then((data) => {
    if (data.status_code == 200) {
      alert(data.results.response);
    } else {
      document.getElementById("signup").reset();
    }
  });
  //if responseCode coś tam to przekierowanie na stronę logowania
  //w przeciwnym razie czy jest potrzeba coś robić? może tylko reset formularza
}

async function createAccount(
  endpoint,
  loginInput,
  passwordInput,
  nameInput,
  surnameInput
) {
  var user = {
    // login: document.getElementById("login").value,
    // password: document.getElementById("password").value,
    // name: document.getElementById("name").value,
    // surname: document.getElementById("surname").value,
    login: loginInput,
    password: passwordInput,
    name: nameInput,
    surname: surnameInput,
  };
  user = JSON.stringify(user);
  const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
    },
    body: user,
  });
  return response.json();
  // response.json().then((data) => {
  //   var statusCode = data.status_code;
  //   var responseText = data.results.response;
  // });
  // return { statusCode, responseText };
  //return code od serwera
}

// function httpGet() {
//   var xmlHttp = new XMLHttpRequest();
//   xmlHttp.open("GET", "http://192.168.0.220:5123/health", false); // false for synchronous request
//   xmlHttp.setRequestHeader("Access-Control-Allow-Origin", "*");
//   xmlHttp.setRequestHeader("Access-Control-Allow-Headers", "*");
//   xmlHttp.setRequestHeader("Accept", "text/plain");
//   xmlHttp.setRequestHeader("Content-Type", "text/plain");
//   xmlHttp.send(null);
//   // return xmlHttp.responseText;
//   console.log(xmlHttp.responseText);
// }
