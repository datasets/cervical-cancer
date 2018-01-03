This is a tool for getting cervical cancer dataset.

## Data

This dataset was found on UCI under the name [Cervical cancer (Risk Factors) Data Set ](https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29#)

The dataset was collected at 'Hospital Universitario de Caracas' in Caracas, Venezuela. 
The dataset comprises demographic information, habits, and historic medical records of 
858 patients. Several patients decided not to answer some of the questions because of 
privacy concerns (missing values).

* 858 incances
* 36 attributes
* Missing values: yes

### Field descriptions:
1. Age : (int)
2. Number of sexual partners : (int) 
3. First sexual intercourse (age) : (int) 
4. Num of pregnancies : (int) 
5. Smokes : (bool) 
6. Smokes : (years) : (bool) 
7. Smokes : (packs/year) : (bool) 
8. Hormonal Contraceptives : (bool) 
9. Hormonal Contraceptives (years) : (int) 
10. IUD : (bool) 
11. IUD (years) : (int) 
12. STDs : (bool) 
13. STDs (number) : (int) 
14. STDs:condylomatosis : (bool) 
15. STDs:cervical condylomatosis : (bool) 
16. STDs:vaginal condylomatosis : (bool) 
17. STDs:vulvo-perineal condylomatosis : (bool) 
18. STDs:syphilis : (bool) 
19. STDs:pelvic inflammatory disease : (bool) 
20. STDs:genital herpes : (bool) 
21. STDs:molluscum contagiosum : (bool) 
22. STDs:AIDS : (bool) 
23. STDs:HIV : (bool) 
24. STDs:Hepatitis B : (bool) 
25. STDs:HPV : (bool) 
26. STDs: Number of diagnosis : (int) 
27. STDs: Time since first diagnosis : (int) 
28. STDs: Time since last diagnosis : (int) 
29. Dx:Cancer : (bool) 
30. Dx:CIN : (bool) 
31. Dx:HPV : (bool) 
32. Dx : (bool) 
33. Hinselmann: target variable : (bool) 
34. Schiller: target variable : (bool) 
35. Cytology: target variable : (bool) 
36. Biopsy: target variable(bool) 

### Output data

Output data is located in directory called `data`

`data/cervical-cancer.csv`

Attributes are the same as they were in input data.

## Scripts

Python scripts are located in directory `scripts`

`scripts/main.py`

## Licence
Licensed under the [Public Domain Dedication and License][pddl] (assuming
either no rights or public domain license in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
