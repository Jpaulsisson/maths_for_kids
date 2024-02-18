from random import randrange

# Easier to work with helper function to get random numbers in a range
def getRandomIntInRange(start: int, stop: int) -> int:
  x = randrange(start, stop+1)
  return x

# Helper function for the digits variables in the problem generator functions
def getRangeEndpoints(digits) -> dict:
  if digits > 5: return "This function only allows up to 5 digits."
  match digits:
    case 1:
      digitRange = { "start": 1, "stop": 9 }
    case 2:
      digitRange = { "start": 10, "stop": 99 }
    case 3:
      digitRange = { "start": 100, "stop": 999 }
    case 4:
      digitRange = { "start": 1000, "stop": 9999 }
    case 5:
      digitRange = { "start": 10000, "stop": 99999 }        
  return digitRange

# generates an addition problem and returns a dictionary with the values and solution
def generateAdditionProblem(digits, secondDigits=None) -> dict:
  xRange = getRangeEndpoints(digits)
  yRange = getRangeEndpoints(digits) if secondDigits == None else getRangeEndpoints(secondDigits)
  
  x = getRandomIntInRange(xRange["start"], xRange["stop"])
  y = getRandomIntInRange(yRange["start"], yRange["stop"])
  
  return { "x": x, "y": y, "solution": x + y }

# generates a subtraction problem and returns a dictionary with the values and solution
def generateSubtractionProblem(digits, secondDigits=None, negativeAnswers=False) -> dict:
  if secondDigits > digits and negativeAnswers == False: return "This will only produce answers with negative values. Please change the digit amount of the second value or set negativeAnswers to true"
  xRange = getRangeEndpoints(digits)
  yRange = getRangeEndpoints(digits) if secondDigits == None else getRangeEndpoints(secondDigits)
  
  x = getRandomIntInRange(xRange["start"], xRange["stop"])
  y = getRandomIntInRange(yRange["start"], yRange["stop"])
    
  if negativeAnswers == False:
    while x - y < 0:
      x = getRandomIntInRange(xRange["start"], xRange["stop"])
      y = getRandomIntInRange(yRange["start"], yRange["stop"])
      
  return { "x": x, "y": y, "solution": x - y }

# generates a multiplication problem and returns a dictionary with the values and solution
def generateMultiplicationProblem(digits, secondDigits=None) -> dict:
  xRange = getRangeEndpoints(digits)
  yRange = getRangeEndpoints(digits) if secondDigits == None else getRangeEndpoints(secondDigits)
  
  x = getRandomIntInRange(xRange["start"], xRange["stop"])
  y = getRandomIntInRange(yRange["start"], yRange["stop"])
  
  return { "x": x, "y": y, "solution": x * y }

# generates a division problem and returns a dictionary with the values and solution
def generateDivisionProblem(digits, secondDigits=None, remainders=True) -> dict:
  if secondDigits > digits and remainders == False: return "This will only produce answers with remainders. Please change the digit amount of the second value or set remainders to true"
  xRange = getRangeEndpoints(digits)
  yRange = getRangeEndpoints(digits) if secondDigits == None else getRangeEndpoints(secondDigits)
  
  x = getRandomIntInRange(xRange["start"], xRange["stop"])
  y = getRandomIntInRange(yRange["start"], yRange["stop"])
  
  if remainders == False:
    while x % y != 0:
      x = getRandomIntInRange(xRange["start"], xRange["stop"])
      y = getRandomIntInRange(yRange["start"], yRange["stop"])
      
  return { "x": x, "y": y, "solution": x / y }

# Helper function to run a function x times
def run_x_times(x: int, func, *func_args) -> list:
  result = []
  i = 1
  while i <= x:
    val = func(*func_args)
    result.append(val)
    i += 1
  return result

# Helper function to generate a list of random values
def generateListOfNumbers(digits, amountOfNumbers):
  result = []
  start, stop = getRangeEndpoints(digits).values()
  i = 0
  while i < amountOfNumbers:
    result.append(getRandomIntInRange(start, stop))
    i += 1
  return result

# Returns the mean of a list of numbers
def getMean(listOfNumbers): 
  result = 0
  for num in listOfNumbers:
    result += num
  result /= len(listOfNumbers)
  return result

# Returns the median of a list of numbers
def getMedian(listOfNumbers):
  sortedNums = sorted(listOfNumbers)
  if len(sortedNums) % 2 == 0:
    first, second = sortedNums[len(sortedNums) // 2 - 1], sortedNums[len(sortedNums) // 2]
    median = (first + second) / 2
  else:
    median = sortedNums[len(sortedNums) // 2]
  return median

# Returns the mode(s) or "No mode" from a list of numbers
def getMode(listOfNumbers):
  result = { "type": "", "mode": [] }
  if len(listOfNumbers) == 0:
    result["type"], result["mode"] = "none", "no mode"
  elif len(listOfNumbers) == 1:
    result["type"], result["mode"] = "single-mode", listOfNumbers[0]
  else:
    uniqueNums = set(listOfNumbers)
    counted = {}
    for num in uniqueNums:
      counted[num] = listOfNumbers.count(num)
    counts = [*counted.values()]
    if all(val == 1 for val in counts):
      result["type"], result["mode"] = "none", "no mode" 
    elif all(val == counts[0] for val in counts) and all(val > 1 for val in counts) and len(counts) > 1:
      result["type"], result["mode"] = "multi-mode", [*uniqueNums]
    else:
      highest = max(counts)
      mode = []
      for key in counted:
        if counted[key] == highest:
          mode.append(key)
      if len(mode) > 1:
        result["type"], result["mode"] = "multi-mode", mode
      else:
        result["type"], result["mode"] = "single-mode", mode[0]
  return result
      
