var loginBtn = document.getElementById("loginBtn");

function empty() {
  var login = document.forms["signup"]["login"].value;
  var password = document.forms["signup"]["password"].value;
  var confirmPassword = document.forms["signup"]["confirmPassword"].value;
  var firstname = document.forms["signup"]["name"].value;
  var surname = document.forms["signup"]["surname"].value;
  if (
    login == "" ||
    login == null ||
    password == "" ||
    password == null ||
    confirmPassword == "" ||
    confirmPassword == null ||
    firstname == "" ||
    firstname == null ||
    surname == "" ||
    surname == null
  ) {
    document.getElementById("loginBtn").disabled = true;
  } else {
    document.getElementById("loginBtn").disabled = false;
  }
}

function showPsw() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
