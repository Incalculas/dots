#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}



lxsession &
xclip &
run nm-applet &
#blueman-applet &
numlockx on &
flameshot &
picom --config .config/picom/picom-blur.conf --experimental-backends &
dunst &
nitrogen --restore &
