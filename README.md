# Readme #

This is a Python library for creating workflows of Apache Airflow task instances that captures the provenance from the Apache Airflow task's logs and convert that to ProvWF RDF, according to the [Prov Workflow (ProvWF)](https://data.surroundaustralia.com/def/provworkflow) profile of the 
[PROV-O standard](https://www.w3.org/TR/2013/REC-prov-o-20130430/).

### How do I get set up? ###

* I follow the [Quick Start](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html) and run Airflow using **Docker** and **Docker Compose**.
* Running Airflow in Docker and Docker Compose:

### The program generates following output: ###

* Task 01: the number of cars seen in total
* Task 02: a sequence of lines where each line contains a date (in yyyy-mm-dd format) and the number of cars seen on that day (eg. 2016-11-23 289) for all days listed in the input file.
* Task 03: the top 3 half hours with most cars, in the same format as the input file
* Task 04: the 1.5 hour period with least cars



_Creator:_  
**Monir Moniruzzama**  
_Ontological Research Scientist_  
[SURROUND Australia Pty Ltd](https://surroundaustralia.com)  
<abm.mzkhan@surroundaustrlaia.com>
