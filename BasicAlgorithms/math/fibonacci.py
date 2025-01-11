def fibonacci_recursion(n: int) -> int:
  """
  Алгоритм поиска номера числа в последовательности Фибоначчи.
  
  Последовательность Фибоначчи - это последовательность, в которой 
  каждое число является суммой двух предыдущих (0, 1, 1, 2, 3, 5...).
  
  Аргумент n - это номер числа, которое нужно найти.
  
  Оптимизация: для маленьких значений n.
  
  Применение: в математике, моделировании, некоторых алгоритмах.
  """
  if n <= 1:
    return n
  
  return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
  
  
def fibonacci_iterative(n: int) -> int:
  """
  Алгоритм поиска номера числа в последовательности Фибоначчи.

  Последовательность Фибоначчи - это последовательность, в которой 
  каждое число является суммой двух предыдущих (0, 1, 1, 2, 3, 5...).

  Аргумент n - это номер числа, которое нужно найти.

  Оптимизация: для больших значений n.

  Применение: в математике, моделировании, некоторых алгоритмах.
  """
  if n <= 1:
    return n
  
  a, b = 0, 1
  
  for _ in range(2, n + 1):
    a, b = b, a + b
  
  return b