var registerBtn = document.getElementById("registerBtn");
var loginInput = document.getElementById("login");
var loginAvail = document.getElementById("loginAvailability");

loginInput.onblur = function () {
  document.getElementById("loginAvailability").style.display = "none";
};

loginInput.onkeyup = async function () {
  document.getElementById("loginAvailability").style.display = "block";

  if (loginInput.value.length > 4) {
    var loginDict = {
      login: loginInput.value,
    };
    loginDict = JSON.stringify(loginDict);
    const response = await fetch("http://192.168.0.220:5123/free_login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
      },
      body: loginDict,
    });
    response.json().then((data) => {
      console.log(data.status_code);
      if (data.status_code == 400) {
        document.getElementById("availability").classList.remove("valid");
        document.getElementById("availability").classList.add("invalid");
        document.getElementById("availability").innerHTML =
          data.results.response;
      } else {
        document.getElementById("availability").classList.remove("invalid");
        document.getElementById("availability").classList.add("valid");
        document.getElementById("availability").innerHTML =
          data.results.response;
      }
    });
  } else {
    document.getElementById("availability").innerHTML = "Login is too short";
    document.getElementById("availability").classList.remove("valid");
    document.getElementById("availability").classList.add("invalid");
  }
};

var passwordLvl = 0;
var rightName = 0;

// Jak ktoś ma w imieniu 6 to i tak może przesłać dane. xD

function empty() {
  var login = document.forms["signup"]["login"].value;
  var password = document.forms["signup"]["password"].value;
  var confirmPassword = document.forms["signup"]["confirmPassword"].value;
  var firstname = document.forms["signup"]["name"].value;
  var lastname = document.forms["signup"]["lastname"].value;
  console.log(passwordLvl);
  if (
    passwordLvl < 4 ||
    rightName < 2 ||
    password != confirmPassword ||
    !login ||
    !password ||
    !confirmPassword ||
    !firstname ||
    !lastname
  ) {
    document.getElementById("registerBtn").disabled = true;
  } else {
    document.getElementById("registerBtn").disabled = false;
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

function validateName() {
  rightName = 0;
  var letters = /^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+$/;
  if (nameInput.value.match(letters)) {
    document.getElementById("nameValidate").style.display = "none";
    rightName++;
  } else {
    document.getElementById("nameValidate").style.display = "block";
  }
  if (lastnameInput.value.match(letters)) {
    document.getElementById("lastnameValidate").style.display = "none";
    rightName++;
  } else {
    document.getElementById("lastnameValidate").style.display = "block";
  }
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
  passwordLvl = 0;
  var lowerCaseLetters = /[a-z]/g;
  if (passwordInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
    passwordLvl++;
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }

  var upperCaseLetters = /[A-Z]/g;
  if (password.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
    passwordLvl++;
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  var numbers = /[0-9]/g;
  if (passwordInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
    passwordLvl++;
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  if (passwordInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
    passwordLvl++;
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }

  if (passwordCheck.value == passwordInput.value) {
    document.getElementById("yes").style.display = "block";
    document.getElementById("no").style.display = "none";
  } else {
    document.getElementById("yes").style.display = "none";
    document.getElementById("no").style.display = "block";
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
// passwordInput.onkeyup = function () {
//   if (passwordCheck.value == passwordInput.value) {
//     document.getElementById("yes").style.display = "block";
//     document.getElementById("no").style.display = "none";
//   } else {
//     document.getElementById("yes").style.display = "none";
//     document.getElementById("no").style.display = "block";
//   }
// };

passwordCheck.onfocus = function () {
  document.getElementById("secondValidate").style.display = "block";
};

passwordCheck.onblur = function () {
  document.getElementById("secondValidate").style.display = "none";
};
