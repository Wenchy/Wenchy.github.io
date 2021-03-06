CRF Guide
=====================
Wenchy *2015-06-08*

> Original: [CRF Guide](http://slhck.info/articles/crf)

CRF stands for Constant Rate Factor, x264’s best single-pass encoding method.

## Quick Summary: What is the Constant Rate Factor?
The Constant Rate Factor (CRF) is the default quality setting for the x264 encoder. You can set the values between 0 and 51, where lower values would result in better quality (at the expense of higher file sizes). Sane values are between 18 and 28. The default for x264 is 23, so you can use this as a starting point.

With `ffmpeg`, it'd look like this:

``` shell
ffmpeg -i input.mp4 -c:v libx264 -crf 23 output.mp4
```

If you're unsure about what CRF to use, begin with 23 and change it according to your subjective impression of the output. Is the quality good enough? No? Then set a lower CRF. Is the file size too high? Choose a higher CRF. A change of ±6 should result in about half/double the file size, although your results might vary.

![Video-coding-order](https://wenchy.github.io/images/2015-06-08-crf.png)

## CRF in a nutshell
The way constant quality encoding is usually done, it keeps up a constant quality by compressing every frame of the same type the same amount. In tech speak, that’s maintaining a constant QP (quantization parameter). The quantization parameter defines how much information to “throw away” from a given block of pixels.

Constant Rate Factor, on the other hand, will compress different frames by different amounts. It does this by taking motion into account.

The eye perceives more detail in still objects than when they’re in motion. Because of this, a video compressor can apply more compression (drop more detail) when things are moving, and apply less compression (retain more detail) when things are still. Subjectively, the video will seem to have higher quality.

## How to use it
If you’re using x264, CRF is used by default for constant quality.

But isn’t that other way, constant QP, really better quality in the end?

No. It just wastes space by compressing less in areas you really won’t notice. This isn’t even like MP3s cutting off highs and lows in music that are audible on CDs. There is not a purist’s argument to made here.

If you were a computer, you would look at a CRF encoding and say it was lower quality than the CQP copy. And it would be. But if you’re a human being, subjectively, the CRF copy will look better. It least compresses the parts you see the most, and most compresses the parts you see the least.

Many people always use CRF for single-pass encodes and argue there is no reason to ever use CQP.

## Slightly more technical explanation
A constant QP encode at Q=18 will stay at Q=18 regardless of the frame. Constant Rate Factor will increase the Q to, say, 20, for high motion frames (compressing them more) and lower it down to 16 for low motion. That means that while the average quality as objectively gauged by PSNR goes slightly down, the perceptible image quality goes up.

When you use a constant rate factor, it varies the QP slightly. When a scene has a lot of action and motion, it will raise the QP (compressing more). This is because your eye will be distracted by everything going on, and won’t have the image on screen for enough time to see the heavier compression. When a frame doesn’t have a lot of motion, it will lower the QP, compressing it less. This is because your eye will have more time to look at the image, so you want it to be as much like the source as possible.

CRF is about improving subjective quality—what the human eye sees—at the expense of objective quality—what a PSNR calculation sees. There is no way for anyone to tell you what your eye will notice on any given film.

## If quality goes down in motion, does that mean it gets all blocky like my digital TV?
CRF is not the cause of the blocking you might see on digital cable/sat broadcasts. That derives from too low of a bitrate.

Different bitrates correspond to different compression rate factors with different sources. So 1,500 kBit/s will be enough to get an RF of 15 with one source, but only an RF of 20 with another, dirtier source. When you use CRF or CQP you’re saying “use whatever bitrate is necessary to preserve this much detail.” It’s not a 1-to-1 thing.

Those TV broadcasts get blocky because the complex things they’re displaying require more bits than the broadcaster has chosen to give them. They say “preserve as much detail as you can while never going above this high a bitrate no matter how complicated things get.”

## But still…isn’t lower quality bad?
When you use CRF, it raises the QP (compressing more, losing more detail) for complex parts, yes. But it doesn’t raise it drastically, and it makes sure those complex parts still maintain a set quality level. Just a level a little lower than the simple parts. The bitrate for those parts might still be higher than for the simple parts, because the bitrate needed at a given moment to reach a given rate factor fluctuates. You can go to a lower RF for the simple parts while still keeping a bitrate similar to what you need for the complex parts at a higher RF.

If you use a CRF of 25, sure, you’re going to see blocking on high-motion because the bitrate is simply too low. It’s going to be using a QP of, like, 27 for the complex parts, which is way too heavy a quantizer. And it’ll only use, say, 23 for the simple parts, which isn’t quite low enough to drastically increase quality. But if you use reasonable CRF values, in the range of, say, 23-17, this won’t occur.

> Note:  Parts of this guide were copied from the Handbrake Wiki but has been deleted there. It also shortly appeared on Wikipedia but was removed because it only relied on one source—the Handbrake Wiki. This is an attempt to recover the information, adding a bit here and there. I don't know if there's an original copyright on the content or not. If so, please let me know.
