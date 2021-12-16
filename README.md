# Getting Started

## Server setup

1. Start by downloading the Docker image:
   https://storage.googleapis.com/lp-dev-hiring/images/lp-programming-challenge-1-1625758668.tar.gz
1. Load the container: `docker load -i lp-programming-challenge-1-1625758668.tar.gz`.
1. The output there should tell you what it imported. Go ahead and run it, and be sure to expose port `3123`
   so you can access it: `docker run --rm -p 3123:3123 -ti lp-programming-challenge-1`

## Candidate Setup

1. pip install the requirements.txt file
2. run `python animals.py`
