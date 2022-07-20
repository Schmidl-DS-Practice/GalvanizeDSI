# Xgboost Install Instructions for Mac

This takes a long time so please don't do this during classtime.

Using [these instructions](https://www.ibm.com/developerworks/community/blogs/jfp/entry/Installing_XGBoost_on_Mac_OSX?lang=en).

**NOTE**: Some of these instructions are assuming that `brew` is installing `gcc` version 6.  If this is not the case you will need to alter how you change the `config.mk` file!


1. Install gcc with open mp (**NOTE**: This can take a long time!  )

```bash
$ brew install gcc --without-multilib
```

**NOTE**: If you have a conflicting version of `gcc` installed through Homebrew, you may need to uninstall that by running `brew unlink gcc` first.

2. Clone down the Xgboost library into a particular folder, say `<directory>`:

```bash
$ cd <directory>
$ git clone --recursive https://github.com/dmlc/xgboost
```

3. We now need to build the Xgboost package.  `cd` into the Xgboost repo and copy the `make/config.mk` file by running:

```bash
$ cp make/config.mk .
```

4. Now alter the `<directory>/xgboost/config.mk` file and uncomment the following lines:

```
export CC = gcc-6
export CXX = g++-6
```

5. Now we can build with the following commands (`make -j4` tells the compiler to use 4 cores):

```bash
$ cd <directory>/xgboost
$ make -j4
```

6. Now install the python package by running the following command:

```bash
$ cd python-package; sudo python setup.py install
```

Once you have completed this run the following import to verify that you have installed it successfully:

```python
import xgboost as xgb

model = xgb.XGBClassifier()
```

---

Check out [this tutorial](http://bit.ly/2jidAj9) for a breakdown of some of the hyperparameters we can tune when building an xgboost model.
