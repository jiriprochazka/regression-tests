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
        + TCP_STREAM and UDP_STREAM
        + across interfaces in same VLAN
    3. Offloads:
        + TSO, GRO, GSO
        + tested both on/off variants
