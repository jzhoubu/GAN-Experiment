# GAN Experiment

### Update

- **19/02/14**: Add GAN/CGAN/DCGAN experiment
- **19/04/17**: Start research on GAN on NLP



### GAN on NLP

1. **Famous Work**
   - SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient  (2017@AAAI)
   - MaskGAN: Better Text Generation via Filling in the______ (2018@ICLR)
2. **Challenge**
   - SeqGAN指出了两点challenge：
     - 1）词向量是离散的token，generator生成的embedding未必有与之对应的词语
     - 2）discriminator只适合对entire sequence进行评分







### Experiment

#### GAN 
- Paper: [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)
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


#### Conditional GAN
- Paper: [Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784)
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


#### Deep Convolutional GAN 
- Paper: [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434)
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
- [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)
- [Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784)
- [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434)
- [Improved Techniques for Training GANs](http://papers.nips.cc/paper/6125-improved-techniques-for-training-gans.pdf)
- [InfoGAN: Interpretable Representation Learning by Information Maximizing Generative Adversarial Nets](http://papers.nips.cc/paper/6399-infogan-interpretable-representation-learning-by-information-maximizing-generative-adversarial-nets.pdf)
- [f-GAN: Training Generative Neural Samplers using Variational Divergence Minimization](http://papers.nips.cc/paper/6066-f-gan-training-generative-neural-samplers-using-variational-divergence-minimization.pdf)
- [Improved Training of Wasserstein GANs](http://papers.nips.cc/paper/7159-improved-training-of-wasserstein-gans.pdf)
- [StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation](http://openaccess.thecvf.com/content_cvpr_2018/papers/Choi_StarGAN_Unified_Generative_CVPR_2018_paper.pdf)