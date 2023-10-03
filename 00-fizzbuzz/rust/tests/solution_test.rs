#[cfg(test)]
mod tests {
    use fizzbuzz::fizzbuzz;
    use std::fs;

    #[test]
    fn test_solution() {
        let expected = {
            let contents = fs::read_to_string("../expected.json").expect("Error reading file");
            serde_json::from_str::<Vec<String>>(&contents).expect("Error serializing to JSON")
        };

        let result = fizzbuzz(1, 100);

        assert_eq!(result, expected)
    }
}
