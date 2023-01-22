async function signIn(endpoint, loginInput, passwordInput, userAgent) {
  var user = {
    login: loginInput,
    password: passwordInput,
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

function processLoginUser() {
  var loginInput = document.getElementById("login").value;
  var passwordInput = document.getElementById("logPassword").value;
  var userAgent = navigator.userAgent;
  // var currentTimestamp = Date.now();
  // var fingerprintHash = CryptoJS.MD5(
  //   loginInput + "," + userAgent + "," + currentTimestamp
  // ).toString();
  var responseJson = signIn(
    "http://192.168.0.221:5123/auth",
    loginInput,
    passwordInput,
    userAgent
    // currentTimestamp,
    // fingerprintHash
  );

  responseJson.then((data) => {
    if (data.status_code == 200) {
      alert(data.results.response);
      window.location.href = "usermenu.html";
    } else {
      document.getElementById("passwordCompatibility").style.display = "block";
    }
  });
}
