# low_res_logos_gan
DC GAN for low resolution logo generation

Attached notebook contains an implementation (tensorflow 2.2.0) of vanilla/least squares DC GAN for generating
low resolution logos.

# Geberated examples:

![Generated Logos](https://github.com/nslyubaykin/low_res_logos_gan/blob/master/gen_examples.png)

Training data contains 12180 images parsed from the web. For the purpose of GAN training data was
augumented with random spins, flips and hue adjustments.

# Training dynamics:

![Epoch-1](https://github.com/nslyubaykin/low_res_logos_gan/blob/master/training_progress_imgs/index.png)

![Epoch-50](https://github.com/nslyubaykin/low_res_logos_gan/blob/master/training_progress_imgs/ep50.png)

![Epoch-130](https://github.com/nslyubaykin/low_res_logos_gan/blob/master/training_progress_imgs/ep130.png)

![Epoch-200](https://github.com/nslyubaykin/low_res_logos_gan/blob/master/training_progress_imgs/ep200.png)

![Epoch-300](https://github.com/nslyubaykin/low_res_logos_gan/blob/master/training_progress_imgs/ep300.png)

![Epoch-500](https://github.com/nslyubaykin/low_res_logos_gan/blob/master/training_progress_imgs/ep500.png)
