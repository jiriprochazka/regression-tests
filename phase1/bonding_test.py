from lnst.Controller.Task import ctl

# ------
# SETUP
# ------

m1 = ctl.get_host("testmachine1")
m2 = ctl.get_host("testmachine2")

m1.sync_resources(modules=["IcmpPing", "Netperf"])
m2.sync_resources(modules=["IcmpPing", "Netperf"])

m1_ip = m1.get_ip("test_bond")
m2_ip = m2.get_ip("eth1")

# ------
# TESTS
# ------

ping_mod = ctl.get_module("IcmpPing",
                           options={
                               "addr" : m2_ip,
                               "count" : 10,
                               "iface" : m1.get_devname("test_bond"),
                               "interval" : 0.1
                           })

netperf_srv = ctl.get_module("Netperf",
                              options = {
                                  "role" : "server",
                                  "bind" : m1_ip
                              })

netperf_cli_tcp = ctl.get_module("Netperf",
                                  options = {
                                      "role" : "client",
                                      "netperf_server" : m1_ip,
                                      "duration" : 5,
                                      "testname" : "TCP_STREAM",
                                      "netperf_opts" : "-L %s" % m2_ip
                                })

netperf_cli_udp = ctl.get_module("Netperf",
                                  options = {
                                      "role" : "client",
                                      "netperf_server" : m1_ip,
                                      "duration" : 5,
                                      "testname" : "UDP_STREAM",
                                      "netperf_opts" : "-L %s" % m2_ip
                                  })

m1.run(ping_mod)
server_proc = m1.run(netperf_srv, bg=True)
ctl.wait(1)
m2.run(netperf_cli_tcp)
m2.run(netperf_cli_udp)
server_proc.intr()

ping_mod = ctl.get_module("IcmpPing",
                           options={
                               "addr" : m1_ip,
                               "count" : 10,
                               "iface" : m2.get_devname("eth1"),
                               "interval" : 0.1
                           })


netperf_srv = ctl.get_module("Netperf",
                              options = {
                                  "role" : "server",
                                  "bind" : m2_ip
                              })

netperf_cli_tcp = ctl.get_module("Netperf",
                                  options = {
                                      "role" : "client",
                                      "netperf_server" : m2_ip,
                                      "duration" : 5,
                                      "testname" : "TCP_STREAM",
                                      "netperf_opts" : "-L %s" % m1_ip
                                  })

netperf_cli_udp = ctl.get_module("Netperf",
                                  options = {
                                      "role" : "client",
                                      "netperf_server" : m2_ip,
                                      "duration" : 5,
                                      "testname" : "UDP_STREAM",
                                      "netperf_opts" : "-L %s" % m1_ip
                                  })

m2.run(ping_mod)
server_proc = m2.run(netperf_srv, bg=True)
ctl.wait(1)
m1.run(netperf_cli_tcp)
m1.run(netperf_cli_udp)
server_proc.intr()
