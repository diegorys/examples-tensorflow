#Requeriments pip: pybrain, scipy

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(2, 1)
 
ds.addSample((0,0), (0))
ds.addSample((0,1), (1))
ds.addSample((1,0), (1))
ds.addSample((1,1), (0))
ds.addSample((0,0), (0))
ds.addSample((0,1), (1))
ds.addSample((1,0), (1))
ds.addSample((1,1), (0))
ds.addSample((0,0), (0))
ds.addSample((0,1), (1))
ds.addSample((1,0), (1))
ds.addSample((1,1), (0))
ds.addSample((0,0), (0))
ds.addSample((0,1), (1))
ds.addSample((1,0), (1))
ds.addSample((1,1), (0))


red_neuronal = buildNetwork(2, 4, 1, bias=True)
entrenador = BackpropTrainer(red_neuronal, ds, learningrate = 0.01, momentum = 0.99)
print ("Training, please wait...")
entrenador.trainUntilConvergence(maxEpochs=10000, verbose=False, validationProportion=0.5)
print ("Training finished!")
print '(0,0) :', red_neuronal.activate([0,0])
print '(0,1) :', red_neuronal.activate([0,1])
print '(1,0) :', red_neuronal.activate([1,0])
print '(1,1) :', red_neuronal.activate([1,1])