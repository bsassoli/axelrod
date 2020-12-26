# THIS IS AXELROD50
## Final project for CS50



### Summary 
http://axelrod.herokuapp.com
A webapp simulating Robert Axelrod model of cultural interaction, developed in `Python`,`Flask`, and `Javascript` using `chart.js`.

### Background

[Robert Axelrod](https://en.wikipedia.org/wiki/Robert_Axelrod) is a political scientist who developed a well-known [agent-based model](https://en.wikipedia.org/wiki/Agent-based_model) simulating the dissemination of cultures in his 1997 paper "The dissemination of culture: a model with local convergence and global polarization" ([download](http://www-personal.umich.edu/~axe/research/Dissemination.pdf)).

The model simulates how cultures interact based on their relative similarities. 

A model is a grid of size **(a x b)** each cell of which represents a culture or agent.  Each culture is in turn represented as a vector of **n** *features*, each of which can assume **k** values or *traits*. At each timestep the model is updated as follows:

1. an agent ***A*** is picked at random;

2. a neighbour ***N*** is picked at random from the cells adjacent to ***A***;

3. ***A*** and ***N*** will interact with probably equal to the number of traits they share divided by the number of features: 
   $$
   P(interact_{(A,B)}) = \dfrac{\sum{common\ traits}}{n}
   $$

4. if they do interact then one of the traits that ***A*** that shares with ***N*** will be replaced by the corresponding neighbour's trait.

### How it works

Upon loading the user will be presented with a choice of parameters for the model:

- size
- no_of_features
- no_of_traits

The model will then run and keep iterating until no changes are possible. The chart will display the number of cultures in the model at each 10.000 timesteps of the iteration.

#### Notes

The original code can be found at https://github.com/bsassoli/axelrod.

The real time streaming of the data in `chart.js` consists of code modified from the following [GitHub repo](https://github.com/roniemartinez/real-time-charts-with-flask).
