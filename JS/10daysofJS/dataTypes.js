function performOperation(secondInteger, secondDecimal, secondString) {
  // Declare a variable named 'firstInteger' and initialize with integer value 4.
  const firstInteger = 4;
  let sumInteger = firstInteger + secondInteger;
  console.log(sumInteger);

  // Declare a variable named 'firstDecimal' and initialize with floating-point value 4.0.
  const firstDecimal = 4.0;
  let sumDecimal = firstDecimal + secondDecimal;
  console.log(sumDecimal);

  // Declare a variable named 'firstString' and initialize with the string "HackerRank".
  const firstString = "HackerRank ";
  let sumString = firstString + secondString;
  console.log(sumString);
}

let secondInteger = 12;
let secondDecimal = 4.32;
let secondString = "is the best place to learn and practice coding!";
performOperation(secondInteger, secondDecimal, secondString);
