from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSKernelSwitch, RemoteController

class MassiveTreeTopo(Topo):
    def build(self):
        n_core, n_agg, n_acc, n_hosts = 6, 6, 6, 16

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

def startNet():
    topo = MassiveTreeTopo()
    c0 = RemoteController('c0', ip='192.168.0.101', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=c0)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    startNet()



# 6 core switches

# 6 aggregation switches per core → 36 aggregation switches

# 6 access switches per aggregation → 216 access switches

# 16 hosts per access switch → 3456 hosts