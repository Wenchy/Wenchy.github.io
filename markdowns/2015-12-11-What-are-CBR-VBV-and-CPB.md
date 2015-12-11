What are CBR, VBV and CPB?
=====================
Wenchy *2015-12-11*

> Original: [What are CBR, VBV and CPB?](https://codesequoia.wordpress.com/2010/04/19/what-are-cbr-vbv-and-cpb/)

It’s common mistake to to consider CBR (Constant Bit Rate) as “every frame is allocated the same number of bits”. If it were the case, then what would be the purpose of P or B frames? The whole purpose of P/B frame is to reduce the number of bits by referencing another frame. Of course, there are a lot of CBR streams with P or B frames. You can easily see every frame have very different number of bits even in a CBR stream.

So, what is CBR? In MPEG-2 and H.264, CBR means the number of bits fed to the decoder is constant over time. In other words, the data transfer rate to the decoder is constant. It’s nothing to do with the number of bits of individual frames.

Confused? How is it possible to allocate different number of bits to frames while keeping the incoming data rate constant?

Answer: you need a buffer. To understand the logic, consider a water outlet, a water tank, and a series of “picture decode guys” lined up in front of the tank.

![Video-buffer](https://wenchy.github.io/images/2015-12-11-Video-buffer.png)

The water (coded MPEG-2 or H.264 stream) is constantly flowing into the tank. The guys are lined up in front of the tank and remove the water for each frame to be decoded. The removal happens at the fixed time interval in most cases.

Even though Mr.I, P, and B are removing different amount of water (=each frame needs different number of bits), the water outlet speed is constant thanks to the tank (buffer).

In MPEG-2, the buffer is called VBV buffer (Video Buffer Verifier Buffer). In H.264, the buffer is called CPB (Coded Picture Buffer).

The water level of the tank at certain time instance is called buffer fullness and described in number of bits. The size of the tank is called VBV buffer size in MPEG-2 and CPB buffer size in H.264.

The coded stream must be constructed so that the tank (=buffer) never overflow or underflow. There are commercial/non-commercial software called “buffer verifier” to check the errors.

When the buffer size is set to large value (it’s an encoded stream parameter), the encoder can use large variance of bits for each frame which generally results in better video quality. However, the decoder needs to have the large buffer, which means more expensive hardware.

## Buffering delay and MPEG-2 Transport stream

> Original: [Buffering delay and MPEG-2 Transport stream](https://codesequoia.wordpress.com/2010/04/19/buffering-delay-and-mpeg-2-transport-stream/)

As we discussed in the previous post “What are CBR, VBV, and CPB?”, video decoder has a buffer to compensate the different coded size of each picture. Here is the actual example of the buffer occupancy of a MPEG-2 video stream at the beginning of the stream.

![VBV-buffer-fullness](https://wenchy.github.io/images/2015-12-11-VBV-buffer-fullness.png)

The first picture is decoded (= removed from the buffer) at the time zero. Before the decoding time, the coded stream has been entering into the buffer for more than 0.5 second.

The time interval between the entrance of the first byte of the coded picture and the decoding of the picture is called buffering delay. The delay is essentially the time between these two events.

- The STB starts to receive the coded picture.
- The STB decodes video frame.

The maximum buffering delay is caused when a picture is decoded when the buffer fullness is same as the buffer size. It means the buffer size and bit rate controls the maximum buffering delay.

** max_buffering_delay (second) = buffer_size (bytes) * 8 / bit_rate (bits/second) **

As we discussed, with a given bit rate, you could increase the video quality by increasing the buffer size. However, this trick has its own cost. It makes the STB more expensive and the buffering delay longer.

In the case of MPEG-2 video, the maximum buffering delay is almost always less than 0.7 second. However, in the case of H.264, it’s common to see very long delay such as 4 to 10 seconds especially for Web streaming context.

When multiplexing the video stream into transport stream, however, such long delay would cause a problem. While MPEG-2 TS standard allows up to 10 second delay for H.264 video, almost all STBs accepts up to 1 to 2 second. Therefore, if you want to construct the H.264 stream for transport stream broadcast purpose, you should restrict the CPB buffer size so that the buffer delay is less than one second.