from urllib.request import urlopen

with open("../data/cervical-cancer.csv", "w") as bumps_file:
    unique_row = []
    for line in urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv"):
        decodedLine = line.decode('UTF-8')
        decodedLine = decodedLine.replace('?', '')

        if decodedLine.strip() not in unique_row:
            unique_row.append(decodedLine.strip())
            bumps_file.write(decodedLine.strip() + '\n')

    bumps_file.close()
