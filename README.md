regression-tests
================

3 VLANs
----------------
Topology (3\_vlans.xml):
```
                             switch
    VLAN10                  +------+                  VLAN10
    +-------------------+   |      |   +-------------------+
    |   VLAN20          |   |      |   |          VLAN20   |
    |   +-------------------+      +-------------------+   |
    |   |   VLAN30      |   |      |   |      VLAN30   |   |
    |   |   +-----------+   |      |   +-----------+   |   |
    |   |   |               +------+               |   |   |
    |   |   |                                      |   |   |
    +-------+                                      +-------+
        |                                              |
     +--+--+                                        +--+--+
+----+ eth +----+                              +----+ eth +----+
|    +-----+    |                              |    +-----+    |
|               |                              |               |
|               |                              |               |
|     host1     |                              |     host2     |
|               |                              |               |
|               |                              |               |
|               |                              |               |
+---------------+                              +---------------+
```

Description of topology:
2 hosts, each with one eth interface, which has 3 VLAN subinterfaces.

What is tested (3\_vlans.py):
1. Ping:
+ count: 100
+ interval: 0.1s
+ across interfaces in same VLAN (these should pass)
+ across interfaces in different VLANs (these should fail)
2. Netperf:
+ duration: 60s
+ TCP\_STREAM and UDP\_STREAM
+ across interfaces in same VLAN
3. Offloads:
+ TSO, GRO, GSO
+ tested both on/off variants

3 VLANs over bond
----------------
Topology (3\_vlans\_over\_active\_backup.xml and 3\_vlans\_over\_round\_robin.xml):
```
                                switch
       VLAN10                  +------+                  VLAN10
       +-------------------+   |      |   +-------------------+
       |   VLAN20          |   |      |   |          VLAN20   |
       |   +-------------------+      +-------------------+   |
       |   |   VLAN30      |   |      |   |      VLAN30   |   |
       |   |   +-----------+   |      |   +-----------+   |   |
       |   |   |               +------+               |   |   |
       |   |   |                                      |   |   |
       +-------+                                      +-------+
           |                                              |
           |                                              |
           |                                              |
      +----+---+                                     +----+---+
      |  BOND  |                                     |  BOND  |
      +---++---+                                     +---++---+
          ||                                             ||
       +--++--+                                       +--++--+
       |      |                                       |      |
    +--+-+  +-+--+                                 +--+-+  +-+--+
+---+eth1+--+eth2+---+                         +---+eth1+--+eth2+---+
|   +----+  +----+   |                         |   +----+  +----+   |
|                    |                         |                    |
|                    |                         |                    |
|       host1        |                         |       host2        |
|                    |                         |                    |
|                    |                         |                    |
|                    |                         |                    |
+--------------------+                         +--------------------+

```
Description of topology:
2 hosts, each with two eth interfaces, which are bonded. Bond has 3 VLAN
subinterfaces.

What is tested (3\_vlans.py):
1. Ping:
+ count: 100
+ interval: 0.1s
+ across interfaces in same VLAN (these should pass)
+ across interfaces in different VLANs (these should fail)
2. Netperf:
+ duration: 60s
+ TCP\_STREAM and UDP\_STREAM
+ across interfaces in same VLAN
3. Offloads:
+ TSO, GRO, GSO
+ tested both on/off variants

Active backup, Round robin
----------------
Topology (active\_backup.xml and round\_robin.xml):
```
                                switch
                               +------+
                               |      |
                               |      |
           +-------------------+      +------------------+
           |                   |      |                  |
           |                   |      |                  |
           |                   +------+                  |
           |                                             |
           |                                             |
           |                                             |
           |                                             |
           |                                             |
      +----+---+                                         |
      |  BOND  |                                         |
      +---++---+                                         |
          ||                                             |
       +--++--+                                          |
       |      |                                          |
    +--+-+  +-+--+                                     +-+--+
+---+eth1+--+eth2+---+                         +-------+eth1+------+
|   +----+  +----+   |                         |       +----+      |
|                    |                         |                   |
|                    |                         |                   |
|       host1        |                         |        host2      |
|                    |                         |                   |
|                    |                         |                   |
|                    |                         |                   |
+--------------------+                         +-------------------+

```
Description of topology:
2 hosts, one with 2 bonded eth interfaces, other one with one eth interface

What is tested (bonding\_test.py):
1. Ping:
+ count: 100
+ interval: 0.1s
+ from both sides
2. Netperf:
+ duration: 60s
+ TCP\_STREAM and UDP\_STREAM
+ from both sides
3. Offloads:
+ TSO, GRO, GSO
+ tested both on/off variants

Active backup double bond, Round robin double bond
----------------
```
                                switch
                               +------+
                               |      |
                               |      |
           +-------------------+      +-------------------+
           |                   |      |                   |
           |                   |      |                   |
           |                   +------+                   |
           |                                              |
           |                                              |
           |                                              |
           |                                              |
           |                                              |
      +----+---+                                     +----+---+
      |  BOND  |                                     |  BOND  |
      +---++---+                                     +---++---+
          ||                                             ||
       +--++--+                                       +--++--+
       |      |                                       |      |
    +--+-+  +-+--+                                 +--+-+  +-+--+
+---+eth1+--+eth2+---+                         +---+eth1+--+eth2+---+
|   +----+  +----+   |                         |   +----+  +----+   |
|                    |                         |                    |
|                    |                         |                    |
|       host1        |                         |       host2        |
|                    |                         |                    |
|                    |                         |                    |
|                    |                         |                    |
+--------------------+                         +--------------------+
```
Description of topology:
2 hosts each with two eth interfaces, which are bonded.

What is tested (bonding\_test.py):
1. Ping:
+ count: 100
+ interval: 0.1s
+ from both sides
2. Netperf:
+ duration: 60s
+ TCP\_STREAM and UDP\_STREAM
+ from both sides
3. Offloads:
+ TSO, GRO, GSO
+ tested both on/off variants
