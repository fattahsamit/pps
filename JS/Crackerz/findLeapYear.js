function findLeapYear(arrOfYears) {
  let leap = [];
  for (let i = 0; i < arrOfYears.length; i++) {
    const year = arrOfYears[i];
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
      leap.push(year);
    }
  }
  return leap;
}

const input = [2023, 2024, 2025, 2028, 2030];
const output = findLeapYear(input);
console.log(output);
