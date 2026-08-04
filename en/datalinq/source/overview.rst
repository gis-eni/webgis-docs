General
===========

**WebGIS DataLinq** is a powerful tool for querying, providing, and displaying data from various sources. The application enables both read and write access to data and represents a flexible solution for a wide range of use cases.

===============

Goals
-----

To ensure that **DataLinq** can be used as universally as possible in different applications, the following main goals were defined:

- **Simple Integration and Use**
  - Easy connection to different data sources

- **Detailed Access Control**
  - Separate management of permissions for queries and presentation

- **Flexible Data Output**
  - Providing results both as **raw data (JSON)** and in a formatted form

- **Data Editing**
  - Creation of **forms** for editing data records
  - **Fast and simple** modification of data

- **Advanced Analysis Options**
  - **Statistical evaluation** and analysis of data
  - **Visualization** of data records and analysis results in chart form
  - **Export** of data to various formats (e.g. CSV, PDF)

- **Creation of PDF Templates**
  - Providing **PDF templates** for generating reports and documents from query results
  - Parameterization of the templates for individual adjustment to the respective requirements

===============

Data Sources
------------

**WebGIS DataLinq** supports various data sources to ensure high flexibility when querying data. Possible data sources include:

- **Databases**
- **WebGIS REST API** queries
- **GeoJSON**
- **GeoRSS**
- **Plain Text**
- **Cypher** queries for graph databases
- **JsonApi** queries for REST APIs
  - Lists of values as text – ideal for selection and dropdown lists
- **Other WebGIS DataLinq applications**

===============

Output Options
---------------------

The query results can be output in different formats:

- **Raw Data**
  - Providing the query results in **JSON format**

- **Formatted Display**
  - Visualization as an **HTML view** using **ASP.NET Razor markup**
