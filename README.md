This is dataset about cervical cancer occurrences. Cervical cancer is 
one the most frequent cancer diseases that occur to women. This dataset 
is showing some factors that might influence cervical cancer.

## Data

This dataset was found on UCI under the name [Cervical cancer (Risk Factors) Data Set ](https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29#)

The dataset was collected at 'Hospital Universitario de Caracas' in Caracas, Venezuela. 
The dataset comprises demographic information, habits, and historic medical records of 
858 patients. Several patients decided not to answer some of the questions because of 
privacy concerns (missing values).

* 835 instances
* 36 attributes
* Missing values: yes

Output data is located in directory called `data`

`data/cervical-cancer.csv`

Attributes are the same as they were in input data.

## Preparation

To get our output data several things are done to input data:
* missing values marked with "?" are replaced with ""(empty space)

Python scripts are located in directory `scripts`

`scripts/main.py`

## License
Licensed under the [Public Domain Dedication and License][pddl] (assuming
either no rights or public domain license in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
