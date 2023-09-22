function is_fizz(n: number): boolean {
  return n % 3 == 0;
}

function is_buzz(n: number): boolean {
  return n % 5 == 0;
}

function is_fizzbuzz(n: number): boolean {
  return is_fizz(n) && is_buzz(n);
}

export function FizzBuzz(start: number, end: number) {
  const output: string[] = [];

  for (let i = start; i <= end; i++) {
    if (is_fizzbuzz(i)) {
      output.push("FizzBuzz");
    } else if (is_fizz(i)) {
      output.push("Fizz");
    } else if (is_buzz(i)) {
      output.push("Buzz");
    } else {
      output.push(i.toString());
    }
  }

  return output;
}
