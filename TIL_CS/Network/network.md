# Network structure

![Untitled](C:\Users\hanwonjong\Desktop\TIL\TIL_CS\Network\newwork_images\newwork_structure.png)

## network edge

- application and hosts(laptop, desktop, 웹 브라우저 등)

## network core

- routers
- network or networks

## access networks, physical media

- communication links

# Network edge

## end systems(hosts)

- run application programs

## client/server model

- 클라이언트 : 원할 때 마다 링크에 접속해서 서버와 연결
- 서버 : 항시 연결된 상태로 클라이언트의 요청 대기

## peer-peer model

- minimal use of dedicated servers
- e.g. Skype, BitTorrent, KaZaA

## connection-oriented service의 종류

### TCP

- 사용자에게 아래의 3가지 제공
  - reliable, in-order byte-stream data transfer
    - 신뢰성 : 메시지가 유출되지 않고 순서대로 전달됨
  - flow control
    - sender가 receiver에게 정보를 보낼 때, receiver에 맞게 속도를 조절
  - congestion control
    - 네트워크 상황에 맞게 조절
- 일반적인 웹브라우징 시 사용

### UDP(User Datagram Protocol)

- connectionless
- unreliable data transfer
- no flow control
- no congestion control
- reliable한 컨텐츠가 아닐 때 사용(ex : realtime voice)
- TCP에 비해 많은 네트워크 리소스, 컴퓨팅 리소스 절감

## protocol

- a human protocol and a computer network protocol:
  
  ![Untitled](C:\Users\hanwonjong\Desktop\TIL\TIL_CS\Network\newwork_images\protocol.png)

- 프로토콜 : **데이터의 교환 방식을 정의하는 규칙 체계**

# The Network Core

- mesh of interconnected routers
- the fundamental question: how is data transferred through net?
  - circuit switching : dedicated circuit per call telephone net
  - packet-switching : data sent thru net in discrete “chunks”

## Network Core: Circuit Switching

- **End-end resources reserved for “call”**
  - link bandwidth, switch capacity
  - dedicated resources: no sharing
  - circuit-lik (guaranteed) performance
  - call setup required
- 즉 가는 길을 미리 예약해 놓고 특정 사용자만 사용하도록(유선전화망)

## Packet Switching : Statistical Multiplexing

![Untitled](C:\Users\hanwonjong\Desktop\TIL\TIL_CS\Network\newwork_images\packet_switching.png)

- Sequence of A & B packets does not have fixed pattern, shared on demand → statistical multiplexing.
- TDM(Time Division Multiplexing : 시분할 다중화) : each host gets same slot in revolving TDM frame.
- 그냥 패킷 단위로 끊어서 데이터 전송하는 거라고 생각하면 됨.

## Packet switching vs Circuit switching

![Untitled](C:\Users\hanwonjong\Desktop\TIL\TIL_CS\Network\newwork_images\Packet_switching_vs_Circuit_switching.png)

- Packet switching allows more users to use network
  - 1 Mb/s link
  - each user:
    - 100 kb/s when active
    - active 10% of time
  - circuit switching:
    - 10 users
  - packet switching:
    - with 35 users. probabilit > 10 active less than .0004
