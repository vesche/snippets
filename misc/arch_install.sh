#
# This isn't intended to be run, it's a loose guide of how I install arch
# from a live boot. Might also be of use to someone else. Enjoy, vesche.
#

################
# live install #
################

# update the system clock
timedatectl set-ntp true

# identify hard drive
lsblk

# partion
parted /dev/sdX
    (parted) mklabel msdos
    (parted) mkpart primary ext4 1MiB 100%
    (parted) set 1 boot on
    (parted) quit

# format fs & mount
lsblk /dev/sdX
mkfs.ext4 /dev/sdXY
mount /dev/sdXY /mnt

# install base
pacstrap -i /mnt base base-devel

# generate fstab
genfstab -U /mnt > /mnt/etc/fstab

# chroot
arch-chroot /mnt /bin/bash

# locale
vi /etc/locale.gen # uncomment: en_US.UTF-8 UTF-8
locale-gen

# set timezone
ln -s /usr/share/zoneinfo/America/New_York /etc/localtime
hwclock --systohc --utc

# ramdisk
mkinitcpio -p linux

# bootloader
pacman -S grub os-prober
grub-install --recheck /dev/sdx
grub-mkconfig -o /boot/grub/grub.cfg

# set hostname
echo 'hostname' > /etc/hostname

# set root password
passwd

# reboot
exit
umount -R /mnt
reboot

################
# post install #
################

# create user
useradd -m -G wheel -s /bin/bash user
passwd user

# uncomment wheel group
visudo

# leave root
exit

# dhcp
sudo systemctl enable dhcpcd@eno1.service
sudo systemctl start dhcpcd@eno1.service

# ssh
sudo pacman -S openssh
sudo vi /etc/ssh/sshd_config # change a few things
sudo systemctl enable sshd
sudo systemctl start sshd

# package spam
sudo pacman -S vim wget git net-tools nmap htop nitrogen profont python \
    ranger tcpdump tcpreplay scrot screenfetch unzip unrar tree tmux cmus \
    xf86-video-intel xorg-server xorg-xinit xorg-xrandr bspwm sxhkd \
    dmenu firefox vlc wireshark-cli wireshark-qt mupdf p7zip \
    pulseaudio deluge gvbam i3lock python-pip startup-notification \
    rxvt-unicode-terminfo rsync gconf gtk2 streamlink libxss

# audio
pulseaudio --start

# urxvt (terminal)
mkdir ~/aur
cd ~/aur
wget https://aur.archlinux.org/cgit/aur.git/snapshot/rxvt-unicode-patched.tar.gz
tar xzvf rxvt-unicode-patched.tar.gz
cd rxvt-unicode-patched
makepkg
sudo pacman -U rxvt-unicode-patched-*.pkg.tar.xz

# dotfiles
mkdir ~/code
cd ~/code
git clone https://github.com/vesche/dotfiles
cp dotfiles/{.Xresources, .bashrc, .vimrc, .xinitrc} ~/
cp -r dotfiles/.config ~/

# let's go
startx

# ~~~ additional stuff ~~~

# aur packages
# spotify, megasync, discord, vscode, streamlink-gui

# firefox add-ons: imagus, ublock, stylish
# stylish themes: github, hacker news, reddit, stackoverflow, wikipedia
