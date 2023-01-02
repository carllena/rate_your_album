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

var myInput = document.getElementById("psw");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user clicks on the password field, show the message box
myInput.onfocus = function () {
  document.getElementById("message").style.display = "block";
};

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function () {
  document.getElementById("message").style.display = "none";
};

// When the user starts to type something inside the password field
myInput.onkeyup = function () {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if (myInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }

  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if (myInput.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if (myInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  // Validate length
  if (myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
};
