# decision-ranking
A Python app that ranks a list of input items by presenting two at a time for the user to choose from.

# Overview
Often decision making process with many options can be simplified by considering two options at a time. And this process of ranking options can be modelled after a page ranking algorithm. 

For example, "option B is more preferred to option A" is liken to "page A references page B" (which increases the likelihood of page B ranking higher than A). This approach minimizes the number of questions required to establish ranking. 

# Getting Started 
First, open the terminal and `cd` into the directory where you would like to download this program.
Then, clone the decision-app repository
```
git clone https://github.com/sallyhk/decision-ranking.git
```
Use the following command to run the program:
```
python app.py
```
When prompted, enter decisions you'd like help making, separated by commas. 
That's it! :)

# Example
The below is an example of the app for deciding what to have for dinner...
<img width="932" alt="decision-ranking" src="https://user-images.githubusercontent.com/39283556/81512020-32208180-92d2-11ea-9275-c55214edb9eb.png">

Sushi tonight!

# Behind the Scene
Libraries used:
`random`, `numpy`, `collections`

## Algorithm
Leverages page ranking algorithm, using a custom function named `decision_rank`.

1. Randomly sort user's input of _n_ decisions to make. This new ordering persists throughout the program.
2. Create a matrix of size _n_ by _n_ with zeros.
3. Run `decision_rank` with the matrix. This outputs a vector of weights for each decision. For the first run, the weights would be equal.
4. Pick the first two decisions with the same weight, and prompt user to choose one of the two.
5. Update the matrix by adding 1 to row _i_ and column _j_ where _i_ is the index of the unchosen decision and _j_ that of the chosen.
6. Repeat Step 3 - 5 until the vector of weights no longer have equal weights.
7. Order the decisions based on their final weights - the greater the weights, the higher the ranking.

## Potential Enhancements
* nicer GUI