# genetic-algorithm-band-selection

This repository contains the program to perform band selection for hyperspectral images.
Here we have used Indian_pines dataset from - http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes#Indian_Pines


### ga_utility.py
  - This is a utility file. It contains all the functions required to implement the genetic algorithm for band selection for hyperspectral images

### geneticalgorithm.py
  - This file contains the driver code for running the program.
  
- In this program we are selecting 10 bands out of 200 bands using genetic algorithm. 
- The population consists of 8 individuals
- Each individual has 10 genes.

For running the program run - 

```sh
$ python geneticalgorithm.py
```

 *If you want to use your own dataset change it in the ga_utility.py file.*
