function findOddSum(arrOfNumbers) {
  let sum = 0;
  for (let i = 0; i < arrOfNumbers.length; i++) {
    if (arrOfNumbers[i] % 2 != 0) {
      sum += arrOfNumbers[i];
    }
  }
  return sum;
}

const input = [5, 7, 8, 10, 45, 30];
const output = findOddSum(input);
console.log(output);
