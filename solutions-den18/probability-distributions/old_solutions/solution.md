## Part 1: Identifying Distributions

1. A typist makes on average 2 mistakes per page.  What is the probability of a particular page having no errors on it?

   ```
   #X ~ Poisson(2)

   #P(X = 0)
   #= (2 ^ 0 / 0!) * e ^ -2
   #~= 0.135
   
   dist = stats.poisson(mu=2)
   print("P(X = 0) = ", dist.pmf(0))
   ```


2. Components are packed in boxes of 20. The probability of a component being
   defective is 0.1. What is the probability of a box containing exactly 2 defective components?

   ```
   #X ~ Binomial(n=20, p=0.1)

   #P(X = 2)
   # 20 C 2 is 20 choose 2
   #= (20 C 2) * (0.1 ^ 2) * (1 - 0.1) ^ 18
   #= (20! / 2! * 18!) * (0.1 ^ 2) * (1 - 0.1) ^ 18
   #~= 0.285
   
   dist = stats.binom(20, 0.1)
   print ("P(X = 2) = ", dist.pmf(2))
   ```

3. Components are packed in boxes of 20. The probability of any individual component being
   defective is 0.1. What is the probability of a box containing AT MOST 2 defective components? 

   ```
   X ~ Binomial(n=20, p=0.1)

   P(X <= 2)
   = P(X == 0) + P(X == 1) + P(X == 2)
   =   (20 C 0) * (0.1 ^ 0) * (1 - 0.1) ^ 20
     + (20 C 1) * (0.1 ^ 1) * (1 - 0.1) ^ 19
     + (20 C 2) * (0.1 ^ 2) * (1 - 0.1) ^ 18
   ~= 0.677
   ```

4. Patrons arrive at a local bar at a rate of 30 per hour. What is the probability that the bouncer can take a three minute bathroom break without missing the next patron? 

   ```
   X = waiting time
   X ~ Exponential(0.5)  # 30 per hour = 0.5 per minute

   P(X > 3)
   = 1 - P(X <= 3)
   = 1 - (1 - exp(-0.5 * 3))
   ~= 0.2231
   ```

5. You need to find a tall person, at least 6 feet tall, to help you reach a cookie jar. 8% of the population is 6 feet or taller, and people pass by on average twice per minute.  If you wait on the sidewalk, what is the probability that you will have to wait longer than ten minutes to get some cookies?

   ```
   # The waiting time is exponentially distributed.
   # The rate that the event "someone of sufficient height passes by"
   # happens is:
   #  rate = 2 persons / 1 min * 8 tall persons / 100 persons
   #       = 0.16 tall persons / min
   X ~ Exponential(rate = 0.16)

   P(X > 10 min)
   = 1 - P(X <= 10 min)
   = 1 - (1 - exp(- 0.16 * 10))
   = exp(- 0.16 * 10)
   ~= 0.201
   ```

6. A harried passenger will be several minutes late for a scheduled 10 A.M. flight to NYC. Nevertheless, he might still make the flight, since boarding is always allowed until 10:10 A.M., and boarding is sometimes permitted up to 10:30 AM.

Assuming the end time of the boarding interval is **uniformly distributed** over the above limits, find the probability that the passenger will make his flight, assuming he arrives at the boarding gate at 10:25.

   ```
   X ~ Uniform(10, 30) # Really uniform over 10:10 to 10:30

   P(X > 25)
   = (30 - 25) / (30 - 10) = 0.25
   ```

7. Your cat starts to beg for dinner at 3:30 every day, and you suspect that it meows at a fixed rate.  You've observed that about one fifth of the time, your cat will not meow until 3:40, giving you ten unexpected minutes of quiet.  What is the probability your cat leaves you alone until 4:00?

   ```
   # Looks like this one is Poisson distributed, but we are not 
   # directly given the rate, so we'll have to figure it out.
   X = # of meows in a ten mins
   X ~ Poisson(lambda=???)

   # But here's what we do know:
   P(X == 0) = 0.2
   # On the other hand, since X is Poisson distributed:
   P(X == 0) = exp(- lambda)
   # So, solving the resulting equation
   lambda = - log(0.2) = 1.6

   # So the rate our cat is meowing is (approximately) 1.6 meows / 10 min
   # Now we can actually solve the problem.  We want:
   P(Cat does not meow between 3:30 and 4:00)
   # Which is a 30 min interval.  So let's get the rate the cat meows
   # in every 30 mins
   lambda = 1.6 meows / 10 min = 4.8 meows / 30 min
   # Now we can calculate the needed probability
   P(Your cat leaves you alone until 4:00)
   = P(Your cat meows 0 times in 30 mins)
   = exp(- 4.8)
   ~= 0.008
   ```
 
8. Somehow you ended up with two types of forks.  There are the good forks, which are big and fit a healthy bite, but there are also these small, thin ones that you don't really understand what they are for, you should probably just get rid of them.  You need two forks for you and your partner, and grab a fistful of 5.  If there are 14 forks in the drawer, of which half are the good kind, what is the probability you have at least your two required good forks?

   ```
   # The number of good forks in hand is Hypergeometrically distributed.
   X = # of good forks in a hand of 5.
   X ~ Hypergeometric(N=14, k=7, n=5)

   P(X >= 2)
   = 1 - P(X <= 1)
   # I used scipy for this one.
   # 1 -  scipy.stats.hypergeom(14, 7, 5).cdf(1) 
   ~= 0.867
   ```

## Part 2: Distribution Simulation

1. Given the distributions of each of variables, use `scipy` to write a function that would draw random values from each of the distributions to simulate draws from the distribution of `profit`

   ```python
   def profit_rvs():
       num_views = int(sc.uniform(loc=5000, scale=1000).rvs())
       conversions = sc.binom(p=0.12, n=num_views).rvs()
       wholesales = sc.binom(p=0.2, n=conversions).rvs()
       non_wholesales = conversions - wholesales
       profit = (wholesales * 50 + non_wholesales * 60)
       return profit
   ```

2. Draw 10,000 samples from the distribution of profit, and plot a histogram. Does it look like any of the common distributions is a good fit for `profit`?

   ```python
   samples = [profit_rvs() for _ in range(10000)]
   plt.hist(samples, bins=30)
   plt.xlabel('Profit', fontsize=14, fontweight='bold')
   plt.ylabel('Freq.', fontsize=14, fontweight='bold')
   ```

   ![image](imgs/profit_hist.png)

3. Compute the range of values of profit where the middle 95% of the probability mass lies.

  ```python
  print '2.5% percentile', np.percentile(samples, 2.5)
  print '97.5% percentile', np.percentile(samples, 97.5)
  # 2.5% percentile 33730.0
  # 97.5% percentile 42830.0
  ```
