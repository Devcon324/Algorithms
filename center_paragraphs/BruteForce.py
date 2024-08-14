def center_paragraphs(paragraphs, width):
  result = []
  topBottomBorder = '*' * (width + 2)
  result.append(topBottomBorder) # loads top border

  # formats each line array of the paragraph array
  for line in paragraphs:
    lineLength = 0
    fittedWords, extraWords = [], []
    # Parses a line of words in a paragraph and splits them into lines that fit within the width
    for word in line:
      lineLength += len(word)
      if (lineLength <= width -2):
        fittedWords.append(word) # then the word is added to the line
      elif (lineLength > width-2):
        extraWords.append(word) # then the word needs to go onto the next line

    # * handle a line that has fitted words
    lineString = ' '.join(fittedWords) # join the word array into a string, separated by a space
    spaces = (width - len(lineString)) # gets the number of spaces needed
    if spaces % 2 == 0:
      resultLineString = '*' + ' ' * (spaces // 2) + lineString + ' ' * (spaces // 2) + '*'
    else:
      resultLineString = '*' + ' ' * (spaces // 2) + lineString + ' ' * ((spaces // 2) + 1) + '*'
    # add the line to the result
    result.append(resultLineString)

    # * handle a line that has extra words, ONLY WORKS FOR 1 LINE OF EXTRA WORDS
    if extraWords:
      extraWordsString = ' '.join(extraWords) # join the word array into a string, separated by a space
      spaces = (width - len(extraWordsString))  # gets the number of spaces needed
      if spaces % 2 == 0:
        resultLineString = '*' + ' ' * (spaces // 2) + extraWordsString + ' ' * (spaces // 2) + '*'
      else:
        resultLineString = '*' + ' ' * (spaces // 2) + extraWordsString + ' ' * ((spaces // 2) + 1) + '*'
      result.append(resultLineString) # add the line to the result
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