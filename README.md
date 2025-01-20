# Sales Prediction with Machine Learning using Python

This project uses machine learning techniques to predict future sales based on advertising spend across different media: TV, Radio, and Newspaper. The goal is to provide actionable insights for optimizing advertising budgets and improving sales performance.

---

## Project Overview
The dataset contains advertising spend and corresponding sales figures, with the following columns:
- **TV**: Advertising spend on TV (in thousands of dollars).
- **Radio**: Advertising spend on Radio (in thousands of dollars).
- **Newspaper**: Advertising spend on Newspapers (in thousands of dollars).
- **Sales**: Actual sales generated (in thousands of units).

The task involves:
1. Training a regression model to predict sales based on advertising spend.
2. Evaluating the model's performance.
3. Providing actionable insights for future advertising strategies.

---

## Future Sales Prediction

![image](https://github.com/user-attachments/assets/d845b39d-6993-4571-af27-83aa53638687)

### Evaluation Metrics:
- **Mean Squared Error (MSE)**: `5.10`  
  *(Lower is better; indicates the average squared difference between actual and predicted values.)*
- **R-squared (R²)**: `0.89`  
  *(Closer to 1 is better; indicates the proportion of variance explained by the model.)*

### Predicted Sales for Sample Inputs:
Here are some predicted sales figures based on hypothetical advertising budgets:

| TV Spend | Radio Spend | Newspaper Spend | Predicted Sales |
|----------|-------------|-----------------|-----------------|
| $150     | $20         | $30             | 15.8 units      |
| $200     | $40         | $50             | 20.3 units      |
| $300     | $60         | $70             | 27.5 units      |

---

## Insights from the Analysis

1. **Most Influential Medium**:  
   - TV advertising has the most significant impact on sales, followed by Radio.
   - Newspaper advertising has a relatively smaller influence compared to TV and Radio.

2. **Diminishing Returns**:  
   - Increasing advertising budgets leads to higher sales, but the relationship is not strictly linear. Beyond a certain point, returns diminish.

3. **Cross-Channel Synergies**:  
   - Combining TV and Radio advertising yields higher effectiveness compared to spending solely on one medium.

---

## Recommendations

1. **Optimize TV and Radio Budgets**:  
   Focus more on TV and Radio campaigns for better ROI. For example:
   - Allocate 60% of the budget to TV.
   - Allocate 30% to Radio.
   - Use the remaining 10% for Newspaper campaigns.

2. **Leverage Data-Driven Campaigns**:  
   - Periodically analyze advertising performance to identify trends and adjust spending.

3. **Explore Digital Advertising**
