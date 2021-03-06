'''

Discriminator model architecture which is essentially a Convolutional Neural Network (CNN).

'''


import torch

class Discriminator(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.network = torch.nn.Sequential(
            torch.nn.Conv2d(3, 32, 4, 2, 1),
            torch.nn.BatchNorm2d(32),
            torch.nn.LeakyReLU(0.2),
            torch.nn.Conv2d(32, 64, 4, 2, 1),
            torch.nn.BatchNorm2d(64),
            torch.nn.LeakyReLU(0.2),
            torch.nn.Conv2d(64, 128, 4, 2, 1),
            torch.nn.BatchNorm2d(128),
            torch.nn.LeakyReLU(0.2),
            torch.nn.Conv2d(128, 256, 4, 2, 1),
            torch.nn.BatchNorm2d(256),
            torch.nn.LeakyReLU(0.2),
            torch.nn.Conv2d(256, 1, 2, 1, 0)
        )
    
    def forward(self, inp):
        return self.network(inp)[:,:, 0, 0]

discriminator = Discriminator()
print(discriminator(torch.rand(64, 3, 32, 32)).size())