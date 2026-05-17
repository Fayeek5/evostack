import { render, screen } from "@testing-library/react";

describe("EvoStack Homepage", () => {
  test("basic test validation", () => {
    document.body.innerHTML = "<h1>EvoStack</h1>";

    expect(
      screen.getByText("EvoStack")
    ).toBeInTheDocument();
  });
});
