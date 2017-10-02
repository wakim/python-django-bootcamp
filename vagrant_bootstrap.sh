#!/bin/bash

# Install miniconda
echo 'Installing and configuring conda...'

miniconda=Miniconda3-latest-Linux-x86_64.sh

mkdir ~vagrant/
cd /vagrant

if [[ ! -f $miniconda ]]; then
    wget --quiet http://repo.continuum.io/miniconda/$miniconda
fi

chmod +x $miniconda

./$miniconda -b -p /opt/anaconda

cat >> /home/vagrant/.bashrc << END
# add for anaconda install
PATH=/opt/anaconda/bin:$PATH

echo 'Create conda environment'

conda env create -f django_course.yml

# Some useful aliases for getting started, MotD
echo 'Setting up message of the day, and some aliases...'

printf "\nUseful Aliases:\n" >> ~vagrant/.bashrc
printf "alias menu='cat /etc/motd'\n" >> ~vagrant/.bashrc
printf "alias runserver='python manage.py runserver 0.0.0.0:8000'\n" >> ~vagrant/.bashrc
printf "alias ccat='pygmentize -O style=monokai -f terminal -g'\n" >> ~vagrant/.bashrc

# Complete
echo ""
echo "Vagrant install complete."
echo "Now try logging in:"
echo "    $ vagrant ssh"
