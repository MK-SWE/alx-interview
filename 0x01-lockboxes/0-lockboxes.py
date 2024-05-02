#!/usr/bin/python3
"""
Lockboxes
a method that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
  # Start with the first box unlocked
  unlocked_boxes = {0}
  # Keys we have
  keys = set(boxes[0])
  # While we have keys that can unlock boxes
  while keys:
    new_keys = set()
    # For each key we have
    for key in keys:
      # If the key corresponds to a box
      if key < len(boxes) and key not in unlocked_boxes:
        # Unlock the box
        unlocked_boxes.add(key)
        # Add the keys from the box
        new_keys.update(boxes[key])
    # Update our set of keys
    keys = new_keys
  # If we've unlocked all boxes, return True
  return len(unlocked_boxes) == len(boxes)
