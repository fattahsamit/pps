function secondLargest(numbers) {
  let high2 = 0;
  numbers.sort();
  //   let high = 0;
  //   for (let i = 0; i < numbers.length; i++) {
  //     if (numbers[i] > high) {
  //       high += numbers[i];
  //     }
  //   }
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] == numbers[numbers.length - 1]) {
      continue;
    } else if (numbers[i] > high2) {
      high2 = numbers[i];
    }
  }
  return high2;
}

const numbers = [10, 33, 5, 99, 6];
const largest2 = secondLargest(numbers);
console.log(largest2);
