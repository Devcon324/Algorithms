def center_paragraphs(paragraphs, width):
  # Parses a line of words in a paragraph and splits them into lines that fit within the width
  # returns a 2D array of lines that fit within the width
  def fitWordsToLine(line, width):
    lineLength = 0
    resultLine, fittedWords, extraWords= [], [], []
    for word in line:
      lineLength += len(word)
      if (lineLength <= width -2):
        fittedWords.append(word) # then the word is added to the line
      elif (lineLength > width-2):
        extraWords.append(word) # then the word needs to go onto the next line
    resultLine.append(fittedWords) # adds the fitted words to the line
    if extraWords:
      resultLine.extend(fitWordsToLine(extraWords, width)) # recursively fits extra words in a line
    return resultLine

  result = []
  topBottomBorder = '*' * (width + 2)
  result.append(topBottomBorder) # loads top border
  # formats each line array of the paragraph array
  for line in paragraphs:
    resultMatrix = fitWordsToLine(line, width) # returns a matrix of lines
    for resultLine in resultMatrix:
      lineString = ' '.join(resultLine) # join the word array into a string, separated by a space
      spaces = (width - len(lineString)) # gets the number of spaces needed
      # even spaces at the beginning and end of the line, odd spaces at the end
      if spaces % 2 == 0:
        resultLineString = '*' + ' ' * (spaces // 2) + lineString + ' ' * (spaces // 2) + '*'
      else:
        resultLineString = '*' + ' ' * (spaces // 2) + lineString + ' ' * ((spaces // 2) + 1) + '*'
      result.append(resultLineString) # add the final formatted line to the result
  result.append(topBottomBorder) # add bottom border
  return result



# main function to test the center_paragraphs function
if __name__ == "__main__":
  width = 16
  paragraphs = [
    ['Hello', 'world'],
    ['This','text','isCentered','now', 'forever', 'and', 'always'],
    ['Lets','see','this']
  ]
  #*Expected output:
  # ******************
  # *  Hello world   *
  # *   This text    *
  # * isCentered now *
  # *  forever and   *
  # *     always     *
  # * Lets see this  *
  # ******************
  try:
    centeredPara = center_paragraphs(paragraphs, width)
    for line in centeredPara:
      print(line)
  except Exception as e:
    print(f"An error occurred: {e}")