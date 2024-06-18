#!/bin/bash

add() {
  echo "Addition: $(($1 + $2))"
}

subtract() {
  echo "Subtraction: $(($1 - $2))"
}

multiply() {
  echo "Multiplication: $(($1 * $2))"
}

divide() {
  if [ $2 -ne 0 ]; then
    echo "Division: $(($1 / $2))"
  else
    echo "Division: Error! Division by zero."
  fi
}

read -p "Enter first number: " num1
read -p "Enter second number: " num2

add $num1 $num2
subtract $num1 $num2
multiply $num1 $num2
divide $num1 $num2
