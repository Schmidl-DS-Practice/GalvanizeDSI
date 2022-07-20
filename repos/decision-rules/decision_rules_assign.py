#part 1

|                        | Actual Positive | Actual Negative |
| :--------------------: |:---------------:|:---------------:|
| **Predicted Positive** |        6        |         6       |
| **Predicted Negative** |        0        |         9       |

#part 2

|    *Threshold: 1.0*    | Actual Positive | Actual Negative |
| ---------------------- |:---------------:|:---------------:|
| **Predicted Positive** |        0        |         0       |
| **Predicted Negative** |        1        |         2       |

|    *Threshold: 0.6*    | Actual Positive | Actual Negative |
| ---------------------- |:---------------:|:---------------:|
| **Predicted Positive** |        0        |         1       |
| **Predicted Negative** |        1        |         1       |

|    *Threshold: 0.4*    | Actual Positive | Actual Negative |
| ---------------------- |:---------------:|:---------------:|
| **Predicted Positive** |        1        |         1       |
| **Predicted Negative** |        0        |         1       |

|    *Threshold: 0.2*    | Actual Positive | Actual Negative |
| ---------------------- |:---------------:|:---------------:|
| **Predicted Positive** |        1        |         2       |

cost_benefit = np.array([[6, 6], [0, 9]])
thresholds = [1.0, 0.6, 0.4, 0.2]
confusion_matrices = [np.array([[0, 0], [1, 2]]),
                      np.array([[0, 1], [1, 1]]),
                      np.array([[1, 1], [0, 1]]),
                      np.array([[1, 2], [0, 0]])]
total_observations = 3

for threshold, confusion_matrix in zip(thresholds, confusion_matrices):
    threshold_expected_profit = np.sum(cost_benefit * confusion_matrix) / total_observations
    print('Profit at threshold of {}: {}'.format(threshold, threshold_expected_profit))

import pandas as pd
import profit_curve_solution as ss

df = pd.read_csv('data/churn.csv')
print(df)

df.drop(['State', 'Area Code', 'Phone'], axis=1, inplace=True)
#print(df)
df = pd.get_dummies(df, columns=["Int'l Plan", "VMail Plan"])
#print(df)

cost_benefit_matrix = np.array([[79, -20], [ 0,   0]])