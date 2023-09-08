---
title: Data models, standards & ontologies
description: Introduction to data standards
---

Within large Europe-wide initiatives like the 1+MG initiative both germline and tumour sequencing data is generated at different sites and by different laboratories and in different contexts (research vs. clinical).

The description of the phenotypic and clinical information is heterogeneous, mostly unstructured, and spread across multiple (often not integrated/linked) systems. It does not always capture the entire history of a patient and is mostly recorded in the local language.

To facilitate cross-border searching, linking and analysis of genomic and health data, this section of the 1+MG Framework includes a set of recommendations and guidelines that cover the minimal requirements for the provenance of the samples and the description of patient-specific phenotype and clinical data. Also, establishing and using standards for both sequencing and phenotypic and clinical data are, together with the ELSI standards, key elements in creating trust.

## [Documented best practices in sharing and linking phenotypic and genetic data](https://zenodo.org/record/7342855) <span class="badge badge-dark">Recommended<i class="fa-solid fa-thumbs-up"></i></span>
This document identifies and describes best practices on sharing and linking phenotypic and genetic data in both the healthcare sector as in the research setting to, as much as possible, avoid reinventing the wheel, learn from previous/current existing projects to improve performance and avoid mistakes made by others. The listed ’best practices’ have been identified by the 1+MG WG3 experts, who are nominated by the Member States, and are exemplary practices that have achieved results which could be used for larger-scale cross-border initiatives.

The areas of best practices covered are “data models and templates”, “Data interoperability, ontology and controlled terminology, ontology collections, mappings”, “Data standards”, “Data exchange standards”, “Data infrastructure, data management platforms and tools”, “Data governance, genomics data framework”, and “Data dictionaries”.

## [Phenotypic and clinical metadata framework 2v0](https://zenodo.org/record/7554481) <span class="badge badge-warning">Required<i class="fa-sharp fa-regular fa-star"></i></span>
One of the crucial instruments for 1+MG is a phenotypic and clinical metadata framework which describes, in a commonly understandable language, the principles, models, and recommendations for sharing and linking of phenotypic and clinical metadata and genetic metadata between the member states.  This framework document proposes to adhere to standards for data capture and exchange.  It provides guidance on which standards, terminologies, and tools to use.  

## [Data Use Ontology](https://www.ga4gh.org/product/data-use-ontology-duo/) <span class="badge badge-warning">Required<i class="fa-sharp fa-regular fa-star"></i></span>
The Data Use Ontology (DUO) is an ontology that describes the data use conditions that are applied to one or more datasets held within a node. As the DUO is an ontology, it is by design machine-readable. The conditions can affect the type of secondary use that can be performed on the original data. For example, the data can be restricted to a certain location, or to research within a certain disease. Each release of the DUO is versioned, ensuring that historic DUO attributes are maintained when the definition of the term is modified to reflect changes in the legal and technological landscape around genomic data.The DUO can be seen as part of the data Discoverability Functionality, and the Data Access Management Tools functionality. This is because the machine-readable attribute of the DUO allows prospective users to query data sets based on the data use conditions - for example, user A may wish to research disease X, so can filter out from available datasets all but that disease. The DUO can also be used to determine data access, for example by determining if the researcher who is applying for data access intends to use the data for a purpose allowed by the Data Access Committee or data controller.

## [Phenopackets](https://www.ga4gh.org/product/phenopackets/) <span class="badge badge-warning">Required<i class="fa-sharp fa-regular fa-star"></i></span>
The Phenopacket standard is designed to allow phenotypic information to be exchanged in a consistent standardised and structured format. It links phenotypic information with individual, genetic, and disease information. Phenopackets are already used by the rare disease community, for example in the Solve-RD project and RD-Connect, which makes them ideal as a standard to drive the exchange of phenotypic information between nodes or services.

## [DCAT](https://www.w3.org/TR/vocab-dcat-3/)
DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web.

## [DCAT-AP](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/11)
DCAT-AP is the implementation of the European standard to aggregate data collections across borders in a single portal (1+MG User Portal currently in development) that facilitates integration and discovery by users of 1+MG, EHDS and other EU Data Spaces


## 1+MG Minimal dataset for cancer <span class="badge badge-warning">Required<i class="fa-sharp fa-regular fa-star"></i></span> 
* paper in progress



**We are still working on the content for this page.** If you are interested in adding to the page, then:

[Feel free to contribute](how_to_contribute){: class="btn btn-primary btn-lg rounded-pill"}

This is a community-driven website, so contributions are welcome! You will, of course, be listed as a contributor on the page.
