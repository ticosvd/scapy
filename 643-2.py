import optparse,ipaddress,time
import random
from  scapy.all import ICMP, IP, sr1, TCP, srloop,Raw


def sendpack(send_sa,timeout,ipaddress,port,sport,sipaddress ):
   if(send_sa.haslayer(TCP)):
       print ("DDDDDDDDDDDDDDDDDDD")
       #time.sleep(timeout)
       sendpack(sr1(IP(src=sipaddress,dst=ipaddress)/TCP(sport=sport,dport=port,flags='A', seq=send_sa.ack, ack=send_sa.seq + 1)/Raw("DKDJFKDJF"),timeout=1),timeout,ipaddress,port,sport,sipaddress)
  



def mainf():
   p=optparse.OptionParser()
   p.add_option('--ipaddress','-i',default='192.168.122.152')
   p.add_option('--spaddress','-s',default='192.168.122.1')
   p.add_option('--port','-p',default=10001)
   #p.add_option('--port','-p',default=20000)
   p.add_option('--timeout','-t',default=10)
   p.add_option('--count','-c',default=1)
   options,arguments=p.parse_args()
   
   for i in range(int(options.count)):
       
       sport = random.randint(1023,65535)
       print ("DDDDDDDDDDDDDd " ,options.ipaddress,' ',options.port," ", options.spaddress,"  " , sport) 
       synack=sr1(IP(src=options.spaddress,dst=options.ipaddress)/TCP(sport=sport,dport=options.port,flags='S'),timeout=10)

#   if (synack.haslayer(TCP)):
#       if(synack.getlayer(TCP).flags == 0x12):
 #      sendpack(sr1(IP(src=options.spaddress,dst=options.ipaddress)/TCP(sport=sport,dport=options.port,flags='A', seq=synack.ack, ack=synack.seq + 1),timeout=1),options.timeout,options.ipaddress,options.port,sport,options.spaddress)

   #sendpack(send_sa,options.timeout,options.ipaddress,options.port)
#   if(send_sa.haslayer(TCP)):
#       print ("DDDDDDDDDDDDDDDDDDD")
#
#       #time.sleep(options.timeout)
#       
#       srloop(IP(dst=options.ipaddress)/TCP(dport=options.port,flags='A', seq=synack.ack, ack=synack.seq + 1))
  
   #print("DDDDDDDDDDDDDDDD %s"  % resp)
if __name__=="__main__":
        mainf()

