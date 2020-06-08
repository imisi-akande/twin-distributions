# twin-distributions

This Python module can be used to obtain the Binomial and Normal distribution.

## Instructions
- Clone the repository
    - ```Git clone https://github.com/imisi-akande/twin-distributions.git```

- Change Directory
    - ```cd twin-distributions```
- Enter your terminal

- Install the module:
    - ```pip install .```

- Enter your python interactive shell:
    - ```python```

- Import required functions:
    - ```from twin_distribution import Binomial, Normal```

- To obtain normal distribution:
    - ```normal_dist_one = Normal(25, 3)```
    - ```normal_dist_two = Normal(30, 2)```

- To obtain the mean values of Normal distribution:
    - ```normal_dist_one.mean```
    - ```normal_dist_two.mean```

- To obtain the standard deviation values of Normal distribution:
    - ```normal_dist_one.stdv```
    - ```normal_dist_two.stdv```

- Add two Normal instances:
    - ```normal_dist_one + normal_dist_two```

- Read data from an extrernal file
    - ```normal_three = Normal() ```
    - ```normal_three.read_input_file('numbers.txt') ```

- To obtain binomial distribution:
    - ```binomial_dist_one = Binomial(.5, 20)```
    - ```binomial_dist_two = Binomial(.5, 30)```

- To obtain the mean values of Binomial distribution:
    - ```binomial_dist_one.mean```
    - ```binomial_dist_two.mean```

- To obtain the standard deviation values of Binomial distribution:
    - ```binomial_dist_one.stdv```
    - ```binomial_dist_two.stdv```

- Add two binomial instances:
    - ```binomial_dist_one + binomial_dist_two```