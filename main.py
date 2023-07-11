# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(word):
  word_list = []

  for i in word:
      current_letter = i.lower()

      if len(word_list) == 0:
          word_list.append(i)
      elif current_letter == word_list[-1].lower():
          word_list.pop()
      else:
          word_list.append(i)
  result = " ".join(word_list)
  return result


print(print_hi("totally"))