How to get Ubuntu back after installing Windows?
=====================
Wenchy *2015-12-29*

> Original: [How can I repair grub?](http://askubuntu.com/questions/88384/how-can-i-repair-grub-how-to-get-ubuntu-back-after-installing-windows)

## Solution 0

The Windows installer doesn't care about other OS in the system. So it writes own code over the master boot record. Fortunately the solution is easy too.

You need to repair the MBR. Do the following

Boot using a live usb/cd of ubuntu. Use **boot-repair** to fix the problem.

After booting with live usb/cd, run following command in terminal:

``` shell
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo apt-get update
sudo apt-get install -y boot-repair
boot-repair
```

Use **Recomended Repair**.

Ref - [Boot-Repair](https://help.ubuntu.com/community/Boot-Repair)

## Solution 1

When you install Windows, Windows assumes it is the only operating system (OS) on the machine, or at least it does not account for Linux. So it replaces GRUB with its own boot loader. What you have to do is replace the Windows boot loader with GRUB. I've seen various instructions for replacing GRUB by mucking around with GRUB commands or some such, but to me the easiest way is to simply chroot into your install and run update-grub. chroot is great because it allows you to work on your actual install, instead of trying to redirect things here and there. It is really clean.

Here's how:

1. Boot from the live CD or live USB, in "Try Ubuntu" mode.
2. Determine the partition number of your main partition. GParted (which should already be installed, by default, on the live session) can help you here. I'm going to assume in this answer that it's `/dev/sda2`, but make sure you use the correct partition number for your system!
3. Mount your partition: 

``` shell
sudo mount /dev/sda2 /mnt  #Replace sda2 with your partition number
```

4. Bind mount some other necessary stuff:

``` shell
for i in /sys /proc /run /dev; do sudo mount --bind "$i" "/mnt$i"; done
```

5. `chroot` into your Ubuntu install:

``` shell
sudo chroot /mnt
```

6. At this point, you're in your install, not the live session, and running as root. Update grub:

``` shell
update-grub
```

If you get errors, go to step 7. (Otherwise, it is optional.)

7. Depending on your situation, you might have to reinstall grub:

``` shell
grub-install /dev/sda
update-grub # I'm not sure if this is necessary, but it doesn't hurt.
```

8. If everything worked without errors, then you're all set:

``` shell
exit
sudo reboot
```

10. At this point, you should be able to boot normally.

If you cannot boot normally, and didn't do step 7 because there were no error messages, try again with step 7.

> Sometimes giving GRUB2 the correct configuration for your partitions is not enough, and you must actually install it (or reinstall it) to the Master Boot Record, which step 7 does. Experience helping users in chat has shown that step 7 is sometimes necessary even when no error messages are shown.
