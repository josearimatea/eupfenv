from trex_stl_lib.api import STLStream, STLPktBuilder, STLTXCont
from scapy.all import Ether, IP, UDP
import pprint

# Cria um stream básico
def create_test_stream():
    return STLStream(
        packet=STLPktBuilder(
            pkt=Ether()/IP(src="1.1.1.1", dst="2.2.2.2")/UDP(dport=1234, sport=1234)/("X"*100)
        ),
        mode=STLTXCont()
    )

# Imprime informações do stream
if __name__ == "__main__":
    stream = create_test_stream()
    pprint.pprint(stream)
