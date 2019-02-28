FROM python:3-stretch

ADD scip/SCIPOptSuite-6.0.1-Linux.deb /hashcode/scip/SCIPOptSuite-6.0.1-Linux.deb

ADD scip/SCIPOptSuite-5.0.1-Linux.deb /hashcode/scip/SCIPOptSuite-5.0.1-Linux.deb

RUN apt-get update
RUN apt-get install -y libblas3 libgsl2 libgfortran3 liblapack3
#RUN dpkg -i /hashcode/scip/SCIPOptSuite-6.0.1-Linux.deb
RUN dpkg -i /hashcode/scip/SCIPOptSuite-5.0.1-Linux.deb

RUN pip3 install tqdm

RUN pip3 install pyscipopt==1.4
