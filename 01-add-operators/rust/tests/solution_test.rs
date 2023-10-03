#[cfg(test)]
mod tests {
    use addOperators::addOperators;

    #[test]
    fn test_solution() {
        let result = addOperators(123, 6);
        let expected = vec!["1*2*3", "1+2+3"]
        assert_eq!(result, expected)
        
    }
}