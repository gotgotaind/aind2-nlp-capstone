conda create --name aind-nlp-capstone python=3.5 numpy
activate aind-nlp-capstone
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.2.1-cp35-cp35m-win_amd64.whl
conda install scipy
pip install keras -U
conda install jupyter