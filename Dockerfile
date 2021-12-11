#IMAGE: wjxx/benchmark
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN set -ex ;\
 apt-get update ;\
 apt-get -y install python3 ;\
 apt-get -y install build-essential ;\
 apt-get -y install cmake ;\
 apt-get -y install ninja-build ;\
 apt-get -y install libssl-dev ;\
 rm -rf /var/lib/apt/lists/*

WORKDIR /work/cmake-3.22.1
ADD cmake-3.22.1.tar.gz /work/
RUN cmake -G Ninja -H. -Bbuild -DCMAKE_INSTALL_PREFIX=bin
ADD benchmark.py .

ENTRYPOINT ["python3","/work/cmake-3.22.1/benchmark.py"]


