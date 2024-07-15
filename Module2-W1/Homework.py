import numpy as np
import matplotlib.image as mpimg
import pandas as pd


# Question 12 - Lightness
img = mpimg.imread ('Module2-W1/dog.jpeg')
gray_img_01 = (img.max(axis=2) + img.min(axis=2)) / 2
print(gray_img_01 [0 , 0])

# Question 13 - Average
gray_img_01 = img.mean(axis=2)
print(gray_img_01 [0 , 0])

# Question 14 - Luminosity:
gray_img_01 = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
print(gray_img_01 [0 , 0])


# DATA
df = pd.read_csv ('Module2-W1/advertising.csv')
data = df.to_numpy()

# Question 15
max_value = data[:, -1].max()
max_index = data[:, -1].argmax()
print(f"Max: {max_value} - Index: {max_index}")

# Question 16
mean_tv = data[:, 0].mean()
print(f"Mean TV: {mean_tv}")

# Question 17
count_sales = (data[:, -1] >= 20).sum()
print(f"Count: {count_sales}")

# Question 18
mean_radio = data[data[:, -1] >= 15, 1].mean()
print(f"Mean Radio: {mean_radio}")

# Question 19
mean_newspaper = data[:, 2].mean()
total_sales = data[data[:, 2] > mean_newspaper, -1].sum()
print(f"Total Sales: {total_sales}")

# Question 20
mean_sales = data[:, -1].mean() 
scores = np.where(data[:, -1] > mean_sales, 'Good', np.where(data[:, -1] < mean_sales, 'Bad', 'Average'))
print(scores[7:10])

# Question 21
mean_sales = data[:, -1].mean() 
closest_to_mean_sales = data[np.abs(data[:, -1] - mean_sales).argmin(), -1] 

scores = np.where(data[:, -1] > closest_to_mean_sales, 'Good', np.where(data[:, -1] < closest_to_mean_sales, 'Bad', 'Average')) 

print(scores[7:10])