from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSKernelSwitch, RemoteController
from datetime import datetime
from random import choice, randrange
from time import sleep

class MassiveTreeTopo(Topo):
    def build(self):
        n_core, n_agg, n_acc, n_hosts = 2, 2, 4, 8

        cores = [self.addSwitch(f's{i+1}', cls=OVSKernelSwitch, protocols='OpenFlow13') 
                 for i in range(n_core)]

        aggs = []
        for core in cores:
            for _ in range(n_agg):
                agg_id = len(aggs) + n_core + 1
                agg = self.addSwitch(f's{agg_id}', cls=OVSKernelSwitch, protocols='OpenFlow13')
                aggs.append(agg)
                self.addLink(core, agg)

        accs = []
        h_id = 1
        for agg in aggs:
            for _ in range(n_acc):
                acc_id = len(accs) + n_core + len(aggs) + 1
                acc = self.addSwitch(f's{acc_id}', cls=OVSKernelSwitch, protocols='OpenFlow13')
                accs.append(acc)
                self.addLink(agg, acc)

                for _ in range(n_hosts):
                    host = self.addHost(f'h{h_id}', mac=f"00:00:00:00:00:{h_id:02x}",
                                        ip=f"10.0.0.{h_id}/24", cpu=1.0 / (n_hosts * len(accs)))
                    self.addLink(acc, host)
                    h_id += 1

def ip_generator():
    """Generates random IPs in the range of available hosts."""
    return f"10.0.0.{randrange(1, 129)}"

if __name__ == '__main__':
    
    start_time = datetime.now()
    
    setLogLevel('info')
    print("Starting Fat-Tree Network...")
    
    topo = MassiveTreeTopo()
    c0 = RemoteController('c0', ip='192.168.0.101', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=c0)
    
    net.start()
    
    hosts = [net.get(f'h{i+1}') for i in range(128)]  

    print("--------------------------------------------------------------------------------")    
    print("Generating traffic ...")    
    h1 = hosts[0] 
    
    h1.cmd('cd /home/mininet/webserver')
    h1.cmd('python -m SimpleHTTPServer 80 &')
    h1.cmd('iperf -s -p 5050 &')
    h1.cmd('iperf -s -u -p 5051 &')
    
    sleep(2)

    for h in hosts:
        h.cmd('cd /home/mininet/Downloads')

    for i in range(600): 
        print("--------------------------------------------------------------------------------")    
        print(f"Iteration {i+1} ...")
        print("--------------------------------------------------------------------------------") 

        for _ in range(10):
            src = choice(hosts) 
            dst_ip = ip_generator() 
            
            print(f"Generating ICMP traffic between {src} and {dst_ip}, and TCP/UDP traffic with h1")
            src.cmd(f"ping {dst_ip} -c 100 &")
            src.cmd("iperf -p 5050 -c 10.0.0.1 &")
            src.cmd("iperf -p 5051 -u -c 10.0.0.1 &")
            
            print(f"{src} Downloading index.html from h1")
            src.cmd("wget http://10.0.0.1/index.html")
            print(f"{src} Downloading test.zip from h1")
            src.cmd("wget http://10.0.0.1/test.zip")

        h1.cmd("rm -f *.* /home/mininet/Downloads")
    
    print("--------------------------------------------------------------------------------")  
    net.stop()
    
    end_time = datetime.now()
    print("Execution Time:", end_time - start_time)