while True:
      numbers = int(input())
      if numbers == -1:
         break

      divisors = []
      total = 0

      for i in range(1, numbers):
          if numbers % i == 0:
             divisors.append(i)
             total += i

      if total == numbers:
         print(f"{numbers} = " + " + ".join(map(str, divisors)))
      else:
         print(f"{numbers} is NOT perfect")