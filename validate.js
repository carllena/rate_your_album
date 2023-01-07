var loginBtn = document.getElementById("loginBtn");

var passwordLvl = 0;

function empty() {
  var login = document.forms["signup"]["login"].value;
  var password = document.forms["signup"]["password"].value;
  var confirmPassword = document.forms["signup"]["confirmPassword"].value;
  var firstname = document.forms["signup"]["name"].value;
  var lastname = document.forms["signup"]["lastname"].value;
  if (
    passwordLvl < 4 ||
    password != confirmPassword ||
    !login ||
    !password ||
    !confirmPassword ||
    !firstname ||
    !lastname
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

var nameInput = document.getElementById("name");
var lastnameInput = document.getElementById("lastname");

nameInput.onkeyup = function () {
  var letters = /^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+$/;
  if (!nameInput.value.match(letters)) {
    document.getElementById("nameValidate").style.display = "block";
  } else {
    document.getElementById("nameValidate").style.display = "none";
  }
};

lastnameInput.onkeyup = function () {
  var letters = /^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+$/;
  if (!lastnameInput.value.match(letters)) {
    document.getElementById("lastnameValidate").style.display = "block";
  } else {
    document.getElementById("lastnameValidate").style.display = "none";
  }
};

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
    passwordLvl++;
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
    passwordLvl--;
  }

  var upperCaseLetters = /[A-Z]/g;
  if (password.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
    passwordLvl++;
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
    passwordLvl--;
  }

  var numbers = /[0-9]/g;
  if (passwordInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
    passwordLvl++;
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
    passwordLvl--;
  }

  if (passwordInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
    passwordLvl++;
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
    passwordLvl--;
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
passwordInput.onkeyup = function () {
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
