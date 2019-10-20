# Constucting VPN
## UTILS
- shadowsocks
- serverspeeder
## Problems
- network speed is a little bit slow
- when using thunder or Baidu network disk, the server could get data.
    + Chrome
    + the server problem
## to do list
- 443 port failed
    + learn ping (check: no loss, maybe the rounter cause the problems)
    + find IP address
    + server hosts resolution
- try ubuntu availablity for serverspeed
    + if yes, do next
    + if not, find speed application and try again (maybe learn shadowsocks is good)
- testing data transfer limit
    + other browsers (check, chrome has a good workflow
    + ubuntu to get data from this website, why is on forbid list
        * thunder problem
        * or school options for
- to show the shadowsocks connection state
## experiment
- when using go.connect its speed is well, maybe server speed is not well for outside network. maybe I can buy a treeberry linux to make a VPN to place in the lab.
- maybe server download using apt-get is high-speed, but it perform bad in simple cn-net.
    + download: 46.78 Mbit/s
    + upload: 14.56 Mbit/s
- key problem: serverspeed
    + can connect but time failed
    + speed urge different kernel
- linux kernel change:
    + linux-image-4.15.0-29-generic         install
    + max ubuntu 3 - -generic
- get familiar with shadowsockets
    + info user connect
    + info data transfer
    + learn about something about ipv6