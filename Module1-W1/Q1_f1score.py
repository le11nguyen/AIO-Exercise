# -------------Question 1: F1 score -----------------

def calculate_metrics(tp, fp, fn):
  """
  This function calculates precision, recall and f1-score given true positives, false positives and false negatives.

  Args:
      tp: Number of true positives.
      fp: Number of false positives.
      fn: Number of false negatives.
  Conditions:
      tp,fp,tn must be integer
      tp,fp,tn must be greater than zero

  Returns:
      A dictionary containing precision, recall and f1-score.

      
          
  """

  # Check if all inputs are integers
  if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
    if not isinstance(tp, int):
      print("tp is not an integer.")
    if not isinstance(fp, int):
      print("fp is not an integer.")
    if not isinstance(fn, int):
      print("fn is not an integer.")
    return None

  # Check if all inputs are above 0
  if tp <= 0 or fp <= 0 or fn <= 0:
    print("tp and fp and fn must be greater than zero")
  

  # Calculate metrics
  precision = tp / (tp + fp)
  recall = tp / (tp + fn)
  f1_score = 2 * (precision * recall) / (precision + recall)


  # Return results
  return precision,recall, f1_score


# Example usage

# calculate_metrics(tp=2 , fp=3 , fn=4)
calculate_metrics(tp ='a', fp =3 , fn =4)
# calculate_metrics(tp =2 , fp ='a', fn =4)
# calculate_metrics(tp =2 , fp =3 , fn ='a')
# calculate_metrics(tp =2 , fp =3 , fn =0)
# calculate_metrics(tp =2.1 , fp =3 , fn =0)
