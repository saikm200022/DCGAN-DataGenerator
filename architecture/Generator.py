'''

Generator Model Architecture - Generates Images with latent vector input. Comprised of up convolutions.

'''

import torch

class Generator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.network = torch.nn.Sequential(
            torch.nn.ConvTranspose2d(100, 64 * 8, 4, 1, 0),
            torch.nn.BatchNorm2d(64 * 8),
            torch.nn.LeakyReLU(0.2),
            torch.nn.ConvTranspose2d(64 * 8, 64 * 4, 4, 2, 1),
            torch.nn.BatchNorm2d(64 * 4),
            torch.nn.LeakyReLU(0.2),
            torch.nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1),
            torch.nn.BatchNorm2d(64 * 2),
            torch.nn.LeakyReLU(0.2),
            torch.nn.ConvTranspose2d(64 * 2, 64, 4, 2, 1),
            torch.nn.BatchNorm2d(64),
            torch.nn.LeakyReLU(0.2),
            torch.nn.ConvTranspose2d(64, 3, 5, 1, 2),
            torch.nn.Tanh()
        )
        

    def forward(self, im):
        return self.network(im)

generator = Generator()
print(generator(torch.rand(64, 100, 1, 1)).size())