# phbs-qps-2024
The code is to get US CPI data and report the last quarters of inflation in the US.

## URL to the repository
[GitHub Repository](https://github.com/Jeff-cyberprog/phbs-qps-2024)

## file structure
```
phbs-qps-2024
├── data
├── notebooks
├── scripts
└── src
```

## installation
Please make sure you have installed the packages below:

- pandas
- pandas\_datareader

You can use the instructions below to install needed packages

```bash
pip install pandas pandas_datareader
```

## usage
Here is how to run a script to obtain US CPI data and report inflation rates for the past four quarters:

1.clone the storage to local:
``` bash
git clone https://github.com/Jeff-cyberprog/phbs-qps-2024
```

2.enter into the storage directory
```bash
cd phbs-qps-2024
```


3.create and activate virtual environment(recomment, but optional, you can just use the enviroment you have)
```bash
# use conda command to create virtual environment(you can use other command)
conda create phbs-qps-2024-env python=3.8

# activate virtual environment
conda activate phbs-qps-2024-env
```


4.install packages
```bash
pip install pandas pandas_datareader
```

5.run the script
```bash
python scripts/Get_US_CPI.py
```

After run the script, the data would be saved into "data/last\_4\_quarters\_inflation.csv"
