# GAN Experiment

## Experiment

#### GAN [[Paper]](https://arxiv.org/abs/1406.2661)
- Notebook: `0211_GAN_MINST.ipynb`
- Dataset: MNIST from `tf.keras`
- Training time: 270s
- Paramters:
    + epochs: 3000
    + batch_size: 32
    + save_interval: 200
- Size:
    + Generator: 5974080B
    + Discriminator: 2134020B
- Result: [Visualization](https://sysu-zjw.github.io/GAN-Experiment/html/0211_GAN_MNIST/)


#### Conditional GAN [[Paper]](https://arxiv.org/abs/1411.1784)
- Notebook: `0211_CGAN_MINST.ipynb`
- Dataset: MNIST from `tf.keras`
- Training time: 392s
- Paramters:
    + epochs: 3000
    + batch_size: 32
    + save_interval: 200
- Size:
    + Generator: 5978080B
    + Discriminator: 3742340B
- Result: [Visualization](https://sysu-zjw.github.io/GAN-Experiment/html/0211_CGAN_MNIST/)


#### Deep Convolutional GAN [[Paper]](https://arxiv.org/abs/1511.06434)
- Notebook: `0212_DCGAN_MINST.ipynb`
- Dataset: MNIST from `tf.keras`
- Training time: 1503s
- Paramters:
    + epochs: 300
    + batch_size: 32
    + save_interval: 20
- Size:
    + Generator: 3424772B
    + Discriminator: 1574916B
- Result: [Visualization](https://sysu-zjw.github.io/GAN-Experiment/html/0212_DCGAN_MNIST/)





## Related Work
- [**The GAN Zoo**](https://github.com/hindupuravinash/the-gan-zoo) provides paper list of GAN.
- [**ganhacks**](https://github.com/soumith/ganhacks) introduces tips and tricks to make GANs work.
- [**Keras-GAN**](https://github.com/eriklindernoren/Keras-GAN) lists most keras implementations of GAN.
