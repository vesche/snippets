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
locale-gen
echo 'LANG=en_US.UTF-8' > /etc/locale.conf

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

# package spam
sudo pacman -S \
cmus feh gcc git nano net-tools nitrogen nmap htop openssh profont ranger \
rtorrent screenfetch scrot tcpdump tcpreplay tree tmux unzip vim weechat wget \
yajl youtube-dl \
python python-pip python-setuptools python2 python2-pip python2-setuptools \
dmenu firefox livestreamer vlc wireshark-cli wireshark-qt \
xf86-video-intel xorg-server xorg-xinit xorg-xrandr bspwm sxhkd dmenu \
rxvt-unicode \

# yaourt
mkdir -p ~/tmp/AUR && cd $_
wget https://aur.archlinux.org/cgit/aur.git/snapshot/package-query.tar.gz
tar xfz package-query.tar.gz  # unpack tarball
cd package-query  &&  makepkg  # cd and create package from source
sudo pacman -U package-query*.pkg.tar.xz
cd ~/tmp/AUR
wget https://aur.archlinux.org/cgit/aur.git/snapshot/yaourt.tar.gz
tar xzf yaourt.tar.gz
cd yaourt && makepkg
sudo pacman -U yaourt*.pkg.tar.xz

# AUR
yaourt -S atom-editor lemonbar-git spotify

# dotfiles
git clone https://github.com/vesche/dotfiles
cp dotfiles/{.Xresources, .bar.py, .bash_profile, .bashrc, .vimrc, .xinitrc} ~/
cp -R dotfiles/.config ~/

# firefox add-ons: imagus, ublock, stylish
# stylish themes: github, hacker news, reddit, stackoverflow, wikipedia
