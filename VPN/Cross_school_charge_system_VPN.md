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
- Tecent cloud
    + software use different way to connect with outside
    + why it don't function for chrome, maybe its netspeed is slow or security protocol
## successfully build my VPN to avoid surffing the internet
- software and browser use different port to get information
- why tencent server is not allowed to be a VPN
- WHY THUNDER USE IE PROXY to get no download data but dictionary get data
- different symbol of connection state
## speed test(Ping from Wuhan)

VPN | down(Mbps) | up(Mbps) | bandwidth
: | : | : | :
none | 70.09 | 88.58 | unknown
tencent cloud | 0.32 | 34.38 | 1M
mingde server | 97.76 | 158.68 | 1000M
HK VPN | 44.85 | 139.83 | unknown
JP VPN | 43.88 | 87.94 | unknown
4G hotpoint(Yidong) | 21.41 | 10.05 | unknown
