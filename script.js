function processCreatingAccount() {
  var loginInput = document.getElementById("login").value;
  var passwordInput = document.getElementById("password").value;
  var nameInput = document.getElementById("name").value;
  var surnameInput = document.getElementById("lastname").value;
  var userAgent = navigator.userAgent;
  var currentTimestamp = Date.now();
  var fingerprintHash = CryptoJS.MD5(
    loginInput + "," + userAgent + "," + currentTimestamp
  ).toString();
  var responseJson = createAccount(
    "http://192.168.0.221:5123/create_account",
    loginInput,
    passwordInput,
    nameInput,
    surnameInput,
    userAgent,
    currentTimestamp,
    fingerprintHash
  );

  responseJson.then((data) => {
    if (data.status_code == 200) {
      alert(data.results.response);
      window.location.href = "signin.html";
    } else {
      document.getElementById("signup").reset();
    }
  });
}

async function createAccount(
  endpoint,
  loginInput,
  passwordInput,
  nameInput,
  surnameInput,
  userAgent,
  currentTimestamp,
  fingerprintHash
) {
  var user = {
    login: loginInput,
    password: passwordInput,
    name: nameInput,
    surname: surnameInput,
    timestamp: currentTimestamp,
    fingerprint: fingerprintHash,
  };
  user = JSON.stringify(user);
  const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "User-Agent": userAgent,
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
    },
    body: user,
  });
  return response.json();
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
