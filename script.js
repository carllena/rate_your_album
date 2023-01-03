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

var passwordInput = document.getElementById("password");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

passwordInput.onfocus = function () {
  document.getElementById("firstValidate").style.display = "block";
};

passwordInput.onblur = function () {
  document.getElementById("firstValidate").style.display = "none";
};

passwordInput.onkeyup = function () {
  var lowerCaseLetters = /[a-z]/g;
  if (passwordInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }

  var upperCaseLetters = /[A-Z]/g;
  if (password.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  var numbers = /[0-9]/g;
  if (passwordInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  if (passwordInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
};

// Confirm password validate
var passwordCheck = document.getElementById("confirmPassword");
passwordCheck.onkeyup = function () {
  if (passwordCheck.value == passwordInput.value) {
    document.getElementById("yes").style.display = "block";
    document.getElementById("no").style.display = "none";
  } else {
    document.getElementById("yes").style.display = "none";
    document.getElementById("no").style.display = "block";
  }
};

passwordCheck.onfocus = function () {
  document.getElementById("secondValidate").style.display = "block";
};

passwordCheck.onblur = function () {
  document.getElementById("secondValidate").style.display = "none";
};

var loginBtn = document.getElementById("loginBtn");

var login = document.forms["signup"]["login"];

login.onblur = function allFilled() {
  var login_value = document.forms["signup"]["login"].value;
  // var password = document.forms["signup"]["password"].value;
  // var confirmPassword = document.forms["signup"]["confirmPassword"].value;
  // var name = document.forms["signup"]["name"].value;
  // var surname = document.forms["signup"]["surname"].value;
  if (
    login_value == "" // ||
    // password == "" ||
    // confirmPassword == "" ||
    // name == "" ||
    // surname == ""
  ) {
    document.getElementById("loginBtn").disabled = true;
  } else {
    document.getElementById("loginBtn").disabled = false;
  }
};
