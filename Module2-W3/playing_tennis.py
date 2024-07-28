# ########################
# Create data
# ########################
import numpy as np


def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']
    ]
    return np . array(data)


train_data = create_train_data()
print(train_data)


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np . zeros(len(y_unique))
    for i, j in enumerate(y_unique):
        prior_probability[i] = np.sum(train_data[:, -1] == j) / len(train_data)
    return prior_probability


prior_probablity = compute_prior_probability(train_data)
print("P( play tennis = No", prior_probablity[0])
print("P( play tennis = Yes", prior_probablity[1])


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []
    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for j, y in enumerate(y_unique):
            for k, x in enumerate(x_unique):
                x_conditional_probability[j, k] = np.sum((train_data[:, i] == x) & (
                    train_data[:, -1] == y)) / np.sum(train_data[:, -1] == y)
        conditional_probability.append(x_conditional_probability)
    return conditional_probability, list_x_name


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])


def get_index_from_value(feature_name, list_features):
    return np.nonzero(list_features == feature_name)[0][0]


outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)


x1 = get_index_from_value("Sunny", list_x_name[0])
conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
print(
    f"P('Outlook'='Sunny'|Play Tennis'='Yes') = {conditional_probability[0][1, x1]:.2f}")


print(
    f"P('Outlook'='Sunny'|Play Tennis'='No') = {conditional_probability[0][0, x1]:.2f}")


def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)
    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])

    p0 = prior_probability[0] * conditional_probability[0][0, x1] * conditional_probability[1][0,
                                                                                               x2] * conditional_probability[2][0, x3] * conditional_probability[3][0, x4]
    p1 = prior_probability[1] * conditional_probability[0][1, x1] * conditional_probability[1][1,
                                                                                               x2] * conditional_probability[2][1, x3] * conditional_probability[3][1, x4]

    return 1 if p1 > p0 else 0


X = ['Sunny', 'Cool', 'High', 'Strong']
pred = prediction_play_tennis(
    X, list_x_name, prior_probablity, conditional_probability)
print("Ad should go!" if pred else "Ad should not go!")
