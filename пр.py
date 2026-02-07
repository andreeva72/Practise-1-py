import 'dart:io';
import 'dart:math';

void main(List<String> args) {
  double a, b;
  
  if (args.length >= 2) {
    a = double.parse(args[0]);
    b = double.parse(args[1]);
  } else {
    print("Введите первое число:");
    String input1 = stdin.readLineSync()!;
    a = double.parse(input1);
    
    print("Введите второе число:");
    String input2 = stdin.readLineSync()!;
    b = double.parse(input2);
  }
  
  print("АРИФМЕТИКАз");
  print("Сложение: " + (a + b).toString());
  print("Вычитание: " + (a - b).toString());
  print("Умножение: " + (a * b).toString());
  
  if (b != 0) {
    print("Деление: " + (a / b).toString());
    print("Целочисленное деление: " + (a ~/ b).toString());
    print("Остаток: " + (a % b).toString());
  } else {
    print("На ноль делить нельзя!");
  }
  
  print("Степень: " + pow(a, b).toString());
  
  // Оценка 4: Сравнение
  print("\n=== ОЦЕНКА 4: СРАВНЕНИЕ ===");
  print("Равно: " + (a == b).toString());
  print("Не равно: " + (a != b).toString());
  print("Больше: " + (a > b).toString());
  print("Меньше: " + (a < b).toString());
  print("Больше или равно: " + (a >= b).toString());
  print("Меньше или равно: " + (a <= b).toString());
  
  // Оценка 5: Логика
  print("\n=== ОЦЕНКА 5: ЛОГИКА ===");
  bool uslovie1 = a > 10;
  bool uslovie2 = b < 5;
  bool uslovie3 = a == b;
  
  print("a > 10: " + uslovie1.toString());
  print("b < 5: " + uslovie2.toString());
  print("a == b: " + uslovie3.toString());
  
  print("\nЛогическое И (&&):");
  print("a > 10 && b < 5: " + (uslovie1 && uslovie2).toString());
  print("a > 10 && a == b: " + (uslovie1 && uslovie3).toString());
  
  print("\nЛогическое ИЛИ (||):");
  print("a > 10 || b < 5: " + (uslovie1 || uslovie2).toString());
  print("a > 10 || a == b: " + (uslovie1 || uslovie3).toString());
  
  print("\nЛогическое НЕ (!):");
  print("!(a > 10): " + (!uslovie1).toString());
  print("!(a == b): " + (!uslovie3).toString());
  
  print("\nКомбинированные условия:");
  bool kombin1 = (a > b) && !(a == 0);
  print("(a > b) && !(a == 0): " + kombin1.toString());
  
  bool kombin2 = (a < 0) || (b > 100);
  print("(a < 0) || (b > 100): " + kombin2.toString());
}