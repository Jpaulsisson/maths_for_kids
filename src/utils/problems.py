from random import randrange

def getRandomIntInRange(start: int, stop: int) -> int:
  x = randrange(start, stop+1)
  return x

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


def generateAdditionProblem(digits, secondDigits=None) -> dict:
  xRange = getRangeEndpoints(digits)
  yRange = getRangeEndpoints(digits) if secondDigits == None else getRangeEndpoints(secondDigits)
  
  x = getRandomIntInRange(xRange["start"], xRange["stop"])
  y = getRandomIntInRange(yRange["start"], yRange["stop"])
  
  return { "x": x, "y": y, "solution": x + y }

def generateSubtractionProblem(digits, secondDigits=None, negativeAnswers=True) -> dict:
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

def generateMultiplicationProblem(digits, secondDigits=None, negativeAnswers=True) -> dict:
  xRange = getRangeEndpoints(digits)
  yRange = getRangeEndpoints(digits) if secondDigits == None else getRangeEndpoints(secondDigits)
  
  x = getRandomIntInRange(xRange["start"], xRange["stop"])
  y = getRandomIntInRange(yRange["start"], yRange["stop"])
  
  if negativeAnswers == False:
    while x - y < 0:
      x = getRandomIntInRange(xRange["start"], xRange["stop"])
      y = getRandomIntInRange(yRange["start"], yRange["stop"])
  
  return { "x": x, "y": y, "solution": x * y }

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

def run_x_times(x: int, func, *func_args) -> list:
  result = []
  i = 1
  while i <= x:
    val = func(*func_args)
    result.append(val)
    i += 1
  return result
