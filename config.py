seed = 1234
evotorch_seed = 1234
deterministic_matches = False
allow_model_rng_access = False
warmup_rounds = 0
total_rounds = 150
popsize = 250
generations = 1000
log_interval = 1
pickle_interval = 5
stdev_init = 10.0
initial_bounds = 5.0
ROCK = 0
PAPER = 1
SCISSORS = 2
# mean_eval | pop_best_eval | median_eval | best_eval | worst_eval
visualization_metric = 'median_eval'
hidden_dim = 25

# allows the introduction of asymmetries that destabilize
#  the trivial always-random strategy
score_weights = {
    'rock': 2.0,
    'paper': 1.0,
    'scissors': 1.0
}


