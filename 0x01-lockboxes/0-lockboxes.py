#!/usr/bin/python3
'''This module contains the lockbox implementation.
'''


def canUnlockAll(boxes):
  """Checks if all boxes in a list can be unlocked, given the first box is open.

  Args:
    boxes: A list of lists, where each inner list represents a box containing keys (indices) to other boxes.

  Returns:
    True if all boxes can be unlocked, False otherwise.
  """

  total_boxes = len(boxes)
  accessible_boxes = {0}  # Initially, only box 0 is accessible
  potential_keys = set(boxes[0]) - {0}  

  while potential_keys:
    new_key = potential_keys.pop()
    if new_key not in accessible_boxes and 0 <= new_key < total_boxes:  
      accessible_boxes.add(new_key)
      potential_keys |= set(boxes[new_key]) 

  return total_boxes == len(accessible_boxes)
