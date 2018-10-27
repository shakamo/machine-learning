# machine-learning 

* Python3の勉強も兼ねて、機械学習の勉強のために作成

keras + Boosting系のモデルを利用して開発（途中）。


brew install pyenv
pyenv install anaconda3-5.2.0
pyenv global anaconda3-5.2.0

vi ~/.bash_profile
export PATH="$HOME/.pyenv/shims:$PATH"
source ~/.bash_profile

conda update scipy
pip install u-msgpack-python
pip install GPy

brew install gcc5
brew install gcc@5
pip install xgboost

git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; cp make/minimum.mk ./config.mk; make -j4
cd python-package
python setup.py install

pip install plotly
pip install joblib
brew install ta-lib
pip install TA-Lib


