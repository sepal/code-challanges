pub fn fizzbuzz(start: i32, end: i32) -> Vec<String> {
    let mut result: Vec<String> = Vec::new();

    for i in start..end + 1 {
        match (i % 3, i % 5) {
            (0, 0) => result.push(String::from("FizzBuzz")),
            (0, _) => result.push(String::from("Fizz")),
            (_, 0) => result.push(String::from("Buzz")),
            _ => result.push(i.to_string()),
        }
    }
    result
}
