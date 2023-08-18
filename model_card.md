# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Random forest model using tuned hyperparameters. Trained with scikit-learn version 1.2.2.

## Intended Use

Classifying individuals into high salary (>50k) and low salary (<=50k) categories.
It should mainly be used in fairness and bias-related endeavours and not in production.

## Training Data

Census Income dataset acquired from the UCI Machine Learning
Repository: https://archive.ics.uci.edu/dataset/20/census+income

* 14 different attributes (such as ‘age’, ‘workclass’ or ‘hours-per-week’)
    * The redundant attribute "education_num" has been removed
* Target is income: ≤50K or >50K.
* Imbalance ratio (IR) high income : low income of 1 : 3.03

Originally from: Kohavi,Ron. (1996). Census Income. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.

## Evaluation Data

Data segregation was performed with a regular train-test-split with 80% used for training and 20% for testing

## Metrics

F1 classification with a macro average of 0.79, 0.68 for the minority class, and 0.90 for the majority class.

![Classification report](Images/metrics.png "Model Classification report")

When analyzing across data slices, model performance is higher for low-salary individuals.

## Ethical Considerations

If this model were used in decisions, such as job applications or loan approvals, individuals with
accurate income predictions above $50,000 might gain more opportunities, while those predicted below might face
disadvantages. This could further perpetuate existing socioeconomic disparities.

## Caveats and Recommendations

This model is built on a dataset that contains sensitive attributes and (legally) protected groups such as race or sex.
Furthermore, the dataset overall is imbalanced with a higher proportion of low income individuals. For high-income
individuals the F1-score and especially the recall is worse. Also, the model performs slightly worse for women than for
men. Another limitation of the model is the necessity for complete input data. Missing values are not handled
off-the-gate.

It is recommended this model is strictly used for bias and fairness-related studies.
