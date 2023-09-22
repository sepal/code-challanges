import { describe, test, expect } from "vitest";
import { FizzBuzz } from ".";
import fs from "fs";

describe("FizzBuzz", () => {
  test("output should be correct from number 0 to 100", () => {
    const expected = fs.readFileSync("../expected.json");

    const output = JSON.stringify(FizzBuzz(1, 100));
    expect(output).toEqual(expected);
  });
});
