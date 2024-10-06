from d2l import torch as d2l
import torch
from torch import nn
class LinearRegression(d2l.Module):
    def __init__(self, lr):
        super().__init__()
        self.save_hyperparameters()
        self.net = nn.LazyLinear(1)
        self.net.weight.data.normal_(0, 0.1)
        self.net.bias.data.fill_(0.)

#define forward pred        
@d2l.add_to_class(LinearRegression)
def forward(self, X):
    return self.net(X)

#def loss
@d2l.add_to_class(LinearRegression)
def loss(self, y_hat, y):
    return nn.MSELoss()(y_hat, y) #in pytorch, nn.MSELoss is a class; nn.MSELoss() is the fun


#def optim
@d2l.add_to_class(LinearRegression)
def configure_optimizers(self):
    return torch.optim.SGD(self.parameters(), self.lr)

#def training
model = LinearRegression(lr=0.03)
data = d2l.SyntheticRegressionData(w=torch.tensor([2, -3.4]), b=4.2)
trainer = d2l.Trainer(max_epochs=3)
trainer.fit(model, data)