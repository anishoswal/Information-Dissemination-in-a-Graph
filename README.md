# CSE 575 Information Dissemination in a Graph

## Description
Two cases arise in controlling information dissemination: reduce/contain information flow and increase/enhance dissemination.<br />

**1. Reduce/Contain Dissemination:**

To reduce the information dissemination in a graph, the two approaches are to remove either nodes or edges from the graph. Both approaches have their applications in different situations.
For example, in social-media networks, we cannot just remove nodes(users) in most of the cases. So we use edge deletion. In other cases such as containing virus propagation, it is effective to use
node deletion. The Netshield algorithm removes the k nodes and Netmelt algorithm removes k edges from the graph.<br /><br />
        **- NetShield Algorithm:**<br />
            Given a graph, this algorithm finds the k best nodes to be removed to minimize the dissemination in the remaining nodes of the graph.
            This is the core problem for many applications:
                a. In a computer network, we want to find the k best nodes to be removed to minimize the spread of malware.
                b. In a law-enforcement setting, given a network of criminals, we want to neutralize or remove the nodes that will maximally scatter the graph.
            To compute the k nodes to be removed, we need a measure of vulnerability of the graph, a measure of shield-value for a set of k nodes. To obtain that, Netshield algorithm is used.<br /><br />
        **- NetMelt Algorithm:**<br />
            This algorithm contains the dissemination by removing a given number of edges, i.e. deleting a set of k edges from the graph to minimize the infected population. For example, we can consider\ the distribution of malware over a social network. Deleting user accounts may not be desirable, but deleting edges (‘unfriending’ people) may be more acceptable. We implemented both the methods mentioned above and analyzed which method provides better results for the chosen datasets in the results and evaluations section.<br />


**2. Increase/Enhance Dissemination:**<br />
This algorithm enhances the dissemination by adding a given number of edges. Specifically, we want to add a set of k new edges into the graph to maximize the population that adopts the information. For example, we could extend the social network scenario using the recent ‘Arab spring’ which often used Facebook and Twitter for coordinating events: we may want to maximize the spread of a potential piece of information.
After we analyze the results, we will integrate the above algorithms into an ensemble system which would be capable of determining actions that would need to be taken in order to either increase or decrease the flow of information, given the graph.<br /><br />


The program is split into two modules:<br />
**1. Netshield**<br />
    - plots - 
    **Output Plots for Karate and AS datasets.** <br />
    - alpha.txt - 
    **A small demo graph that is taken as input to the program.** <br />
    - asgraph.txt - 
    **AS Graph Dataset with nearly 12000 nodes and 25000 edges.**<br />
    - karate.txt - 
    **A small dataset with 34 nodes and 57 edges.**<br />
    - gelling_melting.py - 
    **The main program containing the algorithm for NetMelt and NetGel.**<br /><br />
    
    
**2. Netmelt_and_Netgel**<br />
    - plots - 
    **Output Plots for Karate dataset.** <br />
    - Netshield.py - 
    **The main program containing the algorithm for NetShield.**<br /><br />

## Tested Running Environment
**OS:** Ubuntu 18<br />
**Python:** 3.7

## Requriements
All requirements necessary can be found in [requirements.txt](requirements.txt)

```
sudo pip install -r requirements.txt
```

Each module has its own directory containing the corresponding code, running instructions(README.md) and sample output plots respectively.
