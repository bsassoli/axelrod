## Charting of no_cultures vs timesteps
### Logic of this type of chart is compare multiple stochastic runs of the same params
- [x]  ~~make chart break once model reaches equilibrium (might make sense to just have a `stop simulation` button)~~
- [] maybe make a `restart` simulation button?
- [x] ~~resize chartv
- [x] ~~make model get args from input form~~


## Implement color charting evolution of models
### This just gives a more visual sense of how a model evolves
- [] use `make_color_snapshot` in `helpers.py` as logic
- [] pass it to *bubble* chart in `chart.js`
- NB this would not be a visualization that's compatible with the previous one

## Refactoring 
### Implement `Agent` class so as to give user more choices
- [] Types of agent could have more aggressiveness, less aggressiveness etc.
- [] User could choose mix when customizing model

## Write docstrings and comments

## Make site a little prettier

## Deploy to heroku

## Remember to quote sources in the README.md file