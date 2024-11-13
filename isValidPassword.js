function isValidPassword(password) {
    const minLength = 10;
    const hasUpperCase = /[A-Z]/;
    const hasLowerCase = /[a-z]/;
    const hasNumber = /[0-9]/;
    const hasSymbol = /[!@#$%^&*(),.?":{}|<>]/;
  
    if (password.length < minLength) {
      return false;
    }
    if (!hasUpperCase.test(password)) {
      return false;
    }
    if (!hasLowerCase.test(password)) {
      return false;
    }
    if (!hasNumber.test(password)) {
      return false;
    }
    if (!hasSymbol.test(password)) {
      return false;
    }
  
    return true;
}

// Example usage:
console.log(isValidPassword("Password1!")); // true
console.log(isValidPassword("password")); // false
console.log(isValidPassword("Password")); // false (no number or symbol)
console.log(isValidPassword("Password1")); // false (no symbol)
console.log(isValidPassword("password1!")); // false (no uppercase letter)
console.log(isValidPassword("PASSWORD1!")); // false (no lowercase letter)
console.log(isValidPassword("Pass1!")); // false (too short)
console.log(isValidPassword("P@ssword123")); // true
console.log(isValidPassword("1234567890!Aa")); // true
console.log(isValidPassword("!@#$%^&*Aa1")); // true
console.log(isValidPassword("1234567890")); // false (no uppercase, lowercase, or symbol) 