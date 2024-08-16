---
title: Data processing
description: Introduction to data processing
---


Local, high-performance and cloud computing must fulfil appropriate security standards to provide processing capacities for human data coordinated in 1+MG. Distinct processing events happen on the infrastructure: Localisation of the data and code to the appropriate platform (local or distributed) and data analysis by the individual data user who has acquired the access rights for the intended data use.  


### [Workflow](https://www.ga4gh.org/product/workflow-execution-service-wes/) <span class="badge badge-dark">Recommended<i class="fa-solid fa-thumbs-up"></i></span> & [Task Execution Service](https://www.ga4gh.org/product/task-execution-service-tes/) <span class="badge badge-dark">Recommended<i class="fa-solid fa-thumbs-up"></i></span>  (WES & TES)
The GA4GH Workflow Execution Service (WES) standard specifies how complex analytic pipelines can be specified in a standardised way to allow these pipelines to run in different locations, for example at different federated node: an important requirement in allowing users to send the analysis to the data rather than bring the data to the analysis which helps to ensure the data remains secure and conforms to the ELSI issues that apply to it. The Task Execution Service (TES) allows analysis pipelines to run on a wide range of heterogeneous infrastructure. For example, a user may wish to run the same variant calling pipeline on data hosted at three different nodes, but the compute infrastructure used by these nodes is different. While WES allows the pipeline to be specified in a standardised way, TES ensures that the task required to run the pipeline can be executed on different types of compute infrastructure, such as different high performance computing (HPC) orCloud environments. WES and TES together ensure that identical, repeatable, and consistent analysis can be run on different federated nodes irrespective of the underlying compute infrastructure.

### [Tool Registry Service (TRS)](https://www.ga4gh.org/product/tool-registry-service-trs/) <span class="badge badge-dark">Recommended<i class="fa-solid fa-thumbs-up"></i></span>

Researchers use genomics tools and workflows to conduct analyses in cloud computing environments. Tools and workflows, however, are often developed for a specific environment and are stored in a registry that services only associated platforms. Since each registry requires the tools and workflows it stores to meet a unique set of criteria, the contents of one registry are not guaranteed to work across multiple cloud environments. This lack of interoperability slows research and limits the variety of analyses that researchers can perform. Developed by the GA4GH Cloud Work Stream, the Tool Registry Service (TRS) API provides a standard mechanism to list, search, and register tools and workflows across multiple registries.

### [Report on federated learning technologies](https://zenodo.org/records/11550561)

Federated learning is described as a distributed machine learningtechnique in which multiple participants, which provide remote devices or siloed data centres, collaboratively train a shared machine learning model while keeping their data locally, better supporting data privacy. In this report, we provide a brief background on recent work on federated learning applied to genomics and health and how they are aligned to demonstrations performed in GDI, report the results of surveys conducted within the GDI participants regarding workflows and federated learning technologies, and discuss and evaluation of different possible scenarios for integrating these technologies into the GDI infrastructure.


### [Evaluation of distributed analysis and federated learning infrastructure solutions and recommendations for adoption](https://zenodo.org/records/10887366)

The completion of the first iteration of the Global Data Initiative technical demonstrators marks a significant milestone in collaborative efforts defining the next level of technologies that will be incorporated into the project. Three key demonstrators showcased advancements in distributed and federated analysis, cancer data mobilisation, and trusted research environments. Advancements in Distributed and Federated Analysis, Cancer Data Mobilization and Integration, and Advancements in Trusted Research Environments:






**We are still working on the content for this page.** If you are interested in adding to the page, then:

[Feel free to contribute](how_to_contribute){: class="btn btn-primary btn-lg rounded-pill"}

This is a community-driven website, so contributions are welcome! You will, of course, be listed as a contributor on the page.


