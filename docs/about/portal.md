![horizontal line](media/image28.png){width="6.470197944006999in" height="0.11458333333333333in"} 
-------------------------------------------------------------------------------------------------

![](media/image1.png){width="5.171875546806649in"
height="2.793144138232721in"}

Portal and Dashboard\
User Guide

Version 1.0

**────────────────────────────────────**

**Revision History**

  **Date (MM/DD/YYYY)**   **Version \#**   **Changes Made By**   **Description of Change**
  ----------------------- ---------------- --------------------- -----------------------------------
  06/30/2020              1.0              Erin Friday           Initial draft.
  10/30/2020              2.0              Erin Friday           Updated for latest functionality.

**Table of Contents**

**[Introduction](#introduction) 3**

> [Common Fund Data Ecosystem (CFDE)](#common-fund-data-ecosystem-cfde)
> 3
>
> [Purpose of this Document](#purpose-of-this-document) 3
>
> [Login](#login) 4
>
> [View Your Profile](#view-your-profile) 5

**[Portal](#portal) 6**

> [Access the Portal](#access-the-portal) 6
>
> [Filter the Chart](#filter-the-chart) 6
>
> [Export the Chart](#export-the-chart) 8
>
> [Explore the Repository](#explore-the-repository) 8
>
> [Browse All Collections](#browse-all-collections) 9
>
> [Browse by Biosample](#browse-by-biosample) 10
>
> [Browse by Subject](#browse-by-subject) 11
>
> [Browse by File](#browse-by-file) 13
>
> [Browse by Project](#browse-by-project) 14
>
> [Browse by Vocabulary](#browse-by-vocabulary) 16
>
> [Browse by Data Contributors](#browse-by-data-contributors) 16
>
> [View Details](#view-details) 18
>
> [Refine Search Results](#refine-search-results) 20
>
> [Sort and View Search Results](#sort-and-view-search-results) 22
>
> [Export Search Results](#export-search-results) 22
>
> [Documentation](#documentation) 23
>
> [Latest News](#latest-news) 23

**[Dashboard](#dashboard) 24**

> [Access the Dashboard](#access-the-dashboard) 24
>
> [Filter the Bar Charts](#filter-the-bar-charts) 24
>
> [Filter the Anatomy by Assay Type across the Common Fund
> Chart](#filter-the-anatomy-by-assay-type-across-the-common-fund-chart)
> 26
>
> [Filter the Anatomy by Common Fund Program
> Chart](#filter-the-anatomy-by-common-fund-program-chart) 27
>
> [Export the Chart](#export-the-chart-1) 28

Introduction
============

Common Fund Data Ecosystem (CFDE)
---------------------------------

The CFDE is an effort to identify and solve issues that inhibit data
access and reuse across NIH Common Fund (CF) programs. The goal of the
CFDE is for Common Fund data to be more usable and useful both within a
single program and among data sets from multiple programs. By connecting
the data sets and making them more accessible, the CFDE is intended to
enable novel scientific research that was not possible before, including
hypothesis generation, discovery, and validation.

The Common Fund programs include:

-   [[4DN]{.ul}](https://www.4dnucleome.org/) -- 4D Nucleome

-   [[HMP]{.ul}](https://hmpdacc.org/) -- Human Microbiome Project

-   [[GTEx]{.ul}](https://gtexportal.org/home/) -- Genotype-Tissue
    > Expression

-   [[KidsFirst]{.ul}](https://kidsfirstdrc.org/) -- Gabriella Miller
    > Kids First Pediatric Research Program

-   [[LINCS]{.ul}](http://www.lincsproject.org/) -- Library of
    > Integrated Network-Based Cellular Signatures

-   [[MoTrPAC]{.ul}](https://www.motrpac.org/) -- Molecular Transducers
    > of Physical Activity Consortium

The specific goals of the CFDE are to:

-   Increase usability -- enable the uptake, reuse, and creation of
    > Common Fund (CF) data and tools.

-   Preserve data -- support the storage, sharing, and sustainability of
    > CF data sets.

-   Provide training -- maximize scientists' ability to use CF data and
    > other resources.

Purpose of this Document
------------------------

The CFDE website includes two modules to ensure the specific goals are
met and users can find data---the
[[portal]{.ul}](https://app.nih-cfde.org/) and the
[[dashboard]{.ul}](https://app.nih-cfde.org/dashboard.html). This
document describes those modules in detail. The goals of both the portal
and the dashboard are to establish FAIR data production by:

-   F -- Providing rich metadata using an entity-relationship model to
    > express relationships between diverse data elements.

-   A -- Offering rich access control and access to metadata via
    > standard HTTP web service interfaces.

-   I -- Integrating with standardized terms defined by collaborators,
    > consortium, and communities.

-   R -- Supporting dynamic model evolution so the presented data
    > accurately represents the current structure and state of knowledge
    > within an investigation.

To support these principals, the dashboard and data browser within the
portal emphasize well-defined metadata and data models, use controlled
vocabularies and ontologies, allow others to reproduce experiments, etc.

Login
-----

Currently, all features are available without a login, but this may
change in the future.

To log into the portal and dashboard:

1.  Click **Log In** in the upper-right of the page. The Login page
    > displays.![](media/image13.png){width="4.666666666666667in"
    > height="3.2083333333333335in"}

2.  Search for your organization using the drop-down, sign in with
    > Google, or sign in with an ORCID iD.

    a.  If you do not see your organization in the drop-down, then click
        > **Sign in with ORCID ID** to create a Globus account. A
        > warning message
        > displays.![](media/image4.png){width="4.666666666666667in"
        > height="4.229166666666667in"}

    b.  Click **Allow**.

    c.  Enter your information and click **Login**.

View Your Profile
-----------------

Select your name in the upper-right after logging in, click the down
arrow, and select **Profile**.

Portal
======

The CFDE portal is a hub for searching the CFDE data across all
programs. The main page of the portal (shown below) is meant for
high-level decision-making, whereas the repository (or "data browser")
allows users such as clinical researchers, bioinformatics power users,
and NIH program officers to search for CFDE data.

From the portal, you can:

-   View and export a dashboard bar chart.

-   Explore the repository of Common Fund data.

-   Access the full dashboard with additional summary charts.

-   Read documentation about the C2M2 and FAIR Cookbook.

-   See the latest news regarding the CFDE.

![](media/image30.png){width="6.5in" height="3.4305555555555554in"}

Access the Portal
-----------------

Access the portal directly by using this link:
[[https://app.nih-cfde.org/]{.ul}](https://app.nih-cfde.org/).

Filter the Chart
----------------

The portal chart is an interactive graphic that renders automatically
when different criteria are selected from the X-axis, Y-axis, and Stack
By drop-downs. For example, the chart below shows the number of files by
assay for each CF program.

![](media/image31.png){width="6.5in" height="3.4305555555555554in"}
-------------------------------------------------------------------

To filter the portal chart:

1.  Select an **X-axis** value from the drop-down. Options include:

-   CF Program

-   Data Type

-   Assay

-   Species

-   Anatomy

> The horizontal axis of the bar chart updates automatically with the
> option selected.

2.  Select a **Y-axis** value from the drop-down. Options include:

-   File Count

-   Data Volume

-   Sample Count

-   Subject Count

> The vertical axis of the bar chart updates automatically with the
> option selected.

3.  Select a **Stack By** value from the drop-down. Options include:

-   CF Program

-   Data Type

-   Assay

-   Species

-   Anatomy

> The bars are stacked/sorted automatically with the option selected and
> the color-coded key updates with the appropriate categories.

NOTE: The same X-axis option cannot be selected for the Stacked By
option, so the corresponding option in the Stacked By drop-down will be
disabled if it is already selected in the X-axis drop-down.

Export the Chart
----------------

The Export icon (![](media/image3.png){width="0.22916666666666666in"
height="0.22916666666666666in"}) displays next to each chart to export
the data as a PNG, SVG, or CSV file. The PNG and SVG exports are image
files of the chart, whereas the CSV export is a spreadsheet of the data.

Explore the Repository
----------------------

The CFDE repository, referred to as the "data browser," provides views
of the data based on the underlying data model and annotations. Using
the data browser, you can:

-   Search, explore, and browse collections of data

-   Navigate from one data record to the next by following their
    > relationships

-   Explore and export data collections

-   Share data with other users and cite the data for use in
    > publications

The portal includes multiple ways to access the repository so you can
view the data differently. For example, you can select "Browse All
Collections" to see the entire CFDE data collection or select "Browse by
Biosample" to see the data automatically pre-filtered by biosample. The
data that displays and the Refine Search options differ based on the
option selected.

The repository can be accessed in the following ways from the portal:

-   Select **Browse \> Collection** from the main menu bar. See the
    > [[Browse All Collections]{.ul}](#browse-all-collections) section
    > below for more information.

-   Click the **Search All Collections** button under Explore our
    > Repository. See the [[Browse All
    > Collections]{.ul}](#browse-all-collections) section below for more
    > information.

-   Click a link under Browse by Feature in the Explore our Repository
    > section to display a pre-filtered repository by one of the
    > following features (NOTE: These options also display under the
    > Browse drop-down in the main menu bar):

    -   Collection -- See the [[Browse All
        > Collections]{.ul}](#browse-all-collections) section below for
        > more information.

    -   Biosample -- See the [[Browse by
        > Biosample]{.ul}](#browse-by-biosample) section below for more
        > information.

    -   Subject -- See the [[Browse by
        > Subject]{.ul}](#browse-by-subject) section below for more
        > information.

    -   File -- See the [[Browse by File]{.ul}](#browse-by-file) section
        > below for more information.

-   Select **Browse \> Project** from the main menu bar. See the
    > [[Browse by Project]{.ul}](#browse-by-project) section below for
    > more information.

-   Select **Browse \> Vocabulary** from the main menu bar and select an
    > item from the list. See the [[Browse by
    > Vocabulary]{.ul}](#browse-by-vocabulary) section below for more
    > information.

-   Click **Data Contributors** under About this Website. See the
    > [[Browse by Data Contributors]{.ul}](#browse-by-data-contributors)
    > section below for more information.

### Browse All Collections

To search by all collections:

1.  Select one of the following options:

-   The **Browse \> Collection** option in the main menu bar.

-   The **Search All Collections** button under Explore our Repository.

-   The **Collection** link under Browse by Feature in the Explore our
    > Repository section.

The entire CFDE data collection displays in the data browser.

![](media/image6.png){width="6.826981627296588in"
height="3.588542213473316in"}

2.  The data browser includes the following columns in the results
    > table:

-   View -- Click the icon next to the appropriate record to view more
    > information about the record. See the [[View
    > Details]{.ul}](#view-details) section for more information.

-   ID Namespace -- A grouping of collection IDs.

-   ID -- The unique collection ID within the ID Namespace.

-   Name -- A short user-friendly label for the collection.

-   Description -- A user-friendly description of the collection.

-   Creation Time -- The date and time the collection was created.

3.  The results can be filtered using the Refine Search filter panel.
    > See the [[Refine Search Results]{.ul}](#refine-search-results)
    > section for more information. The panel includes the following
    > facets by which you can filter the results:

-   Data Type

-   File Format

-   Assay Type

-   Anatomy

-   Subject Taxonomy

-   Common Fund Program

-   Project

-   Subject Granularity

-   Subject Role

-   Collection Creation Time

-   File Creation Time

-   Biosample Creation Time

-   Part of Collection

-   Contained Subject

-   Contained Biosample

-   Contained File

### Browse by Biosample

To search by biosample:

1.  Select one of the following options:

-   The **Browse \> Biosample** option in the main menu bar.

-   The **Biosample** link under Browse by Feature in the Explore our
    > Repository section on the main portal page.

The data browser displays the CFDE data and filters related to
biosamples.

2.  The data browser includes the following columns in the results
    > table:

-   View -- Click the icon next to the appropriate record to view more
    > information about the record. See the [[View
    > Details]{.ul}](#view-details) section for more information.

-   ID Namespace -- A grouping of biosample IDs.

-   ID -- The unique biosample ID within the ID Namespace.

-   Project -- The project attributed as the source of the biosample.

-   Assay Type -- The assay type characterizing the biosample.

-   Anatomy -- The anatomy from which the biosample is derived.

-   Creation Time -- The date and time the biosample was created.

3.  The results can be filtered using the Refine Search filter panel.
    > See the [[Refine Search Results]{.ul}](#refine-search-results)
    > section for more information. The panel includes the following
    > facets by which you can filter the results:

-   Assay Type

-   Anatomy

-   Subject Taxonomy

-   Common Fund Program

-   Project

-   Creation Time

-   Source Subject

-   Described by File

-   Part of Collection

### Browse by Subject

To search by subject:

1.  Select one of the following options:

-   The **Browse \> Subject** option in the main menu bar.

-   The **Subject** link under Browse by Feature in the Explore our
    > Repository section on the main portal page.

> The data browser displays the CFDE data and filters related to
> subjects.

![](media/image25.png){width="6.707446412948381in"
height="3.5364588801399823in"}

2.  The data browser includes the following columns in the results
    > table:

-   View -- Click the icon next to the appropriate record to view more
    > information about the record. See the [[View
    > Details]{.ul}](#view-details) section for more information.

-   ID Namespace -- A grouping of subject IDs.

-   ID -- The unique subject ID within the ID Namespace.

-   Project -- The project attributed as the source of the subject.

-   Granularity -- The specificity of the subject description, i.e.,
    > organism versus cell-line.

-   Taxonomy -- The classification concept(s) that characterize the
    > subject.

-   Creation Time -- The date and time the subject record was created.

3.  The results can be filtered using the Refine Search filter panel.
    > See the [[Refine Search Results]{.ul}](#refine-search-results)
    > section for more information. The panel includes the following
    > facets by which you can filter the results:

-   Taxonomy

-   Subject Granularity

-   Taxonomic Role

-   Common Fund Program

-   Project

-   Creation Time

-   Derived Biosample

-   Described by File

-   Part of Collection

### Browse by File

To search by file:

1.  Select one of the following options:

-   The **Browse \> File** option in the main menu bar.

-   The **File** link under Browse by Feature in the Explore our
    > Repository section on the main portal page.

> The data browser displays the CFDE data and filters related to files.

![](media/image10.png){width="6.825987532808399in"
height="3.5989588801399823in"}

2.  The data browser includes the following columns in the results
    > table:

-   View -- Click the icon next to the appropriate record to view more
    > information about the record. See the [[View
    > Details]{.ul}](#view-details) section for more information.

-   ID Namespace -- A grouping of file IDs.

-   ID -- The unique file ID within the ID Namespace.

-   Filename -- The name of the file excluding prepended PATH
    > information.

-   Project -- The project attributed as the source of the file.

-   Size in Bytes -- The size of the file in bytes.

-   File Format -- The content format of the file.

-   Data Type -- The type of data represented by the file.

-   Creation Time -- The date and time the file was created.

3.  The results can be filtered using the Refine Search filter panel.
    > See the [[Refine Search Results]{.ul}](#refine-search-results)
    > section for more information. The panel includes the following
    > facets by which you can filter the results:

-   Data Type

-   File Format

-   Assay Type

-   Anatomy

-   Subject Taxonomy

-   Common Fund Program

-   Project

-   Subject Granularity

-   Subject Role

-   File Creation Time

-   Biosample Creation Time

-   Size in Bytes

-   Part of Collection

-   Described Biosample

-   Described Subject

### Browse by Project

To search by project:

1.  Select **Browse \> Project** from the main menu bar. The data
    > browser displays the CFDE data and filters related to projects.

![](media/image32.png){width="6.5in" height="3.4305555555555554in"}

2.  The data browser includes the following columns in the results
    > table:

-   View -- Click the icon next to the appropriate record to view more
    > information about the record. See the [[View
    > Details]{.ul}](#view-details) section for more information.

-   ID Namespace -- A grouping of project IDs.

-   ID -- The unique project ID within the ID Namespace.

-   Name -- A short user-friendly label for the ID Namespace.

-   Description -- A user-friendly description of the ID Namespace.

-   Creation Time -- The date and time the project was created.

3.  The results can be filtered using the Refine Search filter panel.
    > See the [[Refine Search Results]{.ul}](#refine-search-results)
    > section for more information. The panel includes the following
    > facets by which you can filter the results:

-   Creation Time

-   Super-Project

-   Sub-Project

-   Subject Granularity

-   Subject Role

-   Subject Taxonomy

-   Anatomy

-   Assay Type

-   File Format

-   Data Type

### Browse by Vocabulary

To search by vocabulary:

1.  Select **Browse \> Vocabulary** from the main menu bar.

2.  Select an item from the list:

-   Anatomy

-   Assay Type

-   Data Type

-   File Format

-   NCBI Taxonomy

-   Subject Granularity

-   Subject Role

> The data browser displays the CFDE data and filters related to the
> vocabulary term.

3.  The columns vary based on the vocabulary term selected.

4.  The available filters in the Refine Search panel vary based on the
    > vocabulary term selected. See the [[Refine Search
    > Results]{.ul}](#refine-search-results) section for more
    > information on how to filter the results.

### Browse by Data Contributors

To search by data contributors:

1.  Select one of the following options:

-   The **Browse \> ID Namespace** option in the main menu bar.

-   The **Data Contributors** link under About this Website on the main
    > portal page.

> The data browser displays the CFDE data and filters related to the
> data contributors.

![](media/image18.png){width="6.869792213473316in"
height="3.622053805774278in"}

2.  The data browser includes the following columns in the results
    > table:

-   View -- Click the icon next to the appropriate record to view more
    > information about the record. See the [[View
    > Details]{.ul}](#view-details) section for more information.

-   ID -- The unique ID within the ID Namespace.

-   Abbreviation -- A short label for the ID Namespace.

-   Name -- A short user-friendly label for the ID Namespace.

-   Description -- A user-friendly description of the ID Namespace.

3.  The results can be filtered using the Refine Search filter panel.
    > See the [[Refine Search Results]{.ul}](#refine-search-results)
    > section for more information. The panel includes the following
    > facets by which you can filter the results:

-   ID

-   Abbreviation

-   Name

-   Description

-   Biosample

-   Collection

-   File

-   Project

-   Subject

### View Details

Click the icon in the View column
(![](media/image22.png){width="0.2192979002624672in"
height="0.20833333333333334in"}) next to the appropriate record in the
results table to view more information about the record, such as the
metadata and links to the data files for that record. The options
available on the View Details page vary based on the record selected,
but this section of the document will use the screenshot below as an
example.

![](media/image14.png){width="6.5in" height="3.4305555555555554in"}

The metadata displays in the summary section at the top of the page. In
the example above, the metadata includes:

-   ID Namespace -- The hyperlink will display a View Details page for
    > the Genotype-Tissue Expression ID Namespace.

-   ID -- The unique ID within the ID Namespace.

-   Persistent ID -- An identifier that provides a single view of an
    > individual across numerous devices (desktop, mobile, in-app, etc.)
    > without duplication.

-   Defined by Project -- The hyperlink will display the Genotype-Tissue
    > Expression (GTEx) project in a separate data browser.

    -   Click **Table Mode** to display the project in a table with
        > additional information.

![](media/image16.png){width="6.5in" height="1.8055555555555556in"}

-   Click **Explore** to open the project in a separate data browser.

```{=html}
<!-- -->
```
-   Name -- A short user-friendly label for the ID Namespace.

-   Description -- A user-friendly description of the ID Namespace.

-   Creation Time -- The date and time the project was created.

The Sections panel on the left displays links to the contents of the
View Details page (similar to a Table of Contents) and the counts for
each section. Click one of the links to jump to that section of the View
Details page. You can also scroll down the page to view the sections
instead of using these links.\
![](media/image12.png){width="1.9375in" height="1.9375in"}

Click **Explore** in the gray section header to open the section in a
separate data browser, where you can use the Refine Search filter panel
to refine your search.\
![](media/image24.png){width="6.5in" height="0.4444444444444444in"}

Within each data file, you can click the **View** icon to view
additional information about the record.

The View Details menu bar in the upper-right of the page includes the
following options:

-   Show/Hide empty sections - Toggles the empty sections that display
    > on this page.

-   Export -- See the [[Export Search
    > Results]{.ul}](#export-search-results) section for more
    > information.

-   Share and Cite -- Opens a window with a versioned link and a live
    > link to use for sharing the data and citing the
    > data.![](media/image27.png){width="5.0625in"
    > height="2.3645833333333335in"}

### Refine Search Results

To use the facets to refine your search results:

1.  Click the down arrow next to the appropriate facet to display the
    > related attributes by which you can filter the results.\
    > ![](media/image26.png){width="2.3645833333333335in"
    > height="2.8645833333333335in"}

2.  Within a facet, you can perform any of the following to filter the
    > results:

-   Select the appropriate attribute checkbox(es).

-   Use the Search box to search for attributes only within that facet.

-   Click **Show More** to display additional information about the
    > attributes.

> ![](media/image20.png){width="5.5625in" height="2.46875in"}

3.  The time-related facets (Collection Creation Time, File Creation
    > Time, and Biosample Creation Time) and the Size in Bytes facet
    > function differently. To filter on a time-related facet, perform
    > one of the following:

-   Enter the **From** and **To** dates and times. Click the blue
    > checkmark to filter the results in the main data browser.

-   Use the interactive histogram to find the appropriate time period.
    > Click and drag anywhere in the graph to zoom into a smaller subset
    > of data. The From and To dates update automatically as you use the
    > histogram, but you must select the blue checkmark to filter the
    > results in the main data browser.

> ![](media/image5.png){width="2.3645833333333335in"
> height="3.6354166666666665in"}

### Sort and View Search Results

The data browser search results can be sorted and viewed using the
following functions:

-   The results table can be sorted by column header using the arrow
    > icon (![](media/image17.png){width="0.125in"
    > height="0.22916666666666666in"}).

-   View a different amount of results on one page by selecting a
    > different option for the **Displaying first number of records**
    > drop-down.\
    > ![](media/image15.png){width="2.7604166666666665in"
    > height="0.4479166666666667in"}

-   Use the **Search All Columns** search box at the top of the results
    > table to search for records within the table.\
    > ![](media/image8.png){width="3.1770833333333335in"
    > height="0.4583333333333333in"}

-   View additional results by clicking the **Next** button at the
    > bottom of the table.

-   Click the **X** next to the filter to remove the one filter from the
    > search results.\
    > ![](media/image29.png){width="2.9583333333333335in"
    > height="0.3854166666666667in"}

-   Click **Clear All Filters** to remove all filters from the search
    > results.

### Export Search Results

Search results can be exported from the main data browser and from the
View Details page. To export the search results:

1.  Click the **Export** button.\
    > ![](media/image7.png){width="1.6979166666666667in"
    > height="0.9166666666666666in"}

2.  Select **CSV** or **BAG**. The options that display will depend on
    > which page you are on:

-   CSV -- Opens a .csv file in Excel that includes the metadata
    > displayed in the search results in tabular format. All of the
    > search results display in the file; not just the first page of
    > results. The columns of the CSV file include:

    -   RID - The internal Record ID, which could be considered the
        > Primary Key.

    -   RCT - The timestamp representing the Record Creation Time.

    -   RMT - The timestamp representing the Record Modified Time.

    -   RCB - The Record Created By, which is the GlobusAuth identity
        > string (GUID) representing the creator of the record.

    -   RMB - The Record Modified By, which is the GlobusAuth identity
        > string (GUID) representing the user who last modified the
        > record.

    -   Id_namespace - A C2M2 column that represents the unique DCC
        > namespace identifier assigned by the CFDE to the DCC.

-   BAG -- This option is only available for the View Details page.
    > Downloads the data to a .bag file used for storing ROS message
    > data. Use this option if you want to download large files or if a
    > particular dataset includes many files.

Documentation
-------------

To access additional CFDE resources, select one of the following
options:

-   The **Documentation** link on the main portal page under About this
    > Website.

-   The **Documentation** button on the main menu bar.

The following resources are available:

-   The [[CFDE Crosscut Metadata Model
    > (C2M2)]{.ul}](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/spec-and-docs/C2M2-usage-guides-and-technical-documents/000-INTRODUCTION/)
    > is a flexible standard for describing biomedical experimental
    > data.

-   The [[FAIR
    > Cookbook]{.ul}](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/the-fair-cookbook/content/intro/)
    > provides introductory materials about various aspects of FAIRness,
    > including practical guides that show how to enhance digital
    > objects by adhering them to communicated-accepted standards.

-   The
    > [[glossary]{.ul}](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/CFDE-glossary/)
    > is a list of common CFDE terms with definitions.

Latest News
-----------

Refer to the "What's New" section of the portal for the latest news
related to the CFDE.

 

Dashboard
=========

The CFDE dashboard displays multiple charts for users to view high-level
data. The charts update automatically with the selections you make and
the precise numbers can be viewed by hovering over the chart. The charts
include:

-   Two bar charts that allow users to compare CFDE data by CF Program,
    > Data Type, Assay, Species, or Anatomy using File Count, Data
    > Volume, Sample Count, or Subject Count. The X-axis, Y-axis, and
    > Stack are configurable by all users to customize the data
    > summaries as needed. These bar charts display near each other so
    > you can compare two different data summaries.

-   Pie chart of the number of subjects by anatomy for a single assay
    > type across all Common Fund programs.

-   Pie chart of the number of samples by anatomy for a single Common
    > Fund program.

Access the Dashboard
--------------------

To access the dashboard:

-   Access the dashboard directly using this link:\
    > [[https://app.nih-cfde.org/dashboard.html]{.ul}](https://app.nih-cfde.org/dashboard.html)

-   Click **Dashboard** in the main menu bar from the portal.

Filter the Bar Charts
---------------------

The bar charts allow users to compare CFDE data by CF Program, Data
Type, Assay, Species, or Anatomy using File Count, Data Volume, Sample
Count, or Subject Count. The X-axis, Y-axis, and Stack are configurable
by all users to customize the data summaries as needed. The title of the
charts update automatically to reflect the options selected.

![](media/image21.png){width="6.5in" height="3.8194444444444446in"}
-------------------------------------------------------------------

To filter the bar charts:

1.  Select an **X-axis** value from the drop-down. Options include:

-   CF Program

-   Data Type

-   Assay

-   Species

-   Anatomy

> The horizontal axis of the bar chart updates automatically with the
> option selected.

2.  Select a **Y-axis** value from the drop-down. Options include:

-   File Count

-   Data Volume

-   Sample Count

-   Subject Count

> The vertical axis of the bar chart updates automatically with the
> option selected.

3.  Select a **Stack By** value from the drop-down. Options include:

-   CF Program

-   Data Type

-   Assay

-   Species

-   Anatomy

> The bars are stacked/sorted automatically with the option selected and
> the color-coded key updates with the appropriate categories.

NOTE: The same X-axis option cannot be selected for the Stacked By
option, so the corresponding option in the Stacked By drop-down will be
disabled if it is already selected in the X-axis drop-down.

Filter the Anatomy by Assay Type across the Common Fund Chart![](media/image9.png){width="3.2604166666666665in" height="3.4479166666666665in"}
----------------------------------------------------------------------------------------------------------------------------------------------

To filter the anatomy by assay type across the Common Fund chart:

1.  Select the **Assay Type** from the drop-down. Options include:

-   ChIP-seq assay

-   Hi-C assay

-   RNA-seq assay

-   Binding assay

-   Fluorescence detection assay

-   Histological assay

-   Immuno staining assay

-   Mass spectrometry assay

-   Material sample

-   Metabolite profiling assay

-   Protein expression profiling assay

-   Transcription profiling assay

> The pie chart updates automatically and displays the number of
> subjects for each anatomy category (e.g., blood plasma, digestive
> system, immune system, etc.) across all Common Fund programs based on
> the assay type selected.

Filter the Anatomy by Common Fund Program Chart
-----------------------------------------------

![](media/image11.png){width="3.3333333333333335in"
height="3.2916666666666665in"}

To filter the anatomy by Common Fund program chart:

1.  Select the **CF Program** from the drop-down. Options include:

-   4DN

-   HMP

-   GTEx

-   KidsFirst

-   LINCS

-   MoTrPAC

> The pie chart updates automatically and displays the number of samples
> for each anatomy category (e.g., blood plasma, digestive system,
> immune system, etc.) based on the Common Fund program selected.

Export the Chart
----------------

The Export icon (![](media/image3.png){width="0.22916666666666666in"
height="0.22916666666666666in"}) displays next to each chart to export
the data as a PNG, SVG, or CSV file. The PNG and SVG exports are image
files of the chart, whereas the CSV export is a spreadsheet of the data.
