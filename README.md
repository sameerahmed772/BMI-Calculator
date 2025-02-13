# Basic Weight and Height Calculator

This is a simple Python program that calculates the **Body Mass Index (BMI)** based on user inputs for weight and height. It supports different units for weight (kilograms or pounds) and height (inches or centimeters).

---

## Features

- **Weight Input**: Accepts weight in kilograms (kg) or pounds (lb).
- **Height Input**: Accepts height in centimeters (cm) or inches (in).
- **BMI Calculation**: Computes the BMI using the formula:
  \[
  \text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}
  \]
- **BMI Interpretation**: Provides a basic interpretation of the BMI result (underweight, normal weight, overweight, or obese).

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sameerahmed772/BMI-Calculator.git
   cd BMI-Calculator
   ```

2. **Run the Program**:
   - Ensure you have Python installed on your system.
   - Run the program using the following command:
     ```bash
     python main.py
     ```

3. **Input Your Data**:
   - Enter your weight when prompted.
   - Specify whether the weight is in kilograms (`K`) or pounds (`P`).
   - Enter your height when prompted.
   - Specify whether the height is in centimeters (`C`) or inches (`I`).

4. **View the Results**:
   - The program will calculate your BMI and display the result along with an interpretation.

---

## Example

```
Enter Your Weight: 70
Kilograms or Pound? (K/P): K
Enter Your Height: 175
Inches or Centimetres? (I/C): C
Your BMI is: 22.86
You have a normal weight.
```

---

## BMI Categories

The program uses the following BMI categories for interpretation:

- **Underweight**: BMI < 18.5
- **Normal Weight**: 18.5 ≤ BMI < 24.9
- **Overweight**: 25 ≤ BMI < 29.9
- **Obese**: BMI ≥ 30

---

## Requirements

- Python 3.x

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to open an issue or submit a pull request.

---

Enjoy using the **Basic Weight and Height Calculator**! If you have any questions or feedback, feel free to reach out.
