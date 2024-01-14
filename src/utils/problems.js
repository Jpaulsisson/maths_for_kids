// This file will hold all the functions necessary to create random math problems for kids to solve
// This will produce random values for the problems
function digitHelper(digits) {
  const digitStringArray = ['1']
  let i = 1;
  while (i <= digits) {
    digitStringArray.push('0');
    i++
  }
  const num = Number(digitStringArray.join(''))
  const random = Math.floor(Math.random() * num)

  const x = String(random).length < digitStringArray.length - 1 ? num - random : random

  return x;
}

// Max digits: 6, Differing digits possible, Decimals TBD
function generateAdditionProblem(digits, secondDigits = null, decimalPlaces = null) {
  const x = digitHelper(digits);
  const y = secondDigits === null ? digitHelper(digits) : digitHelper(secondDigits);

  return {
    x,
    y,
    solution: x + y,
  }
}

// Max digits: 6, Differing digits possible, Decimals TBD
function generateSubtractionProblem(digits, secondDigits = null, decimalPlaces = null) {
  const x = digitHelper(digits);
  const y = secondDigits === null ? digitHelper(digits) : digitHelper(secondDigits);

  return {
    x,
    y,
    solution: x - y,
  }
}

// Max digits: 6, Differing digits possible, Decimals TBD
function generateMultiplicationProblem(digits, secondDigits = null, decimalPlaces = null) {
  const x = digitHelper(digits);
  const y = secondDigits === null ? digitHelper(digits) : digitHelper(secondDigits);

  return {
    x,
    y,
    solution: x * y,
  }
}

// Max digits: 6, Differing digits possible, Decimals TBD
function generateDivisionProblem(digits, secondDigits = null, decimalPlaces = null) {
  const x = digitHelper(digits);
  const y = secondDigits === null ? digitHelper(digits) : digitHelper(secondDigits);

  return {
    x,
    y,
    solution: x / y,
  }
}

// Max digits: 2, Max power: 10
function generateExponentProblem(digits, power) {
  let range;
  switch (digits) {
    case 1:
      range = 10;
      break;
    case 2:
      range = 100;
      break;
  }

  const randomX = Math.floor(Math.random() * range)

  return {
    x: randomX,
    power: power,
    solution: randomX ** power,
  }
} 
