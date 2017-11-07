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

# ssh
sudo systemctl enable sshd
sudo systemctl start sshd

# package spam
sudo pacman -S \
cmus feh gcc git nano net-tools nitrogen nmap htop openssh profont ranger \
rtorrent screenfetch scrot tcpdump tcpreplay tree tmux unzip vim weechat wget \
yajl youtube-dl \
python python-pip python-setuptools python2 python2-pip python2-setuptools \
dmenu firefox livestreamer vlc wireshark-cli wireshark-qt \
xf86-video-intel xorg-server xorg-xinit xorg-xrandr bspwm sxhkd \
rxvt-unicode w3m unrar qt4 mupdf p7zip pcmanfs gvbam ntp cheese deluge \
i3lock-blur megasync steam pulseaudio redshift

# yaourt (if you wanna be a noob)
# mkdir -p ~/tmp/AUR && cd $_
# wget https://aur.archlinux.org/cgit/aur.git/snapshot/package-query.tar.gz
# tar xfz package-query.tar.gz  # unpack tarball
# cd package-query  &&  makepkg  # cd and create package from source
# sudo pacman -U package-query*.pkg.tar.xz
# cd ~/tmp/AUR
# wget https://aur.archlinux.org/cgit/aur.git/snapshot/yaourt.tar.gz
# tar xzf yaourt.tar.gz
# cd yaourt && makepkg
# sudo pacman -U yaourt*.pkg.tar.xz

# pip spam
sudo pip install psutil livestreamer requests pygments

# AUR
mkdir -p ~/tmp/AUR
pushd ~/tmp/AUR

# lemonbar-git
wget https://aur.archlinux.org/cgit/aur.git/snapshot/lemonbar-git.tar.gz
tar xfz lemonbar-git.tar.gz
pushd lemonbar-git
makepkg
sudo pacman -U lemonar-git*.pkg.tar.xz
popd

# atom
wget https://aur.archlinux.org/cgit/aur.git/snapshot/atom-editor.tar.gz
tar xfz atom-editor.tar.gz
pushd atom-editor
makepkg
sudo pacman -U atom-edutor*.pkg.tar.xz
popd

# spotify
wget https://aur.archlinux.org/cgit/aur.git/snapshot/spotify.tar.gz
tar xfz spotify.tar.gz
pushd spotify
makepkg
sudo pacman -U spotify*.pkg.tar.xz
popd

# slack
wget https://aur.archlinux.org/cgit/aur.git/snapshot/slack-desktop.tar.gz
tar xfz slack-desktop.tar.gz
pushd slack-desktop
makepkg
sudo pacman -U slack-desktop*.pkg.tar.xz
popd

# megasync
wget https://aur.archlinux.org/cgit/aur.git/snapshot/megasync.tar.gz
tar xfz megasync.tar.gz
pushd megasync
makepkg
sudo pacman -U megasync*.pkg.tar.xz
popd

# end AUR
popd

# dotfiles
git clone https://github.com/vesche/dotfiles
cp dotfiles/{.Xresources, .bar.py, .bash_profile, .bashrc, .vimrc, .xinitrc} ~/
cp -R dotfiles/.config ~/

# firefox add-ons: imagus, ublock, stylish
# stylish themes: github, hacker news, reddit, stackoverflow, wikipedia
