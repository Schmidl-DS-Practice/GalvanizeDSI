## More Map Reduce practice

We'll be using the same 20 newsgroups data from [data-at-scale](https://github.com/zipfian/data-at-scale/blob/master/individual.md).

In the interest of time and quick testing, just run your job on one of the topics that has a few files in it.

1. Write a MRJob program to get the average word length for each filename. You can just use the filename as the key, which is something like 54056.

    Start by writing a version *without* using a combiner.

    When you're taking the average, try to do the calculationg without converting your generator into a list.

2. Now see if you can add the combiner. Your combiner in this case will be different from your reducer!

    To do this, you'll need to have your combiner yield two values (which you can do by putting them in a tuple).
